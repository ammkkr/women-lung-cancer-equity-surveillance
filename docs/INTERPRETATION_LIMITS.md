# Interpretation limits

This repository is intended to support transparent review and reuse of a country-level
equity surveillance analysis. Several boundaries are essential.

## Ecological design

The dataset contains one row per country. Findings describe country-level patterns and
data-system visibility. They cannot be used to infer individual exposure, individual risk,
or individual clinical outcomes.

## No causal attribution

The analyses are descriptive and associational. They do not estimate the causal effect of
tobacco, PM2.5, clean fuels, or any other exposure on female lung-cancer burden.

## Historical smoking proxy

Historical female smoking is defined as the mean of female smoking prevalence in 2000,
2005, and 2010. This proxy was chosen because comparable earlier country-level female
smoking data were not consistently available. It only partially adjusts for historical
tobacco exposure and does not capture the full 20-40 year exposure history relevant to
lung-cancer mortality.

## Smoking-adjusted burden residual

The residual is the difference between observed z-scored country-level burden and burden
expected under the available historical smoking proxy and structural covariates. It is:

- descriptive
- country-level
- partially historical-smoking-adjusted
- useful for surveillance questions

It is not:

- non-smoking lung-cancer burden
- an environmental attributable burden estimate
- an individual-level residual risk measure
- a causal estimate

## Clean-fuel deficit

Clean-fuel deficit is defined as 100 minus the proportion of the population primarily
relying on clean fuels and technologies for cooking. It is a structural proxy for
household energy poverty. It is not a direct personal household air-pollution exposure
measure.

## PM2.5

PM2.5 represents national annual mean ambient concentration. It is not personal exposure
and does not capture micro-environmental, occupational, indoor, or lifetime exposure
histories.

## Measured exposure-burden profiles

The measured exposure-side score combines current female smoking, clean-fuel deficit, and
PM2.5. It is a transparent surveillance heuristic. It should not be used as:

- a validated risk score
- a clinical prediction model
- a national policy ranking
- a performance league table
- evidence that one country has failed or succeeded

## Data visibility as an equity finding

The study treats missingness and data invisibility as part of the equity problem. Absence
of harmonised global indicators for second-hand smoke, occupational exposure, radon,
screening, stage, pathology, molecular subtype, treatment, survival, and socioeconomic
cancer outcomes means that full prevention-care pathway equity cannot yet be monitored
globally.
