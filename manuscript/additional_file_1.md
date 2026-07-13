# Additional file 1

## Supplementary methods

### Scope and source identification
The supplement documents the structured source audit and all analyses supporting the main manuscript. Formal coding used WHO HIDR/HEAT-linked sources, GHO, GHE, GBD-linked outputs, World Bank indicators and Global Data Lab HDI. Targeted verification covered IARC/GLOBOCAN, CanScreen5, CONCORD, WHO second-hand-smoke metadata and GTSS/GATS. Shen Wang and Jing Zhou independently coded all 180 component-by-dimension cells. Their coder-specific records were archived after completion, compared without alteration and showed 100% agreement (Cohen's kappa=1.000); no adjudication change was required. Two AI-assisted read-only passes reproduced the final classifications as secondary quality control and were excluded from the human agreement statistic. The workflow and decision rules are shown in Supplementary Figure S1 and Supplementary Tables S1-S3.

### Missingness and descriptive analyses
The primary frame required current female smoking, clean-fuel access, ambient PM2.5 and age-standardised female lung-cancer incidence. Missingness patterns were mutually exclusive. Coverage percentages used countries in each income or WHO-region stratum as denominators. Country-level values were not population weighted. Full country membership, coverage and distributions appear in Supplementary Tables S4-S6 and Supplementary Figures S2-S4.

### Inequality effect sizes
For each exposure, the prespecified low-income versus high-income contrast was expressed as a difference between group medians in the epidemiologically interpretable direction. Confidence intervals used 5000 within-group bootstrap resamples. Cliff's delta compared low-income with high-income country values and used the same resampling procedure. Estimates are reported in Supplementary Table S7.

### Age-standardised incidence models
The validation model used z-scored 2021 age-standardised female lung-cancer incidence. Historical smoking was the mean female age-standardised current tobacco prevalence in 2000, 2005 and 2010. The primary model adjusted for z-scored log GDP, z-scored urbanisation and WHO region, with HC3 standard errors. Model diagnostics, alternative windows, age-structure adjustment, Cook-distance exclusion, population restriction, Moran's I and Conley-type spatial covariance are reported in Supplementary Figures S5 and S7 and Supplementary Tables S8-S10.

### Exploratory environmental and outcome checks
The incidence residual from the primary smoking model was regressed on z-scored clean-fuel deficit and PM2.5 globally and in non-high-income settings, with region and interaction sensitivity analyses. Analogous incidence and WHO mortality residuals were compared as a source-consistency check. These analyses are supplementary because environmental histories were short and the mortality label did not explicitly state age standardisation (Supplementary Figures S6 and S8; Supplementary Tables S11-S12).

## Supplementary results

### Coverage and audit results
Most excluded countries were missing female smoking, and complete-frame inclusion was lowest in low-income and income-unclassified settings (Supplementary Figure S2; Supplementary Tables S4-S5). Human coder agreement was 180/180 cells (100%; Cohen's kappa=1.000), and all final codes matched both secondary AI-assisted quality-control passes (Supplementary Figure S1; Supplementary Table S3). The audit retained three adequate exposure indicators but classified second-hand smoke, occupational carcinogens and radon as limited. Screening, stage and treatment sources were located but not sufficiently integrated; survival and subtype were available with limitations (Supplementary Figure S3; Supplementary Table S3).

### Exposure inequalities
Country distributions varied substantially across income groups and WHO regions (Supplementary Figure S4; Supplementary Table S6). Bootstrap intervals and Cliff's delta confirmed opposing gradients for female smoking and household-energy deprivation, while ambient PM2.5 displayed a less monotonic intermediate pattern (Supplementary Table S7).

### Model and estimate-quality results
The historical-smoking coefficient remained positive across exposure windows, additional age-structure adjustment, Cook-distance exclusion, population restriction and Conley-type uncertainty estimates (Supplementary Tables S8-S10). Residual spatial autocorrelation remained detectable (Supplementary Figure S7). The non-high-income PM2.5 coefficient was positive before WHO-region adjustment but its interval included zero after regional adjustment (Supplementary Figure S6; Supplementary Table S11). Incidence and mortality residuals were strongly correlated, although this check does not remove source-method differences (Supplementary Figure S8; Supplementary Table S12).

## Supplementary figure legends

Supplementary Figure S1. Source-identification and indicator-audit workflow. Shen Wang and Jing Zhou independently coded the predefined audit cells; human agreement was quantified before finalisation. Two AI-assisted read-only checks were used only as secondary quality control and were excluded from Cohen's kappa. The workflow distinguishes formal source-frame coding from targeted verification of relevant cancer, screening, survival and tobacco resources.

Supplementary Figure S2. Coverage by income group and WHO region. Cells report the percentage of countries or territories with each primary indicator and the complete four-indicator overlap.

Supplementary Figure S3. Overall audit classifications by domain. Stacked bars summarise the adjudicated overall classification of components shown individually in Figure 2 and Supplementary Table S3.

Supplementary Figure S4. Exposure and age-standardised incidence distributions by WHO region. Boxes show medians and interquartile ranges, whiskers extend to 1.5 times the interquartile range, and points represent countries or territories.

Supplementary Figure S5. Incidence-model diagnostics. Panels show residuals versus fitted values, a normal quantile plot, leverage versus residuals and the 12 largest Cook's distances. The dashed Cook threshold is 4/n.

Supplementary Figure S6. Exploratory PM2.5 heterogeneity. Coefficients and HC3 95% confidence intervals are shown for global, non-high-income, WHO-region-adjusted and interaction analyses of the age-standardised incidence residual. Interaction estimates refer to PM2.5 by high-income status and are not directly comparable with the PM2.5 main-effect rows.

Supplementary Figure S7. Spatial residual diagnostics. The Moran scatter plot and geographic residual display use countries matched to Natural Earth centroids. Moran's I used a symmetrised six-nearest-neighbour matrix and 999 permutations.

Supplementary Figure S8. Incidence-mortality residual consistency. Residuals were derived from analogous historical-smoking models adjusted for log GDP, urbanisation and WHO region. The mortality outcome was retained only for supplementary triangulation because age standardisation was not explicit in its downloaded label.

## Supplementary tables

### Supplementary Table S1. Audit classifications and operational criteria
| Classification | Operational rule | Interpretation |
| --- | --- | --- |
| Adequate for this analysis | Generally at least 80% country coverage, comparable definition and unit, machine-readable, and the required female/sex dimension | Usable in the primary analytic frame for its stated purpose |
| Available with limitations | Lower coverage or an important limitation in subgroup, time, uncertainty, comparability or standardisation | Usable only for restricted description, context or sensitivity analysis |
| Source located but not sufficiently harmonised/integrated | A relevant global or multi-country source was verified but could not be integrated into the prespecified frame | Do not describe the component as absent; identify the integration limitation |
| No compatible global indicator identified | No source meeting the country-level compatibility requirements was identified in the predefined search | A source-frame result, not proof that no local data exist |
| Not applicable | The audit dimension is not conceptually applicable to the component | Excluded from adequacy interpretation for that cell |

*Notes:* Thresholds were prespecified for this analysis and describe suitability for the stated analytic role.

### Supplementary Table S2. Source-identification protocol and targeted verification
| source | role | entry_points | search_dates | decision_rule |
| --- | --- | --- | --- | --- |
| WHO HIDR and HEAT | Formal audit frame | WHO inequality repository, downloaded indicator files and metadata | 2026-05-01 to 2026-07-13 | Country-level indicator or disaggregation relevant to the prespecified pathway |
| WHO Global Health Observatory | Formal audit frame | Indicator catalogue, metadata pages and machine-readable downloads | 2026-05-01 to 2026-07-13 | Harmonised definition, country identifier, year and usable value |
| WHO Global Health Estimates | Formal audit frame | Sex-specific lung-cancer mortality, YLL and DALY files and metadata | 2026-05-01 to 2026-07-13 | Used for coverage and triangulation; explicit standardisation required for primary burden modelling |
| IHME/GBD-linked outputs | Formal for used variables; targeted verification for other risks | Public incidence, SDI, risk and methods outputs | 2026-05-01 to 2026-07-13 | Integrated only when country-level definitions and identifiers were compatible |
| IARC/GLOBOCAN | Targeted verification | Global Cancer Observatory, subtype reports and registry documentation | 2026-06-01 to 2026-07-13 | Used to distinguish located sources from absence within the source frame |
| CanScreen5 | Targeted verification | IARC global screening repository, methods and programme documentation | 2026-07-13 | Classified as located but not integrated when lung-screening coverage was incomplete |
| CONCORD | Targeted verification | CONCORD-3 survival publication and explorer documentation | 2026-07-13 | Classified as limited when comparable estimates covered a subset of countries |
| World Bank and Global Data Lab | Compatible structural sources | World Development Indicators and HDI outputs | 2026-05-01 to 2026-07-13 | Country-year linkage and harmonised structural definition |
| GTSS/GATS and WHO second-hand smoke metadata | Targeted verification | Global tobacco surveillance and WHO indicator metadata | 2026-07-13 | Recorded as limited because instruments and observation years varied |

*Notes:* Searches were structured but did not constitute a systematic review of every national data source.

### Supplementary Table S3. Item-level indicator-availability audit and independent-coder agreement
| domain | component | audit_dimension | Shen_Wang_code | Jing_Zhou_code | exact_agreement | final_code | final_label | adjudication_change_required | evidence_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Exposure | Female smoking | Coverage | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Female/sex | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Residence | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Socioeconomic | limited | limited | True | limited | Available with limitations | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Time series | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Machine-readable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Uncertainty | limited | limited | True | limited | Available with limitations | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Age standard | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Female smoking | Overall | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO modelled age-standardised female estimates; socioeconomic survey disaggregation is not globally contemporaneous. |
| Exposure | Clean-fuel access | Coverage | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Female/sex | na | na | True | na | Not applicable | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Residence | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Socioeconomic | limited | limited | True | limited | Available with limitations | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Time series | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Machine-readable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Uncertainty | limited | limited | True | limited | Available with limitations | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Age standard | na | na | True | na | Not applicable | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Clean-fuel access | Overall | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO total, urban and rural estimates; wealth-disaggregated DHS coverage is partial. |
| Exposure | Ambient PM2.5 | Coverage | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Female/sex | na | na | True | na | Not applicable | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Residence | limited | limited | True | limited | Available with limitations | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Time series | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Machine-readable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Uncertainty | limited | limited | True | limited | Available with limitations | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Age standard | na | na | True | na | Not applicable | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Ambient PM2.5 | Overall | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHO national modelled concentration; not personal exposure. |
| Exposure | Second-hand smoke | Coverage | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Female/sex | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Residence | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Socioeconomic | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Time series | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Comparable | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Machine-readable | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Uncertainty | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Age standard | na | na | True | na | Not applicable | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Second-hand smoke | Overall | limited | limited | True | limited | Available with limitations | No | WHO GHO and GTSS/GATS indicators exist, but survey definitions and years vary and complete female country-year coverage was not available in the analytic frame. |
| Exposure | Occupational carcinogens | Coverage | limited | limited | True | limited | Available with limitations | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Female/sex | limited | limited | True | limited | Available with limitations | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Time series | limited | limited | True | limited | Available with limitations | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Comparable | limited | limited | True | limited | Available with limitations | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Machine-readable | limited | limited | True | limited | Available with limitations | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Uncertainty | limited | limited | True | limited | Available with limitations | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Age standard | na | na | True | na | Not applicable | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Occupational carcinogens | Overall | limited | limited | True | limited | Available with limitations | No | GBD attributable-risk estimates are available; harmonised female exposure prevalence by occupation and socioeconomic group was not integrated. |
| Exposure | Residential radon | Coverage | limited | limited | True | limited | Available with limitations | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Female/sex | na | na | True | na | Not applicable | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Time series | limited | limited | True | limited | Available with limitations | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Comparable | limited | limited | True | limited | Available with limitations | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Machine-readable | limited | limited | True | limited | Available with limitations | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Uncertainty | adequate | adequate | True | adequate | Adequate for this analysis | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Age standard | na | na | True | na | Not applicable | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Exposure | Residential radon | Overall | limited | limited | True | limited | Available with limitations | No | GBD 2021 reports exposure and attributable burden with uncertainty, but radon was not present as a compatible HIDR-linked female exposure indicator. |
| Burden | Age-standardised incidence | Coverage | adequate | adequate | True | adequate | Adequate for this analysis | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Female/sex | adequate | adequate | True | adequate | Adequate for this analysis | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Time series | adequate | adequate | True | adequate | Adequate for this analysis | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Machine-readable | adequate | adequate | True | adequate | Adequate for this analysis | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Uncertainty | limited | limited | True | limited | Available with limitations | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Age standard | adequate | adequate | True | adequate | Adequate for this analysis | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Age-standardised incidence | Overall | adequate | adequate | True | adequate | Adequate for this analysis | No | IHME/GBD-linked age-standardised female incidence estimates. |
| Burden | Mortality | Coverage | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Female/sex | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Time series | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Machine-readable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Uncertainty | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Age standard | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | Mortality | Overall | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Coverage | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Female/sex | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Time series | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Machine-readable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Uncertainty | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Age standard | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | YLL | Overall | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Coverage | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Female/sex | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Time series | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Machine-readable | adequate | adequate | True | adequate | Adequate for this analysis | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Uncertainty | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Age standard | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Burden | DALY | Overall | limited | limited | True | limited | Available with limitations | No | WHO GHE/HIDR sex-specific rates; age-standardisation was not explicit in the downloaded label. |
| Care pathway | LDCT programme and uptake | Coverage | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Female/sex | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Time series | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Comparable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Machine-readable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Uncertainty | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Age standard | na | na | True | na | Not applicable | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | LDCT programme and uptake | Overall | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | CanScreen5 and national programme sources were located, but lung-screening indicators were not sufficiently complete and harmonised for the analytic frame. |
| Care pathway | Stage at diagnosis | Coverage | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Female/sex | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Time series | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Comparable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Machine-readable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Uncertainty | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Age standard | na | na | True | na | Not applicable | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Stage at diagnosis | Overall | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Registry sources exist, but no globally integrated female country-level stage indicator compatible with the frame was identified. |
| Care pathway | Histology or subtype | Coverage | limited | limited | True | limited | Available with limitations | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Female/sex | adequate | adequate | True | adequate | Adequate for this analysis | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Time series | limited | limited | True | limited | Available with limitations | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Machine-readable | limited | limited | True | limited | Available with limitations | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Uncertainty | limited | limited | True | limited | Available with limitations | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Age standard | na | na | True | na | Not applicable | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Histology or subtype | Overall | limited | limited | True | limited | Available with limitations | No | IARC has comparable global subtype estimates, but this is not a complete longitudinal care-pathway indicator. |
| Care pathway | Treatment access | Coverage | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Female/sex | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Time series | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Comparable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Machine-readable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Uncertainty | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Age standard | na | na | True | na | Not applicable | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Treatment access | Overall | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Programme and registry sources contain treatment elements, but no globally integrated women-specific treatment-access series was identified. |
| Care pathway | Survival | Coverage | limited | limited | True | limited | Available with limitations | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Female/sex | adequate | adequate | True | adequate | Adequate for this analysis | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Time series | limited | limited | True | limited | Available with limitations | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Comparable | adequate | adequate | True | adequate | Adequate for this analysis | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Machine-readable | limited | limited | True | limited | Available with limitations | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Uncertainty | limited | limited | True | limited | Available with limitations | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Age standard | limited | limited | True | limited | Available with limitations | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Care pathway | Survival | Overall | limited | limited | True | limited | Available with limitations | No | CONCORD-3 provides age-standardised survival from 322 registries in 71 countries, but global coverage and socioeconomic linkage are limited. |
| Equity outcomes | Wealth-stratified LC outcomes | Coverage | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Female/sex | limited | limited | True | limited | Available with limitations | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Time series | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Comparable | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Machine-readable | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Uncertainty | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Age standard | limited | limited | True | limited | Available with limitations | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Wealth-stratified LC outcomes | Overall | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by wealth was identified. |
| Equity outcomes | Education-stratified LC outcomes | Coverage | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Female/sex | limited | limited | True | limited | Available with limitations | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Residence | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Time series | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Comparable | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Machine-readable | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Uncertainty | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Age standard | limited | limited | True | limited | Available with limitations | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Education-stratified LC outcomes | Overall | no_global | no_global | True | no_global | No compatible global indicator identified | No | No compatible global female lung-cancer outcome series stratified by education was identified. |
| Equity outcomes | Residence-stratified LC outcomes | Coverage | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Female/sex | limited | limited | True | limited | Available with limitations | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Residence | limited | limited | True | limited | Available with limitations | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Socioeconomic | no_global | no_global | True | no_global | No compatible global indicator identified | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Time series | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Comparable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Machine-readable | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Uncertainty | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Age standard | limited | limited | True | limited | Available with limitations | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |
| Equity outcomes | Residence-stratified LC outcomes | Overall | located | located | True | located | Source located; not sufficiently harmonised/integrated | No | Subnational registry outputs exist, but were not sufficiently harmonised and integrated across countries. |

*Notes:* Shen Wang and Jing Zhou independently coded 18 components across 10 dimensions. Agreement was 180/180 cells (100%) and Cohen's kappa was 1.000. Coder-specific records were archived on 13 July 2026 after completion; no adjudication change was required. Two AI-assisted read-only checks reproduced the final codes but were excluded from the human inter-rater statistic.

### Supplementary Table S4. Country and territory analytic-frame membership
| iso3 | country | WHO_region | income_group | complete_analytic_indicator_frame | incidence_model_complete | analytic_missingness_pattern | female_smoking_2022 | clean_fuel_2020 | PM25_2019 | female_LC_incidence_2021 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFG | Afghanistan | Eastern Mediterranean | Low-income | True | True | Complete four-indicator frame | 2.000 | 34.600 | 62.486 | 7.034 |
| AGO | Angola | African | Lower-middle-income | False | False | Missing female smoking only |  | 49.400 | 27.165 | 5.130 |
| ALB | Albania | European | Upper-middle-income | True | True | Complete four-indicator frame | 6.000 | 83.400 | 16.280 | 11.390 |
| AND | Andorra | European | High-income | True | True | Complete four-indicator frame | 37.900 | 100.000 | 8.524 | 6.566 |
| ARE | United Arab Emirates | Eastern Mediterranean | High-income | True | True | Complete four-indicator frame | 2.600 | 100.000 | 41.749 | 19.884 |
| ARG | Argentina | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 19.100 | 99.900 | 12.041 | 12.811 |
| ARM | Armenia | European | Upper-middle-income | True | True | Complete four-indicator frame | 1.500 | 98.500 | 34.127 | 8.274 |
| ATG | Antigua and Barbuda | Americas | High-income | False | False | Missing female smoking only |  | 100.000 | 8.297 | 5.771 |
| AUS | Australia | Western Pacific | High-income | True | True | Complete four-indicator frame | 10.900 | 100.000 | 8.933 | 24.255 |
| AUT | Austria | European | High-income | True | True | Complete four-indicator frame | 24.000 | 100.000 | 11.508 | 23.020 |
| AZE | Azerbaijan | European | Upper-middle-income | True | True | Complete four-indicator frame | 0.100 | 98.400 | 24.643 | 5.762 |
| BDI | Burundi | African | Low-income | True | True | Complete four-indicator frame | 1.800 | 0.100 | 27.996 | 2.564 |
| BEL | Belgium | European | High-income | True | True | Complete four-indicator frame | 22.000 | 100.000 | 11.256 | 22.707 |
| BEN | Benin | African | Lower-middle-income | True | True | Complete four-indicator frame | 1.200 | 5.700 | 31.515 | 2.947 |
| BFA | Burkina Faso | African | Low-income | True | True | Complete four-indicator frame | 2.500 | 13.500 | 40.745 | 2.549 |
| BGD | Bangladesh | South-East Asia | Lower-middle-income | True | True | Complete four-indicator frame | 0.500 | 24.600 | 45.989 | 2.983 |
| BGR | Bulgaria | European | High-income | False | True | Missing clean-fuel access only | 38.700 |  | 17.290 | 15.644 |
| BHR | Bahrain | Eastern Mediterranean | High-income | True | True | Complete four-indicator frame | 5.100 | 100.000 | 51.817 | 11.856 |
| BHS | Bahamas | Americas | High-income | True | True | Complete four-indicator frame | 2.100 | 100.000 | 5.199 | 7.756 |
| BIH | Bosnia and Herzegovina | European | Upper-middle-income | True | True | Complete four-indicator frame | 30.900 | 40.200 | 26.194 | 16.441 |
| BLR | Belarus | European | Upper-middle-income | True | True | Complete four-indicator frame | 11.300 | 99.700 | 15.482 | 5.530 |
| BLZ | Belize | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 1.900 | 83.200 | 10.509 | 6.685 |
| BOL | Bolivia (Plurinational State of) | Americas | Lower-middle-income | True | True | Complete four-indicator frame | 4.200 | 87.500 | 25.234 | 10.487 |
| BRA | Brazil | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 8.900 | 96.450 | 10.940 | 11.328 |
| BRB | Barbados | Americas | High-income | True | True | Complete four-indicator frame | 1.700 | 100.000 | 9.790 | 5.936 |
| BRN | Brunei Darussalam | Western Pacific | High-income | True | True | Complete four-indicator frame | 2.200 | 100.000 | 6.865 | 22.949 |
| BTN | Bhutan | South-East Asia | Lower-middle-income | True | True | Complete four-indicator frame | 2.600 | 88.300 | 26.095 | 3.565 |
| BWA | Botswana | African | Upper-middle-income | True | True | Complete four-indicator frame | 3.500 | 65.100 | 12.818 | 8.137 |
| CAF | Central African Republic | African | Low-income | False | False | Missing female smoking only |  | 0.800 | 27.198 | 3.656 |
| CAN | Canada | Americas | High-income | True | True | Complete four-indicator frame | 9.700 | 100.000 | 6.389 | 33.999 |
| CHE | Switzerland | European | High-income | True | True | Complete four-indicator frame | 22.900 | 100.000 | 8.967 | 22.044 |
| CHL | Chile | Americas | High-income | True | True | Complete four-indicator frame | 26.700 | 100.000 | 20.486 | 11.291 |
| CHN | China | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 1.600 | 83.800 | 38.153 | 28.163 |
| CIV | Côte d'Ivoire | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.500 | 36.900 | 40.415 | 2.163 |
| CMR | Cameroon | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.300 | 27.400 | 56.367 | 3.970 |
| COD | Democratic Republic of the Congo | African | Low-income | True | True | Complete four-indicator frame | 0.600 | 4.400 | 31.579 | 3.854 |
| COG | Congo | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.900 | 35.400 | 29.484 | 7.512 |
| COK | Cook Islands | Western Pacific | Unclassified | True | False | Complete four-indicator frame | 22.200 | 76.100 | 7.801 | 10.953 |
| COL | Colombia | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 4.400 | 90.900 | 14.036 | 8.339 |
| COM | Comoros | African | Lower-middle-income | True | True | Complete four-indicator frame | 2.100 | 8.300 | 14.372 | 4.387 |
| CPV | Cabo Verde | African | Upper-middle-income | True | True | Complete four-indicator frame | 2.700 | 81.000 | 31.081 | 9.178 |
| CRI | Costa Rica | Americas | High-income | True | True | Complete four-indicator frame | 4.500 | 95.900 | 14.695 | 5.466 |
| CUB | Cuba | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 9.500 | 94.700 | 13.320 | 22.554 |
| CYP | Cyprus | European | High-income | True | True | Complete four-indicator frame | 23.900 | 100.000 | 14.516 | 10.365 |
| CZE | Czechia | European | High-income | True | True | Complete four-indicator frame | 26.500 | 100.000 | 14.341 | 20.534 |
| DEU | Germany | European | High-income | True | True | Complete four-indicator frame | 19.300 | 100.000 | 10.731 | 25.004 |
| DJI | Djibouti | Eastern Mediterranean | Lower-middle-income | False | False | Missing female smoking only |  | 9.700 | 19.985 | 4.905 |
| DMA | Dominica | Americas | Upper-middle-income | False | False | Missing female smoking only |  | 87.700 | 8.222 | 9.946 |
| DNK | Denmark | European | High-income | True | True | Complete four-indicator frame | 16.100 | 100.000 | 9.657 | 37.914 |
| DOM | Dominican Republic | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 5.800 | 92.300 | 7.585 | 9.200 |
| DZA | Algeria | African | Upper-middle-income | True | True | Complete four-indicator frame | 0.600 | 99.700 | 22.683 | 2.463 |
| ECU | Ecuador | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 2.600 | 94.600 | 16.549 | 6.521 |
| EGY | Egypt | Eastern Mediterranean | Lower-middle-income | True | True | Complete four-indicator frame | 0.400 | 99.900 | 63.157 | 7.724 |
| ERI | Eritrea | African | Low-income | False | False | Missing female smoking only |  | 11.700 | 22.745 | 4.528 |
| ESP | Spain | European | High-income | True | True | Complete four-indicator frame | 27.500 | 100.000 | 9.342 | 13.318 |
| EST | Estonia | European | High-income | True | True | Complete four-indicator frame | 21.500 | 100.000 | 6.350 | 10.082 |
| ETH | Ethiopia | African | Unclassified | True | True | Complete four-indicator frame | 0.900 | 6.200 | 21.805 | 2.582 |
| FIN | Finland | European | High-income | True | True | Complete four-indicator frame | 15.900 | 100.000 | 5.467 | 17.840 |
| FJI | Fiji | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 13.200 | 49.500 | 7.361 | 6.283 |
| FRA | France | European | High-income | True | True | Complete four-indicator frame | 33.700 | 100.000 | 10.457 | 22.368 |
| FSM | Micronesia (Federated States of) | Western Pacific | Lower-middle-income | False | False | Missing female smoking only |  | 13.300 | 7.786 | 16.226 |
| GAB | Gabon | African | Upper-middle-income | False | False | Missing female smoking only |  | 90.000 | 26.286 | 7.559 |
| GBR | The United Kingdom | European | High-income | True | True | Complete four-indicator frame | 12.400 | 100.000 | 9.516 | 31.531 |
| GEO | Georgia | European | Upper-middle-income | True | True | Complete four-indicator frame | 7.600 | 89.600 | 19.064 | 6.193 |
| GHA | Ghana | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.300 | 28.300 | 46.043 | 2.039 |
| GIN | Guinea | African | Lower-middle-income | False | False | Missing female smoking only |  | 1.000 | 37.574 | 2.844 |
| GMB | Gambia | African | Low-income | True | True | Complete four-indicator frame | 0.500 | 1.700 | 39.104 | 1.313 |
| GNB | Guinea-Bissau | African | Low-income | True | True | Complete four-indicator frame | 0.500 | 1.000 | 34.850 | 3.960 |
| GNQ | Equatorial Guinea | African | Upper-middle-income | False | False | Missing female smoking only |  | 23.000 | 25.669 | 8.078 |
| GRC | Greece | European | High-income | True | True | Complete four-indicator frame | 30.600 | 100.000 | 14.623 | 18.155 |
| GRD | Grenada | Americas | Upper-middle-income | False | False | Missing female smoking only |  | 87.200 | 10.084 | 6.956 |
| GTM | Guatemala | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 1.700 | 43.700 | 20.748 | 5.021 |
| GUY | Guyana | Americas | High-income | True | True | Complete four-indicator frame | 2.200 | 100.000 | 11.106 | 5.324 |
| HND | Honduras | Americas | Lower-middle-income | True | True | Complete four-indicator frame | 1.700 | 48.900 | 18.931 | 17.853 |
| HRV | Croatia | European | High-income | True | True | Complete four-indicator frame | 37.300 | 100.000 | 15.288 | 22.834 |
| HTI | Haiti | Americas | Lower-middle-income | True | True | Complete four-indicator frame | 2.500 | 4.200 | 9.691 | 6.377 |
| HUN | Hungary | European | High-income | True | True | Complete four-indicator frame | 28.100 | 100.000 | 14.245 | 33.486 |
| IDN | Indonesia | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 2.100 | 84.600 | 19.340 | 12.785 |
| IND | India | South-East Asia | Lower-middle-income | True | True | Complete four-indicator frame | 1.200 | 66.500 | 50.174 | 3.608 |
| IRL | Ireland | European | High-income | True | True | Complete four-indicator frame | 17.000 | 100.000 | 8.195 | 26.661 |
| IRN | Iran (Islamic Republic of) | Eastern Mediterranean | Upper-middle-income | True | True | Complete four-indicator frame | 1.100 | 96.400 | 31.616 | 6.137 |
| IRQ | Iraq | Eastern Mediterranean | Upper-middle-income | True | True | Complete four-indicator frame | 1.700 | 99.300 | 39.289 | 8.784 |
| ISL | Iceland | European | High-income | True | True | Complete four-indicator frame | 9.400 | 100.000 | 5.789 | 39.520 |
| ISR | Israel | European | High-income | True | True | Complete four-indicator frame | 13.800 | 100.000 | 19.471 | 12.933 |
| ITA | Italy | European | High-income | True | True | Complete four-indicator frame | 19.100 | 100.000 | 14.225 | 17.409 |
| JAM | Jamaica | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 3.500 | 92.400 | 14.831 | 8.013 |
| JOR | Jordan | Eastern Mediterranean | Lower-middle-income | True | True | Complete four-indicator frame | 13.600 | 99.700 | 25.872 | 4.675 |
| JPN | Japan | Western Pacific | High-income | True | True | Complete four-indicator frame | 9.600 | 100.000 | 10.835 | 15.284 |
| KAZ | Kazakhstan | European | Upper-middle-income | True | True | Complete four-indicator frame | 6.400 | 94.200 | 26.502 | 5.362 |
| KEN | Kenya | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.800 | 23.050 | 12.524 | 2.395 |
| KGZ | Kyrgyzstan | European | Lower-middle-income | True | True | Complete four-indicator frame | 3.200 | 78.600 | 37.585 | 4.739 |
| KHM | Cambodia | Western Pacific | Lower-middle-income | True | True | Complete four-indicator frame | 1.600 | 40.600 | 17.803 | 11.254 |
| KIR | Kiribati | Western Pacific | Lower-middle-income | True | True | Complete four-indicator frame | 26.800 | 11.900 | 7.618 | 6.326 |
| KNA | Saint Kitts and Nevis | Americas | High-income | False | False | Missing female smoking only |  | 100.000 | 8.051 | 6.150 |
| KOR | Republic of Korea | Western Pacific | High-income | True | True | Complete four-indicator frame | 5.800 | 100.000 | 24.038 | 16.708 |
| KWT | Kuwait | Eastern Mediterranean | High-income | True | True | Complete four-indicator frame | 2.100 | 100.000 | 64.077 | 3.158 |
| LAO | Lao People's Democratic Republic | Western Pacific | Lower-middle-income | True | True | Complete four-indicator frame | 4.700 | 8.800 | 21.155 | 10.879 |
| LBN | Lebanon | Eastern Mediterranean | Lower-middle-income | False | True | Missing clean-fuel access only | 25.700 |  | 24.234 | 12.161 |
| LBR | Liberia | African | Low-income | True | True | Complete four-indicator frame | 1.300 | 0.600 | 35.796 | 2.890 |
| LBY | Libya | Eastern Mediterranean | Upper-middle-income | False | False | Missing smoking and clean fuel |  |  | 29.836 | 5.524 |
| LCA | Saint Lucia | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 3.000 | 93.500 | 8.977 | 6.747 |
| LKA | Sri Lanka | South-East Asia | Lower-middle-income | True | True | Complete four-indicator frame | 0.200 | 32.100 | 23.878 | 4.277 |
| LSO | Lesotho | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.400 | 48.100 | 17.598 | 8.563 |
| LTU | Lithuania | European | High-income | True | True | Complete four-indicator frame | 19.700 | 100.000 | 10.369 | 9.074 |
| LUX | Luxembourg | European | High-income | True | True | Complete four-indicator frame | 21.600 | 100.000 | 8.895 | 20.313 |
| LVA | Latvia | European | High-income | True | True | Complete four-indicator frame | 19.500 | 100.000 | 12.022 | 9.361 |
| MAR | Morocco | Eastern Mediterranean | Lower-middle-income | True | True | Complete four-indicator frame | 1.000 | 98.200 | 13.440 | 2.032 |
| MCO | Monaco | European | High-income | False | False | Missing female smoking only |  | 100.000 | 9.211 | 56.167 |
| MDA | Republic of Moldova | European | Upper-middle-income | True | True | Complete four-indicator frame | 6.700 | 97.900 | 12.365 | 6.455 |
| MDG | Madagascar | African | Low-income | True | True | Complete four-indicator frame | 1.300 | 1.300 | 16.023 | 3.296 |
| MDV | Maldives | South-East Asia | Upper-middle-income | True | True | Complete four-indicator frame | 3.800 | 99.600 | 13.003 | 4.546 |
| MEX | Mexico | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 6.900 | 85.000 | 17.828 | 5.294 |
| MHL | Marshall Islands | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 4.000 | 65.200 | 7.215 | 14.148 |
| MKD | North Macedonia | European | Upper-middle-income | False | False | Missing female smoking only |  | 78.900 | 25.168 | 13.131 |
| MLI | Mali | African | Low-income | True | True | Complete four-indicator frame | 0.700 | 1.200 | 38.549 | 3.096 |
| MLT | Malta | European | High-income | True | True | Complete four-indicator frame | 23.200 | 100.000 | 12.930 | 11.565 |
| MMR | Myanmar | South-East Asia | Lower-middle-income | True | True | Complete four-indicator frame | 3.100 | 40.100 | 27.165 | 11.078 |
| MNE | Montenegro | European | Upper-middle-income | True | True | Complete four-indicator frame | 33.200 | 61.500 | 19.296 | 24.616 |
| MNG | Mongolia | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 6.600 | 51.800 | 41.304 | 8.582 |
| MOZ | Mozambique | African | Low-income | False | False | Missing female smoking only |  | 6.100 | 16.448 | 3.763 |
| MRT | Mauritania | African | Lower-middle-income | True | True | Complete four-indicator frame | 1.400 | 47.500 | 41.985 | 4.591 |
| MUS | Mauritius | African | Upper-middle-income | True | True | Complete four-indicator frame | 3.000 | 99.000 | 10.482 | 5.549 |
| MWI | Malawi | African | Low-income | True | True | Complete four-indicator frame | 1.300 | 1.800 | 18.570 | 0.816 |
| MYS | Malaysia | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 0.500 | 87.550 | 21.522 | 10.119 |
| NAM | Namibia | African | Lower-middle-income | True | True | Complete four-indicator frame | 4.600 | 46.900 | 11.811 | 3.655 |
| NER | Niger | African | Low-income | True | True | Complete four-indicator frame | 0.600 | 3.800 | 50.150 | 1.918 |
| NGA | Nigeria | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.400 | 18.900 | 55.642 | 0.923 |
| NIC | Nicaragua | Americas | Lower-middle-income | False | False | Missing female smoking only |  | 56.800 | 16.002 | 3.913 |
| NIU | Niue | Western Pacific | Unclassified | False | False | Missing female smoking only |  | 98.400 | 6.742 | 16.808 |
| NLD | Netherlands (Kingdom of the) | European | High-income | True | True | Complete four-indicator frame | 19.000 | 100.000 | 10.742 | 32.643 |
| NOR | Norway | European | High-income | True | True | Complete four-indicator frame | 13.500 | 100.000 | 6.301 | 29.874 |
| NPL | Nepal | South-East Asia | Lower-middle-income | True | True | Complete four-indicator frame | 5.400 | 38.300 | 36.432 | 3.517 |
| NRU | Nauru | Western Pacific | High-income | True | True | Complete four-indicator frame | 44.600 | 100.000 | 7.405 | 22.933 |
| NZL | New Zealand | Western Pacific | High-income | True | True | Complete four-indicator frame | 11.100 | 100.000 | 8.609 | 29.518 |
| OMN | Oman | Eastern Mediterranean | High-income | True | True | Complete four-indicator frame | 0.400 | 100.000 | 34.883 | 2.053 |
| PAK | Pakistan | Eastern Mediterranean | Lower-middle-income | True | True | Complete four-indicator frame | 3.000 | 49.500 | 50.131 | 4.731 |
| PAN | Panama | Americas | High-income | True | True | Complete four-indicator frame | 1.900 | 100.000 | 11.779 | 5.766 |
| PER | Peru | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 2.600 | 86.500 | 29.066 | 9.818 |
| PHL | Philippines | Western Pacific | Lower-middle-income | True | True | Complete four-indicator frame | 4.500 | 54.000 | 22.451 | 9.463 |
| PLW | Palau | Western Pacific | High-income | True | True | Complete four-indicator frame | 7.600 | 100.000 | 7.824 | 46.647 |
| PNG | Papua New Guinea | Western Pacific | Lower-middle-income | True | True | Complete four-indicator frame | 24.900 | 9.800 | 8.886 | 10.072 |
| POL | Poland | European | High-income | True | True | Complete four-indicator frame | 20.100 | 100.000 | 18.828 | 24.382 |
| PRI | Puerto Rico | Americas | High-income | False | False | Other multiple-indicator missingness |  |  |  |  |
| PRK | Democratic People's Republic of Korea | South-East Asia | Low-income | True | False | Complete four-indicator frame | 0.000 | 12.100 | 41.460 | 14.375 |
| PRT | Portugal | European | High-income | True | True | Complete four-indicator frame | 20.700 | 100.000 | 7.342 | 9.147 |
| PRY | Paraguay | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 3.900 | 69.350 | 12.310 | 7.070 |
| PSE | occupied Palestinian territory | Eastern Mediterranean | Lower-middle-income | False | False | Other multiple-indicator missingness |  |  | 30.819 |  |
| QAT | Qatar | Eastern Mediterranean | High-income | True | True | Complete four-indicator frame | 1.900 | 100.000 | 59.037 | 6.979 |
| ROU | Romania | European | High-income | True | True | Complete four-indicator frame | 20.300 | 100.000 | 13.300 | 14.502 |
| RUS | Russian Federation | European | High-income | True | True | Complete four-indicator frame | 17.400 | 100.000 | 8.885 | 8.785 |
| RWA | Rwanda | African | Low-income | True | True | Complete four-indicator frame | 3.500 | 4.300 | 35.658 | 4.127 |
| SAU | Saudi Arabia | Eastern Mediterranean | High-income | True | True | Complete four-indicator frame | 2.000 | 100.000 | 57.156 | 3.513 |
| SDN | Sudan | Eastern Mediterranean | Low-income | False | False | Missing female smoking only |  | 63.400 | 21.426 | 4.425 |
| SEN | Senegal | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.600 | 30.700 | 38.213 | 3.874 |
| SGP | Singapore | Western Pacific | High-income | True | True | Complete four-indicator frame | 4.900 | 100.000 | 13.333 | 15.800 |
| SLB | Solomon Islands | Western Pacific | Lower-middle-income | True | True | Complete four-indicator frame | 19.400 | 8.600 | 7.829 | 11.155 |
| SLE | Sierra Leone | African | Low-income | True | True | Complete four-indicator frame | 3.900 | 0.800 | 39.422 | 3.045 |
| SLV | El Salvador | Americas | Upper-middle-income | True | True | Complete four-indicator frame | 1.900 | 92.000 | 22.152 | 7.679 |
| SMR | San Marino | European | High-income | False | False | Missing female smoking only |  | 100.000 | 9.849 | 11.674 |
| SOM | Somalia | Eastern Mediterranean | Low-income | False | False | Missing female smoking only |  | 3.700 | 14.277 | 2.015 |
| SRB | Serbia | European | Upper-middle-income | True | True | Complete four-indicator frame | 39.100 | 79.500 | 21.739 | 23.108 |
| SSD | South Sudan | African | Low-income | False | False | Missing female smoking only |  | 0.000 | 20.182 | 3.213 |
| STP | Sao Tome and Principe | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.900 | 3.500 | 33.750 | 7.440 |
| SUR | Suriname | Americas | Upper-middle-income | False | False | Missing female smoking only |  | 94.600 | 12.171 | 8.187 |
| SVK | Slovakia | European | High-income | True | True | Complete four-indicator frame | 28.500 | 100.000 | 15.891 | 12.530 |
| SVN | Slovenia | European | High-income | True | True | Complete four-indicator frame | 18.500 | 100.000 | 14.076 | 20.366 |
| SWE | Sweden | European | High-income | True | True | Complete four-indicator frame | 11.900 | 100.000 | 5.955 | 19.110 |
| SWZ | Eswatini | African | Lower-middle-income | True | True | Complete four-indicator frame | 1.000 | 49.400 | 15.073 | 10.604 |
| SYC | Seychelles | African | High-income | True | True | Complete four-indicator frame | 5.600 | 100.000 | 16.957 | 6.535 |
| SYR | Syrian Arab Republic | Eastern Mediterranean | Low-income | False | False | Missing female smoking only |  | 92.400 | 25.141 | 6.414 |
| TCD | Chad | African | Low-income | True | True | Complete four-indicator frame | 1.600 | 7.400 | 41.153 | 2.833 |
| TGO | Togo | African | Low-income | True | True | Complete four-indicator frame | 0.500 | 10.600 | 35.658 | 3.444 |
| THA | Thailand | South-East Asia | Upper-middle-income | True | True | Complete four-indicator frame | 1.500 | 84.400 | 24.639 | 15.647 |
| TJK | Tajikistan | European | Lower-middle-income | False | False | Missing female smoking only |  | 84.800 | 53.646 | 4.640 |
| TKL | Tokelau | Western Pacific | Unclassified | False | False | Other multiple-indicator missingness |  |  |  |  |
| TKM | Turkmenistan | European | Upper-middle-income | True | True | Complete four-indicator frame | 0.500 | 99.900 | 26.409 | 3.755 |
| TLS | Timor-Leste | South-East Asia | Lower-middle-income | True | True | Complete four-indicator frame | 4.900 | 14.900 | 20.474 | 8.085 |
| TON | Tonga | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 15.500 | 85.200 | 7.521 | 12.282 |
| TTO | Trinidad and Tobago | Americas | High-income | False | False | Missing female smoking only |  | 100.000 | 10.265 | 4.793 |
| TUN | Tunisia | Eastern Mediterranean | Lower-middle-income | True | True | Complete four-indicator frame | 1.600 | 99.900 | 26.524 | 3.498 |
| TUR | Türkiye | European | Upper-middle-income | True | True | Complete four-indicator frame | 19.800 | 95.300 | 23.251 | 10.390 |
| TUV | Tuvalu | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 19.100 | 75.000 | 6.807 | 13.448 |
| TZA | United Republic of Tanzania | African | Lower-middle-income | True | True | Complete four-indicator frame | 1.300 | 6.900 | 15.364 | 4.202 |
| UGA | Uganda | African | Low-income | True | True | Complete four-indicator frame | 2.000 | 1.400 | 31.313 | 5.516 |
| UKR | Ukraine | European | Upper-middle-income | True | True | Complete four-indicator frame | 11.500 | 95.300 | 13.507 | 6.700 |
| URY | Uruguay | Americas | High-income | True | True | Complete four-indicator frame | 17.500 | 100.000 | 8.476 | 15.556 |
| USA | United States of America | Americas | High-income | True | True | Complete four-indicator frame | 16.800 | 100.000 | 7.180 | 32.503 |
| UZB | Uzbekistan | European | Lower-middle-income | True | True | Complete four-indicator frame | 1.000 | 80.700 | 40.979 | 3.702 |
| VCT | Saint Vincent and the Grenadines | Americas | Upper-middle-income | False | False | Missing female smoking only |  | 91.900 | 9.413 | 6.471 |
| VEN | Venezuela (Bolivarian Republic of) | Americas | Unclassified | False | False | Missing female smoking only |  | 94.550 | 16.214 | 12.331 |
| VNM | Viet Nam | Western Pacific | Lower-middle-income | True | True | Complete four-indicator frame | 1.000 | 95.900 | 20.892 | 11.338 |
| VUT | Vanuatu | Western Pacific | Lower-middle-income | False | False | Missing female smoking only |  | 17.200 | 8.421 | 7.517 |
| WSM | Samoa | Western Pacific | Upper-middle-income | True | True | Complete four-indicator frame | 13.300 | 36.600 | 7.780 | 3.308 |
| YEM | Yemen | Eastern Mediterranean | Low-income | True | True | Complete four-indicator frame | 6.500 | 51.300 | 41.609 | 4.195 |
| ZAF | South Africa | African | Upper-middle-income | True | True | Complete four-indicator frame | 6.500 | 88.100 | 19.748 | 11.099 |
| ZMB | Zambia | African | Lower-middle-income | True | True | Complete four-indicator frame | 2.700 | 10.900 | 16.897 | 6.251 |
| ZWE | Zimbabwe | African | Lower-middle-income | True | True | Complete four-indicator frame | 0.800 | 30.300 | 13.076 | 9.773 |

*Notes:* Complete status requires current female smoking, clean-fuel access, ambient PM2.5 and age-standardised female lung-cancer incidence.

### Supplementary Table S5. Primary-indicator coverage by income group and WHO region
| stratifier | group | n_total | n_complete | complete_percent | coverage_female_smoking_2022 | coverage_clean_fuel_2020 | coverage_PM25_2019 | coverage_female_LC_incidence_2021 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Income group | High-income | 64 | 57 | 89.1 | 90.6 | 96.9 | 98.4 | 98.4 |
| Income group | Low-income | 25 | 18 | 72.0 | 72.0 | 100.0 | 100.0 | 100.0 |
| Income group | Lower-middle-income | 50 | 41 | 82.0 | 84.0 | 96.0 | 100.0 | 98.0 |
| Income group | Unclassified | 5 | 2 | 40.0 | 40.0 | 80.0 | 80.0 | 80.0 |
| Income group | Upper-middle-income | 53 | 45 | 84.9 | 84.9 | 98.1 | 100.0 | 100.0 |
| WHO region | African | 47 | 39 | 83.0 | 83.0 | 100.0 | 100.0 | 100.0 |
| WHO region | Americas | 36 | 26 | 72.2 | 72.2 | 97.2 | 97.2 | 97.2 |
| WHO region | Eastern Mediterranean | 22 | 15 | 68.2 | 72.7 | 86.4 | 100.0 | 95.5 |
| WHO region | European | 53 | 48 | 90.6 | 92.5 | 98.1 | 100.0 | 100.0 |
| WHO region | South-East Asia | 10 | 10 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| WHO region | Western Pacific | 29 | 25 | 86.2 | 86.2 | 96.6 | 96.6 | 96.6 |

*Notes:* Percentages use the number of countries or territories in each stratum as the denominator.

### Supplementary Table S6. Descriptive exposure and incidence distributions
| stratifier | group | indicator | n | median | Q1 | Q3 | minimum | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Income group | High-income | Current female smoking (%) | 58 | 17.20 | 6.25 | 22.67 | 0.40 | 44.60 |
| Income group | High-income | Historical female smoking (%) | 58 | 22.90 | 9.15 | 28.40 | 0.53 | 58.10 |
| Income group | High-income | Clean-fuel deficit (percentage points) | 62 | 0.00 | 0.00 | 0.00 | 0.00 | 4.10 |
| Income group | High-income | Urban-rural clean-fuel gap (percentage points) | 62 | 0.00 | 0.00 | 0.00 | 0.00 | 9.80 |
| Income group | High-income | Ambient PM2.5 (micrograms per cubic metre) | 63 | 10.73 | 8.50 | 14.57 | 5.20 | 64.08 |
| Income group | High-income | Age-standardised female LC incidence (per 100,000) | 63 | 15.80 | 9.11 | 22.98 | 2.05 | 56.17 |
| Income group | Low-income | Current female smoking (%) | 18 | 1.30 | 0.60 | 2.00 | 0.00 | 6.50 |
| Income group | Low-income | Historical female smoking (%) | 18 | 3.02 | 1.31 | 5.45 | 0.00 | 11.20 |
| Income group | Low-income | Clean-fuel deficit (percentage points) | 25 | 96.20 | 88.30 | 98.80 | 7.60 | 100.00 |
| Income group | Low-income | Urban-rural clean-fuel gap (percentage points) | 25 | 7.00 | 2.10 | 20.80 | 0.00 | 68.10 |
| Income group | Low-income | Ambient PM2.5 (micrograms per cubic metre) | 25 | 34.85 | 22.74 | 39.42 | 14.28 | 62.49 |
| Income group | Low-income | Age-standardised female LC incidence (per 100,000) | 25 | 3.44 | 2.83 | 4.19 | 0.82 | 14.38 |
| Income group | Lower-middle-income | Current female smoking (%) | 42 | 1.50 | 0.83 | 3.95 | 0.20 | 26.80 |
| Income group | Lower-middle-income | Historical female smoking (%) | 42 | 3.50 | 1.87 | 10.41 | 0.50 | 46.23 |
| Income group | Lower-middle-income | Clean-fuel deficit (percentage points) | 48 | 63.85 | 45.30 | 87.05 | 0.10 | 99.00 |
| Income group | Lower-middle-income | Urban-rural clean-fuel gap (percentage points) | 48 | 33.25 | 15.77 | 48.12 | 0.00 | 76.40 |
| Income group | Lower-middle-income | Ambient PM2.5 (micrograms per cubic metre) | 50 | 24.73 | 15.52 | 37.58 | 7.62 | 63.16 |
| Income group | Lower-middle-income | Age-standardised female LC incidence (per 100,000) | 49 | 4.74 | 3.66 | 9.46 | 0.92 | 17.85 |
| Income group | Unclassified | Current female smoking (%) | 2 | 11.55 | 6.23 | 16.88 | 0.90 | 22.20 |
| Income group | Unclassified | Historical female smoking (%) | 2 | 15.55 | 8.18 | 22.93 | 0.80 | 30.30 |
| Income group | Unclassified | Clean-fuel deficit (percentage points) | 4 | 14.68 | 4.49 | 41.38 | 1.60 | 93.80 |
| Income group | Unclassified | Urban-rural clean-fuel gap (percentage points) | 4 | 18.20 | 10.35 | 36.45 | -0.30 | 78.30 |
| Income group | Unclassified | Ambient PM2.5 (micrograms per cubic metre) | 4 | 12.01 | 7.54 | 17.61 | 6.74 | 21.80 |
| Income group | Unclassified | Age-standardised female LC incidence (per 100,000) | 4 | 11.64 | 8.86 | 13.45 | 2.58 | 16.81 |
| Income group | Upper-middle-income | Current female smoking (%) | 45 | 4.00 | 1.90 | 9.50 | 0.10 | 39.10 |
| Income group | Upper-middle-income | Historical female smoking (%) | 45 | 7.60 | 4.30 | 13.43 | 0.27 | 39.03 |
| Income group | Upper-middle-income | Clean-fuel deficit (percentage points) | 52 | 11.15 | 4.70 | 19.38 | 0.10 | 77.00 |
| Income group | Upper-middle-income | Urban-rural clean-fuel gap (percentage points) | 52 | 17.50 | 6.75 | 34.59 | 0.00 | 86.20 |
| Income group | Upper-middle-income | Ambient PM2.5 (micrograms per cubic metre) | 53 | 17.83 | 12.04 | 25.17 | 6.81 | 41.30 |
| Income group | Upper-middle-income | Age-standardised female LC incidence (per 100,000) | 53 | 8.14 | 6.28 | 11.33 | 2.46 | 28.16 |
| WHO region | African | Current female smoking (%) | 39 | 1.20 | 0.60 | 2.30 | 0.30 | 6.50 |
| WHO region | African | Historical female smoking (%) | 39 | 2.43 | 1.17 | 5.08 | 0.50 | 10.77 |
| WHO region | African | Clean-fuel deficit (percentage points) | 47 | 89.10 | 58.10 | 97.35 | 0.00 | 100.00 |
| WHO region | African | Urban-rural clean-fuel gap (percentage points) | 47 | 19.00 | 2.30 | 43.00 | 0.00 | 71.30 |
| WHO region | African | Ambient PM2.5 (micrograms per cubic metre) | 47 | 28.00 | 17.28 | 37.89 | 10.48 | 56.37 |
| WHO region | African | Age-standardised female LC incidence (per 100,000) | 47 | 3.85 | 2.84 | 5.90 | 0.82 | 11.10 |
| WHO region | Americas | Current female smoking (%) | 26 | 3.70 | 2.12 | 8.40 | 1.70 | 26.70 |
| WHO region | Americas | Historical female smoking (%) | 26 | 7.73 | 4.18 | 18.75 | 2.80 | 38.33 |
| WHO region | Americas | Clean-fuel deficit (percentage points) | 35 | 5.45 | 0.00 | 12.65 | 0.00 | 95.80 |
| WHO region | Americas | Urban-rural clean-fuel gap (percentage points) | 35 | 7.30 | 0.00 | 20.30 | 0.00 | 76.40 |
| WHO region | Americas | Ambient PM2.5 (micrograms per cubic metre) | 35 | 11.78 | 9.19 | 16.11 | 5.20 | 29.07 |
| WHO region | Americas | Age-standardised female LC incidence (per 100,000) | 35 | 7.68 | 6.04 | 10.89 | 3.91 | 34.00 |
| WHO region | Eastern Mediterranean | Current female smoking (%) | 16 | 2.00 | 1.48 | 3.52 | 0.40 | 25.70 |
| WHO region | Eastern Mediterranean | Historical female smoking (%) | 16 | 3.92 | 2.95 | 7.34 | 0.53 | 29.93 |
| WHO region | Eastern Mediterranean | Clean-fuel deficit (percentage points) | 19 | 0.70 | 0.00 | 42.65 | 0.00 | 96.30 |
| WHO region | Eastern Mediterranean | Urban-rural clean-fuel gap (percentage points) | 19 | 0.70 | 0.00 | 9.35 | 0.00 | 68.10 |
| WHO region | Eastern Mediterranean | Ambient PM2.5 (micrograms per cubic metre) | 22 | 33.25 | 25.32 | 51.40 | 13.44 | 64.08 |
| WHO region | Eastern Mediterranean | Age-standardised female LC incidence (per 100,000) | 21 | 4.91 | 3.51 | 7.03 | 2.02 | 19.88 |
| WHO region | European | Current female smoking (%) | 49 | 19.50 | 11.90 | 24.00 | 0.10 | 39.10 |
| WHO region | European | Historical female smoking (%) | 49 | 23.87 | 15.73 | 29.40 | 0.27 | 40.73 |
| WHO region | European | Clean-fuel deficit (percentage points) | 52 | 0.00 | 0.00 | 1.72 | 0.00 | 59.80 |
| WHO region | European | Urban-rural clean-fuel gap (percentage points) | 52 | 0.00 | 0.00 | 2.85 | 0.00 | 46.20 |
| WHO region | European | Ambient PM2.5 (micrograms per cubic metre) | 53 | 13.51 | 9.52 | 19.06 | 5.47 | 53.65 |
| WHO region | European | Age-standardised female LC incidence (per 100,000) | 53 | 14.50 | 9.07 | 22.83 | 3.70 | 56.17 |
| WHO region | South-East Asia | Current female smoking (%) | 10 | 2.05 | 0.68 | 3.62 | 0.00 | 5.40 |
| WHO region | South-East Asia | Historical female smoking (%) | 10 | 7.63 | 2.89 | 10.53 | 0.00 | 27.57 |
| WHO region | South-East Asia | Clean-fuel deficit (percentage points) | 10 | 60.80 | 20.07 | 73.53 | 0.40 | 87.90 |
| WHO region | South-East Asia | Urban-rural clean-fuel gap (percentage points) | 10 | 33.90 | 16.45 | 45.70 | 0.40 | 54.80 |
| WHO region | South-East Asia | Ambient PM2.5 (micrograms per cubic metre) | 10 | 26.63 | 24.07 | 40.20 | 13.00 | 50.17 |
| WHO region | South-East Asia | Age-standardised female LC incidence (per 100,000) | 10 | 4.41 | 3.58 | 10.33 | 2.98 | 15.65 |
| WHO region | Western Pacific | Current female smoking (%) | 25 | 7.60 | 4.00 | 15.50 | 0.50 | 44.60 |
| WHO region | Western Pacific | Historical female smoking (%) | 25 | 13.33 | 5.53 | 24.13 | 1.97 | 58.10 |
| WHO region | Western Pacific | Clean-fuel deficit (percentage points) | 28 | 20.05 | 0.00 | 60.40 | 0.00 | 91.40 |
| WHO region | Western Pacific | Urban-rural clean-fuel gap (percentage points) | 28 | 18.45 | 0.00 | 39.66 | -0.30 | 86.20 |
| WHO region | Western Pacific | Ambient PM2.5 (micrograms per cubic metre) | 28 | 8.52 | 7.59 | 19.73 | 6.74 | 41.30 |
| WHO region | Western Pacific | Age-standardised female LC incidence (per 100,000) | 28 | 12.53 | 10.11 | 16.73 | 3.31 | 46.65 |

*Notes:* Summaries are unweighted country-level distributions.

### Supplementary Table S7. Income-group exposure inequality effect sizes
| exposure | contrast | unit | n_low_income | n_high_income | median_low_income | median_high_income | absolute_median_difference | median_difference_95CI_low | median_difference_95CI_high | cliffs_delta_low_vs_high | cliffs_delta_95CI_low | cliffs_delta_95CI_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Current female smoking | HIC minus LIC | percentage points | 18 | 58 | 1.300 | 17.200 | 15.900 | 10.550 | 18.550 | -0.875 | -0.965 | -0.750 |
| Clean-fuel deficit | LIC minus HIC | percentage points | 25 | 62 | 96.200 | 0.000 | 96.200 | 89.400 | 98.600 | 1.000 | 1.000 | 1.000 |
| Ambient PM2.5 | LIC minus HIC | micrograms per cubic metre | 25 | 63 | 34.850 | 10.731 | 24.119 | 14.772 | 28.646 | 0.790 | 0.646 | 0.916 |
| Urban-rural clean-fuel gap | LIC minus HIC | percentage points | 25 | 62 | 7.000 | 0.000 | 7.000 | 2.200 | 18.100 | 0.903 | 0.778 | 1.000 |

*Notes:* Median-difference and Cliff's-delta intervals use 5000 bootstrap samples.

### Supplementary Table S8. Age-standardised incidence model coefficients and fit
| section | model_or_analysis | term | n | estimate | robust_SE_HC3 | CI_low | CI_high | P | R2 | adjusted_R2 | AIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Coefficients | M0 historical smoking only | Intercept |  | -0.0000 | 0.0634 | -0.1251 | 0.1251 | 1.0000 |  |  |  |
| Coefficients | M0 historical smoking only | z_exposure |  | 0.6044 | 0.0772 | 0.4519 | 0.7569 | 0.0000 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | Intercept |  | 0.0375 | 0.1086 | -0.1770 | 0.2521 | 0.7300 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | z_exposure |  | 0.3229 | 0.0812 | 0.1626 | 0.4833 | 0.0001 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | z_log_GDP |  | 0.4830 | 0.0968 | 0.2919 | 0.6742 | 0.0000 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | z_urbanisation |  | 0.0274 | 0.0782 | -0.1270 | 0.1819 | 0.7261 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | WHO_region_Americas |  | -0.1356 | 0.1595 | -0.4506 | 0.1794 | 0.3963 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | WHO_region_Eastern Mediterranean |  | -0.3497 | 0.1933 | -0.7316 | 0.0323 | 0.0725 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | WHO_region_European |  | -0.0616 | 0.1749 | -0.4072 | 0.2840 | 0.7253 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | WHO_region_South-East Asia |  | -0.1745 | 0.2172 | -0.6036 | 0.2546 | 0.4229 |  |  |  |
| Coefficients | M1 + GDP, urbanisation, WHO region | WHO_region_Western Pacific |  | 0.3162 | 0.2360 | -0.1500 | 0.7824 | 0.1822 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | Intercept |  | -0.0018 | 0.1253 | -0.2494 | 0.2458 | 0.9886 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | z_exposure |  | 0.3106 | 0.0882 | 0.1363 | 0.4848 | 0.0006 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | z_log_GDP |  | 0.5122 | 0.1269 | 0.2615 | 0.7629 | 0.0001 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | z_urbanisation |  | 0.0375 | 0.0859 | -0.1321 | 0.2072 | 0.6628 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | z_clean_fuel_deficit |  | 0.0620 | 0.1045 | -0.1445 | 0.2686 | 0.5538 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | z_PM25_2019 |  | -0.0114 | 0.0800 | -0.1695 | 0.1468 | 0.8870 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | WHO_region_Americas |  | -0.0865 | 0.2055 | -0.4925 | 0.3195 | 0.6742 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | WHO_region_Eastern Mediterranean |  | -0.2814 | 0.2361 | -0.7479 | 0.1851 | 0.2352 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | WHO_region_European |  | 0.0041 | 0.2030 | -0.3970 | 0.4052 | 0.9840 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | WHO_region_South-East Asia |  | -0.1331 | 0.2237 | -0.5750 | 0.3088 | 0.5527 |  |  |  |
| Coefficients | M2 + clean-fuel deficit and PM2.5 | WHO_region_Western Pacific |  | 0.3456 | 0.2328 | -0.1144 | 0.8056 | 0.1397 |  |  |  |
| Model fit | M0 historical smoking only |  | 163.0000 |  |  |  |  |  | 0.3653 | 0.3614 | 392.4736 |
| Model fit | M1 + GDP, urbanisation, WHO region |  | 163.0000 |  |  |  |  |  | 0.5639 | 0.5412 | 345.3068 |
| Model fit | M2 + clean-fuel deficit and PM2.5 |  | 161.0000 |  |  |  |  |  | 0.5647 | 0.5357 | 346.6883 |

*Notes:* HC3 confidence intervals are reported for coefficients; R-squared, adjusted R-squared and AIC are reported in model-fit rows.

### Supplementary Table S9. Alternative female-smoking exposure windows
| exposure_window | n | estimate | CI_low | CI_high | P | R2 |
| --- | --- | --- | --- | --- | --- | --- |
| Female smoking 2000 | 163 | 0.3386 | 0.1755 | 0.5016 | 0.0001 | 0.5748 |
| Female smoking 2005 | 163 | 0.3207 | 0.1599 | 0.4815 | 0.0001 | 0.5626 |
| Female smoking 2010 | 163 | 0.2882 | 0.1344 | 0.4421 | 0.0003 | 0.5488 |
| Mean female smoking 2000-2010 | 163 | 0.3229 | 0.1626 | 0.4833 | 0.0001 | 0.5639 |
| Current female smoking 2022 | 163 | 0.1771 | 0.0167 | 0.3376 | 0.0307 | 0.5200 |

*Notes:* Each row uses the same structural adjustment set: log GDP, urbanisation and WHO region.

### Supplementary Table S10. Influence and spatial sensitivity analyses
| analysis | n | estimate | CI_low | CI_high | P |
| --- | --- | --- | --- | --- | --- |
| Primary HC3 model | 163 | 0.3229 | 0.1626 | 0.4833 | 0.0001 |
| Excluding Cook's distance >4/n | 152 | 0.4037 | 0.2775 | 0.5299 | 0.0000 |
| Additional adjustment for age 65+ | 163 | 0.2775 | 0.1170 | 0.4380 | 0.0008 |
| Population at least 1 million | 137 | 0.4533 | 0.2654 | 0.6411 | 0.0000 |
| Conley-type SE, 1500 km | 144 | 0.4453 | 0.2857 | 0.6048 | 0.0000 |
| Conley-type SE, 2500 km | 144 | 0.4453 | 0.2777 | 0.6129 | 0.0000 |
| Conley-type SE, 4000 km | 144 | 0.4453 | 0.2628 | 0.6278 | 0.0000 |
| Moran's I (6-nearest-neighbour weights) | 144 | 0.1055 |  |  | 0.0090 |

*Notes:* Conley-type intervals were calculated for the geocoded subset. Moran's I is reported without a confidence interval.

### Supplementary Table S11. Exploratory environmental heterogeneity models
| analysis | term | n | estimate | CI_low | CI_high | P | R2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Global, mutually adjusted | z_pm25 | 161 | -0.0093 | -0.1305 | 0.1120 | 0.8803 | 0.0005 |
| Non-high-income, mutually adjusted | z_pm25 | 104 | 0.1239 | 0.0133 | 0.2346 | 0.0285 | 0.0664 |
| Non-high-income + WHO region | z_pm25 | 104 | 0.1059 | -0.0423 | 0.2541 | 0.1593 | 0.1066 |
| PM2.5 x high-income interaction | pm25_x_high_income | 161 | -0.3481 | -0.5639 | -0.1323 | 0.0017 | 0.0568 |
| Interaction after Cook's distance exclusion | pm25_x_high_income | 151 | -0.2863 | -0.4189 | -0.1537 | 0.0000 | 0.0815 |

*Notes:* Environmental coefficients are supplementary and should not be interpreted as causal effects.

### Supplementary Table S12. Incidence-mortality residual consistency
| comparison | method | estimate | P | n |
| --- | --- | --- | --- | --- |
| Incidence residual vs mortality residual | Pearson | 0.8044 | 0.0000 | 163 |
| Incidence residual vs mortality residual | Spearman | 0.7581 | 0.0000 | 163 |

*Notes:* Both residuals were derived from models adjusted for historical smoking, log GDP, urbanisation and WHO region.
