# Women's lung-cancer equity surveillance

Reproducibility package for:

**Global indicator availability and exposure inequalities in women's lung-cancer prevention: a cross-national ecological study**

## Contents

- `data/country_level_analysis_dataset.csv`: cleaned aggregate country-level analytic data.
- `data/source_indicator_dictionary.csv`: indicator definitions and source metadata.
- `data/source_access_manifest.csv`: provider terms, access dates and repository treatment.
- `data/external/ne_110m_admin_0_countries.geojson`: map geometry used for display and spatial sensitivity analyses.
- `code/analysis_pipeline.py`: analysis, figure and document-generation script using relative paths.
- `results/`: numerical outputs supporting the manuscript and supplement.
- `figures/`: manuscript and supplementary PNG previews.
- `validation/`: separate SW and JZ audit records, item-level comparison and agreement summary.
- `manuscript/`: Markdown versions of the main manuscript and Additional file 1.

## Reproduction

From the repository root, run:

```bash
python -m pip install -r requirements.txt
python code/analysis_pipeline.py
```

The script writes a `results_generated/` directory. Python 3.12 and the packages listed in `requirements.txt` are required.

## Interpretation

The dataset is ecological, with one row per country or territory. Analyses describe indicator availability and country-level exposure inequalities. They do not support individual-level inference, causal attribution or national performance ranking.

## Data provenance

Source datasets are publicly available from WHO, IHME/GBD-linked outputs, the World Bank and Global Data Lab. No individual-level or identifiable data are included. The cleaned derivative is shared for transparent public-health research reproduction and is not relicensed independently of the original providers. See `DATA_PROVENANCE_AND_REUSE.md` and `data/source_access_manifest.csv` before reuse.

## Audit reproducibility

Shen Wang and Jing Zhou independently coded 18 pathway components across 10 dimensions. Their archived records agree in 180/180 cells (100%; Cohen's kappa 1.000), with no adjudication change required.
