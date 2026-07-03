# Reproducibility guide

This guide explains how to reproduce the repository checks from the shared aggregate
dataset. The script is intentionally portable and uses only relative paths.

## 1. Install dependencies

From the repository root:

```bash
python -m pip install -r requirements.txt
```

The script can still run in a limited mode if `statsmodels` is unavailable, using the
exported manuscript result tables. Installing the full requirements is recommended for
model recomputation.

## 2. Run the public reproduction script

```bash
python scripts/generate_figures.py
```

The script reads:

- `data/country_level_analysis_dataset.csv`
- `data/data_visibility_matrix.csv`
- `results/historical_smoking_model_coefficients.csv`
- `results/historical_smoking_model_fit.csv`
- `results/pm25_robustness_results.csv`

It writes:

- `results/reproduced/reproduced_historical_smoking_models.csv`
- `results/reproduced/reproduced_pm25_residual_models.csv`
- `results/reproduced/reproduced_clean_fuel_correlations.csv`
- `figures/reproduced/Figure1_reproduced_data_visibility.*`
- `figures/reproduced/Figure2_reproduced_visible_exposure_inequalities.*`
- `figures/reproduced/Figure3_reproduced_smoking_adjusted_pm25_signal.*`
- `figures/reproduced/Figure4_reproduced_exposure_burden_profiles.*`

## 3. Expected key checks

Expected console outputs include:

- 197 countries loaded.
- Core overlap of 163 countries.
- Historical female smoking coefficient for female lung-cancer mortality near 0.181
  with 95% CI approximately 0.074 to 0.288.
- Strong clean-fuel deficit correlations with SDI, HDI, urbanisation, and rural
  clean-fuel disadvantage.
- Clearer PM2.5 residual signal in non-high-income robustness models than in the full
  global interpretation.

## 4. Manuscript figures versus reproduced figures

The final manuscript-ready figures are stored in:

- `figures/`

The reproduced figures are stored in:

- `figures/reproduced/`

The reproduced figures are simplified checks generated from public repository files. They
are not intended to exactly duplicate the final journal-layout figures.

## 5. Supplementary materials

Supplementary figure and table indexes are provided at:

- `supplementary/supplementary_figure_index.csv`
- `supplementary/supplementary_table_index.csv`

Supplementary tables are exported as CSV files to make them searchable and reusable
without requiring the supplementary Word document.
