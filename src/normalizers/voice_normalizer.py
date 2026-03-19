"""
Converts a raw voice transcript into a CanonicalDocument.

Voice transcripts are structured like chat logs but come as plain
text with "Speaker N:" prefixes. We keep the speaker labels intact
since they provide useful context for the NER model.
"""
import uuid
from src.schema import CanonicalDocument, SourceType


def normalize_voice(raw_text: str, doc_id: str = None) -> CanonicalDocument:
    """
    Parse a raw voice transcript string into a CanonicalDocument.

    Args:
        raw_text:  The raw transcript as a plain text string
        doc_id:    Optional ID. Auto-generated if not provided.

    Returns:
        A CanonicalDocument with cleaned transcript text.
    """
    lines   = []
    speakers = set()

    for line in raw_text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        lines.append(line)
        # Track unique speakers as metadata
        if line.startswith("Speaker"):
            speaker = line.split(":")[0].strip()
            speakers.add(speaker)

    clean_text = "\n".join(lines)

    return CanonicalDocument(
        doc_id   = doc_id or str(uuid.uuid4()),
        source   = SourceType.VOICE,
        text     = clean_text,
        metadata = {
            "speaker_count": str(len(speakers)),
            "speakers":      ", ".join(sorted(speakers))
        }
    )