"""
FastAPI application for the shipment NER system.

Exposes a single endpoint:
    POST /extract  —  accepts text, returns extracted entities

Run with:
    uvicorn src.api.app:app --reload
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from src.api.models import ExtractionRequest, ExtractionResponse, ExtractedEntity
from src.pipeline.inferencer import ShipmentExtractor
from src.normalizers.chat_normalizer  import normalize_chat
from src.normalizers.email_normalizer import normalize_email
from src.normalizers.voice_normalizer import normalize_voice
from src.schema import SourceType
import json


# Global extractor instance — loaded once at startup
extractor: ShipmentExtractor | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan handler: runs on startup and shutdown.
    We load the model here so it is ready before the
    first request arrives. Loading inside a request
    would make the first call very slow.
    """
    global extractor
    print("Loading NER model...")
    extractor = ShipmentExtractor()
    print("Model ready.")
    yield
    # Cleanup on shutdown (nothing needed here)
    print("Shutting down.")


app = FastAPI(
    title       = "Shipment NER API",
    description = "Extracts shipment entities from chat, email, and voice text.",
    version     = "1.0.0",
    lifespan    = lifespan,
)


@app.get("/health")
def health_check():
    """
    Simple health check endpoint.
    Returns 200 if the API is running and the model is loaded.
    """
    return {
        "status":       "ok",
        "model_loaded": extractor is not None,
    }


@app.post("/extract", response_model=ExtractionResponse)
def extract_entities(request: ExtractionRequest):
    """
    Extract shipment entities from input text.

    Normalizes the text based on source type, runs NER,
    and returns structured entity results.
    """
    if extractor is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please try again shortly."
        )

    try:
        # Route to the correct normalizer based on source type
        if request.source == SourceType.CHAT:
            # Check if it looks like JSON (chat format)
            try:
                json.loads(request.text)
                doc = extractor.extract_from_chat(request.text, request.doc_id)
            except json.JSONDecodeError:
                # Plain text fallback
                doc = extractor.extract_from_text(
                    request.text, request.source, request.doc_id
                )

        elif request.source == SourceType.EMAIL:
            doc = extractor.extract_from_email(request.text, request.doc_id)

        elif request.source == SourceType.VOICE:
            doc = extractor.extract_from_voice(request.text, request.doc_id)

        else:
            doc = extractor.extract_from_text(
                request.text, request.source, request.doc_id
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Extraction failed: {str(e)}"
        )

    return ExtractionResponse(
        doc_id       = doc.doc_id,
        source       = doc.source.value,
        entity_count = len(doc.entities),
        entities     = [
            ExtractedEntity(
                text  = ent.text,
                label = ent.label.value,
                start = ent.start,
                end   = ent.end,
            )
            for ent in doc.entities
        ]
    )