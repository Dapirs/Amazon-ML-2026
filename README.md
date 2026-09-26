# Amazon-ML-2026

## Setup

The directories `training_datasets/` and `cleaned_datasets/` are listed in `.gitignore`. After cloning this repository, you need to create them manually:

```bash
mkdir training_datasets cleaned_datasets
```

Place the following four files inside **training_datasets**:

1. `train_ground_truth.tsv`
2. `train_source1.tsv`
3. `train_source2.tsv`
4. `train_source3.tsv`

These files are required for the training pipeline.

## Project Architecture

```
project_root/
├─ src/               # Source code
├─ training_datasets/ # Raw training data (git‑ignored)
├─ cleaned_datasets/  # Processed data (git‑ignored)
├─ models/            # Saved model checkpoints
└─ README.md
```

(Adjust the diagram as needed for your specific components.)
