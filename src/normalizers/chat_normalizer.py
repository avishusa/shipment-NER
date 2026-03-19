"""
Converts a raw chat JSON conversation into a CanonicalDocument.

Chat logs are multi-turn conversations. We join all message
text into a single string so the NER model sees full context.
"""
import json
import uuid
from src.schema import CanonicalDocument, SourceType


def normalize_chat(raw_json: str, doc_id: str = None) -> CanonicalDocument:
    """
    Parse a raw chat JSON string into a CanonicalDocument.

    Args:
        raw_json:  The raw JSON string from the chat source
        doc_id:    Optional ID. Auto-generated if not provided.

    Returns:
        A CanonicalDocument with joined text and source metadata.
    """
    data = json.loads(raw_json)

    # Join all messages into one block of text
    # We prefix each line with the speaker so context is preserved
    lines = []
    for msg in data.get("messages", []):
        speaker = msg.get("speaker", "unknown").capitalize()
        text    = msg.get("text", "").strip()
        lines.append(f"{speaker}: {text}")

    joined_text = "\n".join(lines)

    return CanonicalDocument(
        doc_id   = doc_id or data.get("conversation_id") or str(uuid.uuid4()),
        source   = SourceType.CHAT,
        text     = joined_text,
        metadata = {
            "conversation_id": data.get("conversation_id", ""),
            "message_count":   str(len(data.get("messages", [])))
        }
    )