# Codebook

The main analytic file is:

- `data/country_level_analysis_dataset.csv`

It contains one row per country and no individual-level records.

## Country identifiers and grouping variables

| Variable | Meaning |
|---|---|
| `iso3` | ISO3 country code |
| `country` | Country or territory name |
| `WHO_region` | WHO region |
| `income_group` | World Bank income group; unclassified countries are retained where applicable |

## Tobacco variables

| Variable | Meaning |
|---|---|
| `female_smoking_2000` | Female age-standardised current tobacco smoking prevalence in 2000 |
| `female_smoking_2005` | Female age-standardised current tobacco smoking prevalence in 2005 |
| `female_smoking_2010` | Female age-standardised current tobacco smoking prevalence in 2010 |
| `female_smoking_2022` | Female age-standardised current tobacco smoking prevalence in 2022 |
| `historical_female_smoking` | Mean of `female_smoking_2000`, `female_smoking_2005`, and `female_smoking_2010` |

`historical_female_smoking` is an available historical smoking proxy. It is not complete
lifetime tobacco exposure and does not capture smoking history before 2000.

## Clean-fuel and environmental variables

| Variable | Meaning |
|---|---|
| `clean_fuel_2020` | Population primarily relying on clean fuels and technologies for cooking in 2020 (%) |
| `clean_fuel_urban_2020` | Urban clean-fuel access in 2020 (%) |
| `clean_fuel_rural_2020` | Rural clean-fuel access in 2020 (%) |
| `clean_fuel_deficit` | `100 - clean_fuel_2020` |
| `rural_clean_fuel_disadvantage` | `clean_fuel_urban_2020 - clean_fuel_rural_2020` |
| `PM25_2019` | National annual mean ambient PM2.5 concentration in 2019 |

Clean-fuel deficit is a country-level household energy poverty proxy. PM2.5 is national
ambient concentration. Neither variable is an individual exposure history.

## Female lung-cancer burden outcomes

| Variable | Meaning |
|---|---|
| `female_LC_mort_2021` | Female trachea, bronchus, and lung cancer mortality rate in 2021 |
| `female_LC_YLL_2021` | Female lung-cancer years of life lost in 2021 |
| `female_LC_DALY_2021` | Female lung-cancer disability-adjusted life years in 2021 |
| `female_LC_incidence_2021` | Female lung-cancer incidence in 2021 |

## Structural covariates

| Variable | Meaning |
|---|---|
| `GDP` | GDP per capita or compatible development covariate used in adjusted models |
| `HDI` | Human Development Index |
| `SDI` | Socio-demographic Index |
| `urbanisation` | Percentage of population living in urban areas |
| `age65` | Percentage of population aged 65 years or older |

## Analysis flags and derived outputs

| Variable | Meaning |
|---|---|
| `analysis_core_complete` | Country has complete data for the core exposure and burden variables |
| `analysis_core_plus_covariates_complete` | Country has complete core and structural covariate data |
| `smoking_adjusted_burden_residual_mortality` | Residual from the mortality model adjusted for available historical smoking proxy and structural covariates |
| `smoking_adjusted_burden_residual_YLL` | Corresponding residual for YLL |
| `smoking_adjusted_burden_residual_DALY` | Corresponding residual for DALY |
| `multiple_exposure_score_equal_weighted` | Equal-weighted measured exposure-side score based on current female smoking, clean-fuel deficit, and ambient PM2.5 |

Residuals are descriptive country-level quantities. They should not be interpreted as
non-smoking lung-cancer burden, causal environmental effects, or unexplained biological
susceptibility.

## Full variable dictionary

For non-missing counts and exact definitions, see:

- `data/variable_dictionary.csv`
- `supplementary/tables/Table_S02_variable_dictionary_and_derived_measures.csv`
