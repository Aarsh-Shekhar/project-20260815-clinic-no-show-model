# Clinic No Show Model

Estimates synthetic appointment no-show risk.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m clinic_no_show_model.cli --input data/sample_appointments.json
```

## Test

```bash
python3 -m unittest discover tests
```
