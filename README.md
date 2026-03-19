# Shipment NER

A production-grade NLP pipeline that extracts shipment entities (IDs, origins,
destinations, ETAs, etc.) from chat logs, email threads, and voice transcripts.

## Quickstart
```bash
git clone https://github.com/YOUR_USERNAME/shipment-ner.git
cd shipment-ner
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Project Structure
```
shipment-ner/
├── data/
│   ├── raw/          # Original source files (chat, email, voice)
│   ├── processed/    # Normalized canonical documents
│   └── annotated/    # Labeled training data
├── src/
│   ├── normalizers/  # Source-specific parsers
│   ├── pipeline/     # Training and inference logic
│   └── api/          # FastAPI app
├── models/           # Saved trained models
├── tests/            # pytest test suite
├── notebooks/        # Exploration and analysis
└── docs/             # Project documentation
```