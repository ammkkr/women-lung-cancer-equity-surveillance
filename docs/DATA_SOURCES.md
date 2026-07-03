# Data sources and provenance

This repository uses public aggregate country-level indicators linked to, or compatible
with, the WHO Health Inequality Data Repository and related global health data systems.

## Main source domains

| Domain | Main source family | Use in analysis |
|---|---|---|
| Tobacco | WHO Global Health Observatory and HIDR-linked tobacco indicators | Female age-standardised current tobacco smoking prevalence in 2000, 2005, 2010, and 2022 |
| Clean fuels | WHO Global Health Observatory environmental health indicators | Total, urban, and rural clean-fuel access; clean-fuel deficit and urban-rural clean-fuel disadvantage |
| Ambient air pollution | WHO Global Health Observatory or compatible PM2.5 estimates | National annual mean PM2.5 concentration |
| Lung-cancer burden | WHO Global Health Estimates and IHME/GBD-linked estimates | Female lung-cancer mortality, YLL, DALY, and incidence |
| Development and structural covariates | World Bank, Global Data Lab, and compatible global indicators | GDP, HDI, SDI, urbanisation, and population aged 65 years or older |
| Visibility assessment | WHO HIDR-linked indicator inventory and compatible global data review | Classification of pathway components as visible, partially visible, largely absent, or absent |

## Source dictionary

The most detailed provenance file is:

- `data/source_indicator_dictionary.csv`

It records source file, dataset identifier, source institution, indicator name,
dimension, unit, country coverage, year coverage, latest year, disaggregation,
age-standardisation status, subgroup availability, modelled-estimate status, and notes.

## Important source-use notes

1. The repository contains cleaned aggregate indicators rather than raw source extracts.
2. The original source providers retain their own data-use terms.
3. Several indicators are modelled country-level estimates and should not be treated as
   direct measurements of individual exposure.
4. Second-hand smoke indicators were identified but were not included in the main models
   because the available country-level longitudinal coverage was not sufficient for the
   study design.
5. Clean-fuel deficit is a structural proxy for household energy poverty, not a direct
   measure of personal household air-pollution exposure.
6. PM2.5 is national ambient annual mean concentration, not personal exposure.

## Reproducible source checking

For review and reuse, start with:

- `data/source_indicator_dictionary.csv`
- `data/variable_dictionary.csv`
- `docs/CODEBOOK.md`
- `DATA_USE_NOTE.md`

These files are intended to make clear what each shared variable represents and what it
does not represent.
