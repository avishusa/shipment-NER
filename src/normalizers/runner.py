"""
Reads all raw source files and runs them through
their respective normalizers. Prints a summary of
each resulting CanonicalDocument.

Run with: python -m src.normalizers.runner
"""
from pathlib import Path
from src.normalizers.chat_normalizer  import normalize_chat
from src.normalizers.email_normalizer import normalize_email
from src.normalizers.voice_normalizer import normalize_voice


def run_all():
    base = Path("data/raw")

    sources = [
        (base / "chat"  / "sample_chat.json",  normalize_chat,  "read_text"),
        (base / "email" / "sample_email.txt",  normalize_email, "read_text"),
        (base / "voice" / "sample_voice.txt",  normalize_voice, "read_text"),
    ]

    for path, normalizer, _ in sources:
        raw  = path.read_text(encoding="utf-8")
        doc  = normalizer(raw)

        print(f"{'='*55}")
        print(f"doc_id  : {doc.doc_id}")
        print(f"source  : {doc.source.value}")
        print(f"metadata: {doc.metadata}")
        print(f"text preview:")
        for line in doc.text.splitlines()[:4]:
            print(f"  {line}")
        print()


if __name__ == "__main__":
    run_all()