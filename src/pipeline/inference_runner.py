"""
Runs the trained model end-to-end on all three sample sources.
Shows extracted entities for each document.

Run with: python -m src.pipeline.inference_runner
"""
from pathlib import Path
from src.pipeline.inferencer import ShipmentExtractor


def print_results(doc) -> None:
    """Pretty print extraction results for a document."""
    print(f"{'='*60}")
    print(f"doc_id : {doc.doc_id}")
    print(f"source : {doc.source.value}")
    print(f"entities found: {len(doc.entities)}")
    print()

    if not doc.entities:
        print("  No entities extracted.")
    else:
        # Group entities by label for clean display
        by_label = {}
        for ent in doc.entities:
            by_label.setdefault(ent.label.value, []).append(ent.text)

        for label, texts in sorted(by_label.items()):
            print(f"  {label:<16} {', '.join(texts)}")
    print()


def main():
    extractor = ShipmentExtractor()
    print()

    # --- Chat ---
    chat_raw = Path("data/raw/chat/sample_chat.json").read_text(encoding="utf-8")
    chat_doc = extractor.extract_from_chat(chat_raw)
    print_results(chat_doc)

    # --- Email ---
    email_raw = Path("data/raw/email/sample_email.txt").read_text(encoding="utf-8")
    email_doc = extractor.extract_from_email(email_raw)
    print_results(email_doc)

    # --- Voice ---
    voice_raw = Path("data/raw/voice/sample_voice.txt").read_text(encoding="utf-8")
    voice_doc = extractor.extract_from_voice(voice_raw)
    print_results(voice_doc)

    # --- Custom text (simulating an API call) ---
    print(f"{'='*60}")
    print("Custom text input (simulating API call):")
    print()
    custom_doc = extractor.extract_from_text(
        "Shipment SHP-9955 is on hold due to a weather hold near Atlanta. "
        "Equipment BNSF-771100 is carrying steel coils, 3 carloads, 45 tons. "
        "New ETA is April 12."
    )
    print_results(custom_doc)


if __name__ == "__main__":
    main()