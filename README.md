# ArmScribe AI

ArmScribe AI is a university project for **Programming for AI & Machine
Learning**. It will recognize handwritten Armenian uppercase characters using
machine learning while comparing a PyTorch CNN with a k-Nearest Neighbors
baseline.

**Authors:** Ahmad Serhal and Melissa Karakouzian

> Status: Phase 1 — project initialization. Dataset processing, model
> implementation, training, evaluation, and recognition are deliberately not
> implemented yet.

## Objectives and planned features

- Recognize 39 Armenian uppercase letters.
- Compare a CNN and k-NN baseline, including augmentation experiments.
- Use writer-independent evaluation to assess generalization to unseen writers.
- Report accuracy, precision, recall, F1-score, confusion matrices, and
  per-character error analysis across three random seeds.
- Deliver a Streamlit interface with drawing and image-upload support in a
  later phase.

## Technology stack

Python 3.11+, PyTorch, torchvision, scikit-learn, NumPy, Pandas, OpenCV,
Pillow, Matplotlib, Seaborn, Streamlit, PyYAML, and pytest.

## Project layout

```text
configs/                 Experiment defaults for shared, CNN, and k-NN runs
data/                    Local datasets (not committed)
src/armscribe/           Importable application package
  data/                  Dataset, preprocessing, augmentation, and splitting interfaces
  models/                Base model, CNN, and k-NN interfaces
  training/              Training orchestration interface
  evaluation/            Metrics and error-analysis interfaces
  inference/             Prediction interface
  utils/                 Configuration and reproducibility helpers
demo/                    Streamlit skeleton
scripts/                 Future command-line entry points
tests/                   Offline infrastructure tests
checkpoints/, results/, reports/  Generated outputs (not committed)
```

## Installation on Windows

From PowerShell in the project directory:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process
Bypass` for the current terminal and retry the activation command.

## Development commands

Run the offline tests:

```powershell
pytest
```

Launch the current Streamlit placeholder:

```powershell
streamlit run demo/app.py
```

The future commands below are placeholders only; their workflows have not been
implemented in Phase 1:

```powershell
python scripts/prepare_data.py
python scripts/train_cnn.py
python scripts/train_knn.py
python scripts/evaluate.py
```

## Configuration

`configs/default.yaml` holds initial values intended for experimentation.
`cnn.yaml` and `knn.yaml` are small model-specific overrides. Paths are
relative to the project root. The eventual split must be writer-independent:
no writer may appear in both training and validation/test sets.

## Development phases

1. **Initialization (current):** package layout, contracts, configurations,
   documentation, and tests.
2. Dataset inspection, class mapping, preprocessing, and writer-aware splits.
3. CNN and k-NN implementations with reproducible training experiments.
4. Evaluation, error analysis, and unseen-writer testing.
5. Streamlit drawing/upload recognition interface.

See [DATASHEET.md](DATASHEET.md) for the data documentation template.
