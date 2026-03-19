from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class SourceType(str, Enum):
    """The three supported input sources."""
    CHAT  = "chat"
    EMAIL = "email"
    VOICE = "voice"


class EntityLabel(str, Enum):
    """All valid NER entity types for V1."""
    SHIPMENT_ID  = "SHIPMENT_ID"
    WAYBILL_ID   = "WAYBILL_ID"
    EQUIPMENT_ID = "EQUIPMENT_ID"
    ORIGIN       = "ORIGIN"
    DESTINATION  = "DESTINATION"
    STATUS       = "STATUS"
    ETA          = "ETA"
    DELAY_REASON = "DELAY_REASON"
    COMMODITY    = "COMMODITY"
    WEIGHT       = "WEIGHT"
    CARLOADS     = "CARLOADS"


@dataclass
class Entity:
    """
    A single extracted entity span from a document.

    Attributes:
        text:   The raw text of the entity (e.g. "SHP-1042")
        label:  The entity type (e.g. EntityLabel.SHIPMENT_ID)
        start:  Character offset where the entity starts in the text
        end:    Character offset where the entity ends in the text
    """
    text:  str
    label: EntityLabel
    start: int
    end:   int


@dataclass
class CanonicalDocument:
    """
    The unified internal representation of any ingested document,
    regardless of its original source format.

    Attributes:
        doc_id:    Unique identifier for this document
        source:    Where it came from (chat / email / voice)
        text:      The clean, normalized plain text
        entities:  List of extracted entities (empty before inference)
        metadata:  Any extra source-specific info (optional)
    """
    doc_id:   str
    source:   SourceType
    text:     str
    entities: list[Entity]        = field(default_factory=list)
    metadata: dict[str, str]      = field(default_factory=dict)