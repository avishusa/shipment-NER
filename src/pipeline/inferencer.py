"""
Inference pipeline for the shipment NER model.

Accepts raw text from any supported source, normalizes it
into a CanonicalDocument, runs the NER model, and returns
the document with extracted entities populated.

Usage:
    from src.pipeline.inferencer import ShipmentExtractor
    extractor = ShipmentExtractor()
    doc = extractor.extract_from_text("SHP-1042 departed Chicago")
"""
import spacy
from pathlib import Path
from src.schema import CanonicalDocument, Entity, EntityLabel, SourceType
from src.normalizers.chat_normalizer  import normalize_chat
from src.normalizers.email_normalizer import normalize_email
from src.normalizers.voice_normalizer import normalize_voice


class ShipmentExtractor:
    """
    Loads the trained NER model and runs extraction
    on any supported input source.
    """

    def __init__(self, model_path: Path = Path("models/shipment_ner/model-best")):
        """
        Load the trained spaCy model from disk.

        Args:
            model_path: Path to the saved model directory.
        """
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model not found at {model_path}.\n"
                f"Run the trainer first: python -m src.pipeline.trainer"
            )
        print(f"Loading model from {model_path}...")
        self.nlp = spacy.load(model_path)
        print(f"Model loaded. Labels: {self.nlp.get_pipe('ner').labels}")

    def _run_ner(self, doc: CanonicalDocument) -> CanonicalDocument:
        """
        Run NER on a CanonicalDocument and populate its entities list.

        Args:
            doc: A CanonicalDocument with text but no entities yet.

        Returns:
            The same document with entities populated.
        """
        spacy_doc = self.nlp(doc.text)

        doc.entities = [
            Entity(
                text  = ent.text,
                label = EntityLabel(ent.label_),
                start = ent.start_char,
                end   = ent.end_char,
            )
            for ent in spacy_doc.ents
        ]
        return doc

    def extract_from_text(
        self,
        text:    str,
        source:  SourceType = SourceType.CHAT,
        doc_id:  str = None
    ) -> CanonicalDocument:
        """
        Run extraction on plain text directly.
        Useful for quick testing and API calls.

        Args:
            text:   Plain text to extract entities from.
            source: Which source type to tag this document as.
            doc_id: Optional document ID.

        Returns:
            CanonicalDocument with entities populated.
        """
        doc = CanonicalDocument(
            doc_id = doc_id or "manual_input",
            source = source,
            text   = text,
        )
        return self._run_ner(doc)

    def extract_from_chat(self, raw_json: str, doc_id: str = None) -> CanonicalDocument:
        """Normalize a raw chat JSON string and extract entities."""
        doc = normalize_chat(raw_json, doc_id)
        return self._run_ner(doc)

    def extract_from_email(self, raw_text: str, doc_id: str = None) -> CanonicalDocument:
        """Normalize a raw email string and extract entities."""
        doc = normalize_email(raw_text, doc_id)
        return self._run_ner(doc)

    def extract_from_voice(self, raw_text: str, doc_id: str = None) -> CanonicalDocument:
        """Normalize a raw voice transcript and extract entities."""
        doc = normalize_voice(raw_text, doc_id)
        return self._run_ner(doc)