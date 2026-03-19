"""
Pydantic models defining the shape of API requests and responses.

Pydantic is a data validation library. When FastAPI receives
a request, it automatically validates it against these models
and returns a clear error if anything is wrong or missing.
"""
from pydantic import BaseModel, Field
from src.schema import SourceType


class ExtractionRequest(BaseModel):
    """
    The body of a POST /extract request.

    Attributes:
        text:    The raw input text to extract entities from.
        source:  Which source type the text came from.
        doc_id:  Optional identifier for this document.
    """
    text:   str        = Field(..., min_length=1,
                               description="Raw input text to extract entities from")
    source: SourceType = Field(SourceType.CHAT,
                               description="Source type: chat, email, or voice")
    doc_id: str | None = Field(None,
                               description="Optional document identifier")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "Shipment SHP-1042 departed Chicago. ETA is March 28.",
                    "source": "chat",
                    "doc_id": "chat_001"
                }
            ]
        }
    }


class ExtractedEntity(BaseModel):
    """A single extracted entity in the API response."""
    text:  str
    label: str
    start: int
    end:   int


class ExtractionResponse(BaseModel):
    """
    The response body from POST /extract.

    Attributes:
        doc_id:        The document identifier.
        source:        The source type.
        entity_count:  Total number of entities found.
        entities:      List of extracted entities.
    """
    doc_id:       str
    source:       str
    entity_count: int
    entities:     list[ExtractedEntity]