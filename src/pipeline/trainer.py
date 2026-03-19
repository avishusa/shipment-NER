"""
Trains a spaCy NER model on the exported training data.
Saves the trained model to the models/ directory.

Run with: python -m src.pipeline.trainer
"""
import subprocess
import sys
from pathlib import Path


def train(
    config_path:    Path = Path("config.cfg"),
    output_dir:     Path = Path("models/shipment_ner"),
    train_data:     Path = Path("data/processed/train.spacy"),
    dev_data:       Path = Path("data/processed/dev.spacy"),
):
    """
    Calls spaCy's training command programmatically.

    spaCy's train command handles:
    - Loading the config
    - Initializing the model with our entity labels
    - Running training iterations
    - Evaluating on dev set after each epoch
    - Saving the best model automatically
    """

    # Verify required files exist before starting
    for path in [config_path, train_data, dev_data]:
        if not path.exists():
            raise FileNotFoundError(
                f"Required file not found: {path}\n"
                f"Make sure you have run the data exporter first."
            )

    output_dir.mkdir(parents=True, exist_ok=True)

    print("Starting NER model training...")
    print(f"  Config    : {config_path}")
    print(f"  Train data: {train_data}")
    print(f"  Dev data  : {dev_data}")
    print(f"  Output    : {output_dir}")
    print()

    # Build the spaCy train command
    command = [
        sys.executable, "-m", "spacy", "train",
        str(config_path),
        "--output",    str(output_dir),
        "--paths.train", str(train_data),
        "--paths.dev",   str(dev_data),
    ]

    # Run training — output streams directly to your terminal
    result = subprocess.run(command)

    if result.returncode != 0:
        print("\nTraining failed. Check the output above for errors.")
        sys.exit(1)

    best_model = output_dir / "model-best"
    if best_model.exists():
        print(f"\nTraining complete.")
        print(f"Best model saved to: {best_model}")
    else:
        print("\nTraining finished but no model-best found.")
        print("This can happen if dev set score never improved.")


if __name__ == "__main__":
    train()