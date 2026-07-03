# Scripts

## `generate_figures.py`

Portable public reproduction script.

Run from the repository root:

```bash
python scripts/generate_figures.py
```

The script:

1. loads the cleaned aggregate country-level dataset;
2. checks the core country overlap;
3. reproduces historical smoking model coefficients when `statsmodels` is installed, or
   reads the exported manuscript coefficient tables when it is not available;
4. reproduces clean-fuel deficit correlations;
5. checks PM2.5 residual model outputs;
6. writes simplified reproduced figures to `figures/reproduced/`;
7. writes reproduced numerical checks to `results/reproduced/`.

The script intentionally uses only relative paths and does not read manuscript drafts,
non-public working files, or local project directories.
