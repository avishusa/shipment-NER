import uuid
from src.schema import CanonicalDocument, SourceType


def normalize_email(raw_text: str, doc_id: str = None) -> CanonicalDocument:
    headers = {}
    body_lines = []
    in_body = False

    known_headers = {"from", "to", "subject", "date", "cc", "bcc"}

    for line in raw_text.strip().splitlines():
        stripped = line.strip()

        if not in_body:
            if stripped == "":
                in_body = True
                continue

            if ":" in line:
                key, _, value = line.partition(":")
                key_clean = key.strip().lower()

                if key_clean in known_headers:
                    headers[key_clean] = value.strip()
                    continue

            in_body = True

        body_lines.append(line)

    body_text = "\n".join(body_lines).strip()

    return CanonicalDocument(
        doc_id=doc_id or str(uuid.uuid4()),
        source=SourceType.EMAIL,
        text=body_text,
        metadata={
            "from": headers.get("from", ""),
            "to": headers.get("to", ""),
            "subject": headers.get("subject", ""),
            "date": headers.get("date", "")
        }
    )