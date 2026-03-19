"""
Quick sanity check for the canonical schema.
Run with: python -m src.schema_validator
"""
from src.schema import CanonicalDocument, Entity, EntityLabel, SourceType


def main():
    # Simulate what a normalized email document would look like
    doc = CanonicalDocument(
        doc_id="email_001",
        source=SourceType.EMAIL,
        text=(
            "Shipment SHP-1042 is currently in transit from Chicago to Houston. "
            "Expected arrival is March 28. Delay due to weather hold."
        ),
        entities=[
            Entity(text="SHP-1042",     label=EntityLabel.SHIPMENT_ID,  start=9,  end=17),
            Entity(text="Chicago",      label=EntityLabel.ORIGIN,        start=45, end=52),
            Entity(text="Houston",      label=EntityLabel.DESTINATION,   start=56, end=63),
            Entity(text="March 28",     label=EntityLabel.ETA,           start=88, end=96),
            Entity(text="weather hold", label=EntityLabel.DELAY_REASON,  start=108, end=120),
        ],
        metadata={"sender": "ops@carrier.com", "subject": "Shipment Update"}
    )

    print(f"Document ID : {doc.doc_id}")
    print(f"Source      : {doc.source}")
    print(f"Text        : {doc.text[:60]}...")
    print(f"Entities    : {len(doc.entities)} found")
    print()
    for ent in doc.entities:
        # Verify the span actually matches the text
        extracted = doc.text[ent.start:ent.end]
        match = "OK" if extracted == ent.text else f"MISMATCH (got '{extracted}')"
        print(f"  [{ent.label.value:<14}] '{ent.text}' at [{ent.start}:{ent.end}] → {match}")


if __name__ == "__main__":
    main()