"""
Converts validated annotations into spaCy binary format.
Computes character offsets automatically from entity strings.
Produces train.spacy and dev.spacy in data/processed/.

Run with: python -m src.pipeline.data_exporter
"""
import random
from pathlib import Path
import spacy
from spacy.tokens import DocBin
from data.annotated.annotations import ANNOTATED_EXAMPLES
from src.pipeline.annotation_validator import validate_annotations


def compute_offsets(text: str, entities: list) -> list:
    """
    Convert (entity_text, label) pairs into (start, end, label)
    triples by searching for each entity string in the text.

    Handles duplicate entity strings (e.g. SHP-1042 appearing
    twice) by searching forward from the last found position.
    """
    result    = []
    search_from = 0

    for entity_text, label in entities:
        start = text.find(entity_text, search_from)
        if start == -1:
            print(f"  [WARNING] Could not find '{entity_text}' "
                  f"after position {search_from} — skipping")
            continue
        end = start + len(entity_text)
        result.append((start, end, label))
        # Move search cursor forward so duplicate entities
        # get distinct positions
        search_from = end

    return result


def export_spacy_format(
    examples:    list,
    output_dir:  Path,
    train_ratio: float = 0.8,
    seed:        int   = 42
) -> None:

    if not validate_annotations(examples):
        raise ValueError("Fix annotation errors before exporting.")

    output_dir.mkdir(parents=True, exist_ok=True)
    nlp = spacy.blank("en")

    random.seed(seed)
    shuffled = examples.copy()
    random.shuffle(shuffled)

    split_idx  = int(len(shuffled) * train_ratio)
    train_data = shuffled[:split_idx]
    dev_data   = shuffled[split_idx:]

    def build_docbin(data: list, split_name: str) -> DocBin:
        db      = DocBin()
        skipped = 0

        for text, entities in data:
            doc    = nlp.make_doc(text)
            offsets = compute_offsets(text, entities)
            ents   = []

            for start, end, label in offsets:
                span = doc.char_span(
                    start, end,
                    label=label,
                    alignment_mode="contract"
                )
                if span is None:
                    print(f"  [WARNING] Span alignment failed: "
                          f"'{text[start:end]}' ({label}) — skipping")
                    skipped += 1
                    continue
                ents.append(span)

            doc.ents = ents
            db.add(doc)

        print(f"  {split_name}: {len(data)} docs, {skipped} spans skipped")
        return db

    print("\nExporting to spaCy format...")
    train_db = build_docbin(train_data, "train")
    dev_db   = build_docbin(dev_data,   "dev")

    train_path = output_dir / "train.spacy"
    dev_path   = output_dir / "dev.spacy"

    train_db.to_disk(train_path)
    dev_db.to_disk(dev_path)

    print(f"\nSaved:")
    print(f"  {train_path}  ({len(train_data)} docs)")
    print(f"  {dev_path}    ({len(dev_data)} docs)")


if __name__ == "__main__":
    export_spacy_format(
        examples   = ANNOTATED_EXAMPLES,
        output_dir = Path("data/processed")
    )