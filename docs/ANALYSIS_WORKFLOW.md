# Analysis workflow

This repository is organised around the manuscript workflow rather than around raw data
extraction. The shared files allow readers to inspect the aggregate dataset, rerun key
checks, and review the figures and tables used in the manuscript.

## Stage 1. Indicator mapping

Indicators were mapped across:

- female tobacco smoking
- clean-fuel access and urban-rural clean-fuel gaps
- ambient PM2.5
- female lung-cancer burden
- structural covariates
- prevention-care pathway visibility

Outputs:

- `data/source_indicator_dictionary.csv`
- `data/data_visibility_matrix.csv`
- `supplementary/tables/Table_S01_indicator_dictionary_and_source_coverage.csv`
- `supplementary/tables/Table_S20_pathway_visibility_matrix.csv`

## Stage 2. Country-level master dataset

The master dataset retains one row per country and harmonises country identifiers,
exposure indicators, burden outcomes, and covariates.

Outputs:

- `data/country_level_analysis_dataset.csv`
- `data/variable_dictionary.csv`
- `supplementary/tables/Table_S02_variable_dictionary_and_derived_measures.csv`

## Stage 3. Missingness and coverage

The analysis quantifies variable coverage, complete-case overlap, missingness by WHO
region and income group, and included versus excluded country characteristics.

Outputs:

- `figures/Figure1_data_visibility_equity_surveillance.*`
- `supplementary/figures/Figure_S2_missingness_heatmap.*`
- `supplementary/figures/Figure_S3_missingness_by_region_and_income.*`
- `supplementary/tables/Table_S03_core_variable_country_coverage.csv`
- `supplementary/tables/Table_S04_missingness_by_who_region_and_income_group.csv`
- `supplementary/tables/Table_S05_included_versus_excluded_country_characteristics.csv`

## Stage 4. Descriptive exposure-side inequities

Visible exposure-side indicators are summarised by income group and WHO region. Clean-fuel
deficit is examined as a structural household energy equity indicator.

Outputs:

- `figures/Figure2_visible_exposure_inequalities.*`
- `results/clean_fuel_correlations.csv`
- `supplementary/figures/Figure_S4_clean_fuel_inequity_gradients.*`
- `supplementary/tables/Table_S06_descriptive_global_patterns_by_who_region_and_income_group.csv`
- `supplementary/tables/Table_S07_clean_fuel_inequity_gradients.csv`

## Stage 5. Historical smoking adjustment

Female lung-cancer burden models use historical female smoking, defined as the mean of
female smoking prevalence in 2000, 2005, and 2010, plus structural covariates. Residuals
are used as descriptive partially historical-smoking-adjusted burden residuals.

Outputs:

- `figures/Figure3_smoking_adjusted_residual_pm25_signal.*`
- `results/historical_smoking_model_coefficients.csv`
- `results/historical_smoking_model_fit.csv`
- `supplementary/figures/Figure_S5_historical_smoking_coefficients.*`
- `supplementary/tables/Table_S08_historical_smoking_model_coefficients.csv`
- `supplementary/tables/Table_S09_historical_smoking_model_fit_statistics.csv`

## Stage 6. Environmental heterogeneity and robustness

Residual models examine whether clean-fuel deficit and PM2.5 are associated with the
descriptive residual globally and whether associations differ by income or development
context.

Outputs:

- `results/pm25_robustness_results.csv`
- `supplementary/figures/Figure_S6_environmental_residual_models.*`
- `supplementary/figures/Figure_S7_pm25_heterogeneity_robustness.*`
- `supplementary/figures/Figure_S8_smoking_adjusted_burden_residual_scatter_diagnostics.*`
- `supplementary/figures/Figure_S9_outcome_uncertainty_proxy_residual_consistency.*`
- `supplementary/tables/Table_S10_environmental_residual_model_coefficients.csv`
- `supplementary/tables/Table_S11_outcome_replacement_and_mortality_incidence_residual_consistency.csv`

## Stage 7. Exploratory measured exposure-burden profiles

The measured exposure-side score combines current female smoking, clean-fuel deficit, and
ambient PM2.5 for descriptive surveillance profiling. It is not a validated risk score or
country ranking.

Outputs:

- `figures/Figure4_measured_exposure_burden_surveillance_profiles.*`
- `supplementary/figures/Figure_S10_current_exposure_typology_summary.*`
- `supplementary/figures/Figure_S11_typology_heatmap_standalone.*`
- `supplementary/figures/Figure_S12_multiple_exposure_score_sensitivity.*`
- `supplementary/figures/Figure_S13_illustrative_country_profiles.*`
- `supplementary/tables/Table_S12_exploratory_exposure_typology_results.csv`
- `supplementary/tables/Table_S13_multiple_exposure_score_validation_and_weighting_sensitivity.csv`
- `supplementary/tables/Table_S14_surveillance_profile_threshold_sensitivity.csv`

## Stage 8. Sensitivity analyses

Sensitivity analyses include alternative smoking windows, outcomes, exposure definitions,
thresholds, clustering, missingness handling, influence diagnostics, latency windows, and
model performance checks.

Outputs:

- `supplementary/figures/Figure_S14_sensitivity_summary.*`
- `supplementary/figures/Figure_S15_lagged_environmental_exposure_models.*`
- `supplementary/figures/Figure_S16_model_performance_comparison.*`
- `supplementary/figures/Figure_S17_measured_exposure_burden_profile_matrix.*`
- `supplementary/tables/Table_S15_smoking_window_sensitivity_analyses.csv`
- `supplementary/tables/Table_S16_exposure_replacement_sensitivity_analyses.csv`
- `supplementary/tables/Table_S17_missing_data_and_imputation_sensitivity_analyses.csv`
- `supplementary/tables/Table_S18_influence_diagnostics_and_robust_regression.csv`
- `supplementary/tables/Table_S19_stratified_and_interaction_models.csv`
