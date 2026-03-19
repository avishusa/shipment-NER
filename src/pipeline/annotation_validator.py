"""
Validates annotated examples in (text, [(entity, label)]) format.
Checks that every entity string can actually be found in the text,
and that all labels are valid.

Run with: python -m src.pipeline.annotation_validator
"""
from data.annotated.annotations import ANNOTATED_EXAMPLES
from src.schema import EntityLabel


def validate_annotations(examples: list) -> bool:
    print(f"Validating {len(examples)} annotated examples...\n")

    all_valid  = True
    all_labels = {label.value for label in EntityLabel}

    for i, (text, entities) in enumerate(examples):
        has_error = False

        for entity_text, label in entities:

            # Check 1: label must be known
            if label not in all_labels:
                print(f"  [Example {i+1}] UNKNOWN LABEL: '{label}'")
                has_error = True
                continue

            # Check 2: entity text must exist in the document text
            if entity_text not in text:
                print(f"  [Example {i+1}] NOT FOUND in text: "
                      f"'{entity_text}' ({label})")
                has_error = True

        if has_error:
            all_valid = False
            print(f"  Full text: {repr(text[:80])}...\n")
        else:
            found = ", ".join(
                f"'{e}'={l}" for e, l in entities
            )
            print(f"  [Example {i+1}] OK — {found}")

    print()
    if all_valid:
        print("All examples valid. Ready for export.")
    else:
        print("Errors found. Fix annotations before exporting.")

    return all_valid


if __name__ == "__main__":
    validate_annotations(ANNOTATED_EXAMPLES)