# Figures folder

This folder contains the main manuscript figures and simplified reproduced figures.

## Manuscript-ready figures

- `Figure1_data_visibility_equity_surveillance.*`
- `Figure2_visible_exposure_inequalities.*`
- `Figure3_smoking_adjusted_residual_pm25_signal.*`
- `Figure4_measured_exposure_burden_surveillance_profiles.*`

PNG and PDF versions are provided.

## Reproduced figure checks

Running:

```bash
python scripts/generate_figures.py
```

creates simplified transparent checks in:

- `figures/reproduced/`

These reproduced figures are not intended to be exact layout duplicates of the final
manuscript-ready figures. They are provided to confirm that the shared data and result
tables reproduce the main patterns.
