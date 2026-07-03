"""Reproduce key results and simplified figures from the public repository data.

The publication figures in ``figures/`` are the final manuscript-ready versions. This
script provides a transparent, portable check that the shared aggregate dataset and
result tables reproduce the key numerical findings and generate simplified figure
versions without relying on local paths or manuscript drafting files.

Run from the repository root:

    python scripts/generate_figures.py
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[1]
MPL_CACHE = ROOT / ".cache" / "matplotlib"
MPL_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    import statsmodels.formula.api as smf

    HAS_STATSMODELS = True
except ImportError:
    smf = None
    HAS_STATSMODELS = False

DATA = ROOT / "data"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
REPRO_FIGURES = FIGURES / "reproduced"
REPRO_RESULTS = RESULTS / "reproduced"
REPRO_FIGURES.mkdir(parents=True, exist_ok=True)
REPRO_RESULTS.mkdir(parents=True, exist_ok=True)

INCOME_ORDER = [
    "Low-income",
    "Lower-middle-income",
    "Upper-middle-income",
    "High-income",
    "Unclassified",
]
INCOME_SHORT = {
    "Low-income": "Low",
    "Lower-middle-income": "Lower-middle",
    "Upper-middle-income": "Upper-middle",
    "High-income": "High",
    "Unclassified": "Unclassified",
}
REGION_ORDER = [
    "African",
    "Americas",
    "Eastern Mediterranean",
    "European",
    "South-East Asia",
    "Western Pacific",
]
REGION_COLORS = {
    "African": "#4C72B0",
    "Americas": "#DD8452",
    "Eastern Mediterranean": "#55A868",
    "European": "#C44E52",
    "South-East Asia": "#8172B3",
    "Western Pacific": "#937860",
}
INCOME_COLORS = {
    "Low-income": "#C44E52",
    "Lower-middle-income": "#E6A14A",
    "Upper-middle-income": "#4C72B0",
    "High-income": "#55A868",
    "Unclassified": "#A6A6A6",
}


def zscore(series: pd.Series) -> pd.Series:
    """Sample-standardized z-score, matching the usual R ``scale`` convention."""
    return (series - series.mean()) / series.std(ddof=1)


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(DATA / "country_level_analysis_dataset.csv")
    visibility = pd.read_csv(DATA / "data_visibility_matrix.csv")
    for col in ["analysis_core_complete", "analysis_core_plus_covariates_complete"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().map({"true": True, "false": False})
    df["income_group"] = df["income_group"].fillna("Unclassified")
    df["logGDP"] = np.log(df["GDP"])
    for col in [
        "historical_female_smoking",
        "female_smoking_2022",
        "clean_fuel_deficit",
        "rural_clean_fuel_disadvantage",
        "PM25_2019",
        "female_LC_mort_2021",
        "female_LC_YLL_2021",
        "female_LC_DALY_2021",
        "female_LC_incidence_2021",
        "logGDP",
        "urbanisation",
        "age65",
        "SDI",
        "HDI",
    ]:
        if col in df.columns:
            df[f"z_{col}"] = zscore(df[col])
    return df, visibility


def fit_historical_models(df: pd.DataFrame) -> pd.DataFrame:
    if not HAS_STATSMODELS:
        src = pd.read_csv(RESULTS / "historical_smoking_model_coefficients.csv")
        fit = pd.read_csv(RESULTS / "historical_smoking_model_fit.csv")
        out = src[
            src["term"].eq("z_historical_smoking")
            & src["covariate_set"].eq("primary_logGDP")
        ][["outcome", "outcome_label", "term", "estimate", "conf_low", "conf_high", "p_value"]].copy()
        out = out.merge(
            fit[fit["covariate_set"].eq("primary_logGDP")][["outcome", "n", "r_squared", "adj_r_squared"]],
            on="outcome",
            how="left",
        )
        out.to_csv(REPRO_RESULTS / "reproduced_historical_smoking_models.csv", index=False)
        return out

    outcomes = {
        "female_LC_mort_2021": "Female LC mortality",
        "female_LC_YLL_2021": "Female LC YLL",
        "female_LC_DALY_2021": "Female LC DALY",
    }
    rows = []
    for outcome, label in outcomes.items():
        z_outcome = f"z_{outcome}"
        cols = [z_outcome, "z_historical_female_smoking", "z_logGDP", "z_urbanisation", "z_age65", "WHO_region"]
        model_df = df[cols].dropna().copy()
        formula = f"{z_outcome} ~ z_historical_female_smoking + z_logGDP + z_urbanisation + z_age65 + C(WHO_region)"
        fit = smf.ols(formula, data=model_df).fit(cov_type="HC3")
        rows.append(
            {
                "outcome": outcome,
                "outcome_label": label,
                "term": "z_historical_female_smoking",
                "estimate": fit.params["z_historical_female_smoking"],
                "conf_low": fit.conf_int().loc["z_historical_female_smoking", 0],
                "conf_high": fit.conf_int().loc["z_historical_female_smoking", 1],
                "p_value": fit.pvalues["z_historical_female_smoking"],
                "n": int(fit.nobs),
                "r_squared": fit.rsquared,
                "adj_r_squared": fit.rsquared_adj,
            }
        )
    out = pd.DataFrame(rows)
    out.to_csv(REPRO_RESULTS / "reproduced_historical_smoking_models.csv", index=False)
    return out


def fit_environmental_models(df: pd.DataFrame) -> pd.DataFrame:
    if not HAS_STATSMODELS:
        out = pd.read_csv(RESULTS / "pm25_robustness_results.csv")
        out.to_csv(REPRO_RESULTS / "reproduced_pm25_residual_models.csv", index=False)
        return out

    base = df.dropna(
        subset=[
            "smoking_adjusted_burden_residual_mortality",
            "z_PM25_2019",
            "z_clean_fuel_deficit",
            "WHO_region",
            "z_SDI",
            "z_urbanisation",
            "z_age65",
        ]
    ).copy()
    base["non_high_income"] = base["income_group"].ne("High-income")
    rows = []
    models = {
        "global_base": base,
        "non_high_income_base": base[base["non_high_income"]],
        "high_income_base": base[~base["non_high_income"]],
    }
    for label, model_df in models.items():
        if len(model_df) < 15:
            continue
        fit = smf.ols(
            "smoking_adjusted_burden_residual_mortality ~ z_PM25_2019 + z_clean_fuel_deficit",
            data=model_df,
        ).fit(cov_type="HC3")
        rows.append(
            {
                "model_id": label,
                "term": "z_PM25_2019",
                "estimate": fit.params["z_PM25_2019"],
                "conf_low": fit.conf_int().loc["z_PM25_2019", 0],
                "conf_high": fit.conf_int().loc["z_PM25_2019", 1],
                "p_value": fit.pvalues["z_PM25_2019"],
                "n": int(fit.nobs),
                "r_squared": fit.rsquared,
            }
        )
    nonhic = base[base["non_high_income"]].copy()
    fit = smf.ols(
        "smoking_adjusted_burden_residual_mortality ~ z_PM25_2019 + z_clean_fuel_deficit + C(WHO_region) + z_SDI + z_urbanisation + z_age65",
        data=nonhic,
    ).fit(cov_type="HC3")
    rows.append(
        {
            "model_id": "non_high_income_extended",
            "term": "z_PM25_2019",
            "estimate": fit.params["z_PM25_2019"],
            "conf_low": fit.conf_int().loc["z_PM25_2019", 0],
            "conf_high": fit.conf_int().loc["z_PM25_2019", 1],
            "p_value": fit.pvalues["z_PM25_2019"],
            "n": int(fit.nobs),
            "r_squared": fit.rsquared,
        }
    )
    out = pd.DataFrame(rows)
    out.to_csv(REPRO_RESULTS / "reproduced_pm25_residual_models.csv", index=False)
    return out


def reproduce_clean_fuel_correlations(df: pd.DataFrame) -> pd.DataFrame:
    targets = {
        "SDI": "SDI",
        "HDI": "HDI",
        "urbanisation": "Urbanisation",
        "rural_clean_fuel_disadvantage": "Rural clean-fuel disadvantage",
    }
    rows = []
    for col, label in targets.items():
        temp = df[["clean_fuel_deficit", col]].dropna()
        rho, p_value = spearmanr(temp["clean_fuel_deficit"], temp[col])
        rows.append({"x": "clean_fuel_deficit", "y": col, "y_label": label, "n": len(temp), "rho": rho, "p_value": p_value})
    out = pd.DataFrame(rows)
    out.to_csv(REPRO_RESULTS / "reproduced_clean_fuel_correlations.csv", index=False)
    return out


def savefig(fig: plt.Figure, name: str) -> None:
    fig.savefig(REPRO_FIGURES / f"{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(REPRO_FIGURES / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)


def draw_figure1(df: pd.DataFrame, visibility: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    coverage_vars = [
        "female_LC_mort_2021",
        "female_LC_YLL_2021",
        "female_LC_DALY_2021",
        "female_LC_incidence_2021",
        "PM25_2019",
        "clean_fuel_2020",
        "female_smoking_2022",
        "HDI",
        "SDI",
    ]
    labels = [
        "Female LC mortality",
        "Female LC YLL",
        "Female LC DALY",
        "Female LC incidence",
        "PM2.5",
        "Clean fuels",
        "Female smoking",
        "HDI",
        "SDI",
    ]
    coverage = pd.Series({lab: df[var].notna().sum() for var, lab in zip(coverage_vars, labels)}).sort_values()
    axes[0].barh(coverage.index, coverage.values, color="#4C72B0")
    axes[0].axvline(int(df["analysis_core_complete"].sum()), color="#C44E52", linestyle="--")
    axes[0].set_xlabel("Countries with non-missing data")
    axes[0].set_title("A. Core indicator coverage", loc="left", fontweight="bold")

    avail_order = ["yes", "partially visible", "largely absent", "absent"]
    counts = visibility["available_in_HIDR"].value_counts().reindex(avail_order).fillna(0)
    axes[1].bar(counts.index, counts.values, color=["#4C72B0", "#E6A14A", "#C44E52", "#8C8C8C"])
    axes[1].set_ylabel("Pathway components")
    axes[1].set_title("B. Prevention-care visibility summary", loc="left", fontweight="bold")
    axes[1].tick_params(axis="x", rotation=30)
    savefig(fig, "Figure1_reproduced_data_visibility")


def box_by_income(ax: plt.Axes, df: pd.DataFrame, var: str, title: str, ylabel: str, log: bool = False) -> None:
    values = []
    labels = []
    colors = []
    for group in INCOME_ORDER:
        vals = df.loc[df["income_group"].eq(group), var].dropna()
        if len(vals):
            values.append(vals.values)
            labels.append(INCOME_SHORT[group])
            colors.append(INCOME_COLORS[group])
    bp = ax.boxplot(values, patch_artist=True, showfliers=False)
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.35)
        patch.set_edgecolor("#333333")
    for i, vals in enumerate(values, start=1):
        rng = np.random.default_rng(i)
        ax.scatter(rng.normal(i, 0.05, len(vals)), vals, s=12, alpha=0.45, color=colors[i - 1])
    ax.set_xticks(range(1, len(labels) + 1))
    ax.set_xticklabels(labels, rotation=25, ha="right")
    ax.set_title(title, loc="left", fontweight="bold")
    ax.set_ylabel(ylabel)
    if log:
        ax.set_yscale("log")


def draw_figure2(df: pd.DataFrame, corr: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    box_by_income(axes[0, 0], df, "female_smoking_2022", "A. Female smoking by income", "Prevalence (%)")
    box_by_income(axes[0, 1], df, "clean_fuel_deficit", "B. Clean-fuel deficit by income", "Population without access (%)")
    box_by_income(axes[0, 2], df, "PM25_2019", "C. Ambient PM2.5 by income", "Annual mean PM2.5")
    box_by_income(axes[1, 0], df, "female_LC_mort_2021", "D. Female LC mortality by income", "Per 100,000, log scale", log=True)
    box_by_income(axes[1, 1], df, "rural_clean_fuel_disadvantage", "E. Urban-rural clean-fuel gap", "Percentage points")
    corr_plot = corr.iloc[::-1]
    axes[1, 2].axvline(0, color="#999999", linewidth=0.8)
    for i, row in enumerate(corr_plot.itertuples()):
        axes[1, 2].plot([0, row.rho], [i, i], color="#777777", linewidth=1.2)
        axes[1, 2].scatter(row.rho, i, s=45, color="#4C72B0" if row.rho < 0 else "#C44E52")
        axes[1, 2].text(row.rho + (0.04 if row.rho >= 0 else -0.04), i, f"{row.rho:.2f}", ha="left" if row.rho >= 0 else "right", va="center")
    axes[1, 2].set_yticks(range(len(corr_plot)))
    axes[1, 2].set_yticklabels(corr_plot["y_label"])
    axes[1, 2].set_xlim(-1, 1)
    axes[1, 2].set_xlabel("Spearman rho")
    axes[1, 2].set_title("F. Correlates of clean-fuel deficit", loc="left", fontweight="bold")
    fig.tight_layout()
    savefig(fig, "Figure2_reproduced_visible_exposure_inequalities")


def draw_figure3(df: pd.DataFrame, hist: pd.DataFrame, pm25: pd.DataFrame) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    plot_df = df[["historical_female_smoking", "female_LC_mort_2021", "WHO_region"]].dropna()
    for region, group in plot_df.groupby("WHO_region"):
        axes[0, 0].scatter(group["historical_female_smoking"], group["female_LC_mort_2021"], s=20, alpha=0.65, label=region, color=REGION_COLORS.get(region, "#777777"))
    axes[0, 0].set_xlabel("Historical female smoking proxy (%)")
    axes[0, 0].set_ylabel("Female LC mortality per 100,000")
    axes[0, 0].set_title("A. Historical smoking and burden", loc="left", fontweight="bold")

    y = np.arange(len(hist))
    axes[0, 1].axvline(0, color="#999999", linewidth=0.8)
    axes[0, 1].errorbar(hist["estimate"], y, xerr=[hist["estimate"] - hist["conf_low"], hist["conf_high"] - hist["estimate"]], fmt="o", color="#4C72B0")
    axes[0, 1].set_yticks(y)
    axes[0, 1].set_yticklabels(hist["outcome_label"])
    axes[0, 1].set_xlabel("Adjusted beta for historical smoking")
    axes[0, 1].set_title("B. Historical smoking coefficients", loc="left", fontweight="bold")

    scatter = df[["PM25_2019", "smoking_adjusted_burden_residual_mortality", "income_group"]].dropna().copy()
    scatter["income_binary"] = np.where(scatter["income_group"].eq("High-income"), "High-income", "Non-high-income")
    for label, color in [("High-income", "#4C72B0"), ("Non-high-income", "#DD8452")]:
        group = scatter[scatter["income_binary"].eq(label)]
        axes[1, 0].scatter(group["PM25_2019"], group["smoking_adjusted_burden_residual_mortality"], s=22, alpha=0.6, label=label, color=color)
    axes[1, 0].axhline(0, color="#999999", linestyle="--", linewidth=0.8)
    axes[1, 0].set_xlabel("Ambient PM2.5")
    axes[1, 0].set_ylabel("Smoking-adjusted burden residual")
    axes[1, 0].set_title("C. PM2.5 residual pattern", loc="left", fontweight="bold")
    axes[1, 0].legend(frameon=False)

    y2 = np.arange(len(pm25))
    axes[1, 1].axvline(0, color="#999999", linewidth=0.8)
    axes[1, 1].errorbar(pm25["estimate"], y2, xerr=[pm25["estimate"] - pm25["conf_low"], pm25["conf_high"] - pm25["estimate"]], fmt="o", color="#C44E52")
    axes[1, 1].set_yticks(y2)
    axes[1, 1].set_yticklabels(pm25["model_id"])
    axes[1, 1].set_xlabel("Beta for PM2.5")
    axes[1, 1].set_title("D. PM2.5 robustness models", loc="left", fontweight="bold")
    fig.tight_layout()
    savefig(fig, "Figure3_reproduced_smoking_adjusted_pm25_signal")


def draw_figure4(df: pd.DataFrame) -> None:
    plot_df = df[["multiple_exposure_score_equal_weighted", "female_LC_mort_2021", "WHO_region", "country"]].dropna()
    xmed = plot_df["multiple_exposure_score_equal_weighted"].median()
    ymed = plot_df["female_LC_mort_2021"].median()
    fig, ax = plt.subplots(figsize=(6.2, 5.4))
    for region, group in plot_df.groupby("WHO_region"):
        ax.scatter(group["multiple_exposure_score_equal_weighted"], group["female_LC_mort_2021"], s=24, alpha=0.75, label=region, color=REGION_COLORS.get(region, "#777777"), edgecolor="white", linewidth=0.3)
    ax.axvline(xmed, color="#555555", linestyle="--", linewidth=0.9)
    ax.axhline(ymed, color="#555555", linestyle="--", linewidth=0.9)
    ax.set_yscale("log")
    ax.set_xlabel("Measured exposure-side score")
    ax.set_ylabel("Female LC mortality per 100,000, log scale")
    ax.set_title("Measured exposure-burden surveillance profiles", loc="left", fontweight="bold")
    ax.legend(frameon=False, fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
    savefig(fig, "Figure4_reproduced_exposure_burden_profiles")


def main() -> None:
    df, visibility = load_data()
    hist = fit_historical_models(df)
    env = fit_environmental_models(df)
    corr = reproduce_clean_fuel_correlations(df)
    draw_figure1(df, visibility)
    draw_figure2(df, corr)
    draw_figure3(df, hist, env)
    draw_figure4(df)
    print(f"Loaded {len(df)} countries.")
    print(f"Core overlap: {int(df['analysis_core_complete'].sum())}")
    print("Reproduced outputs written to:")
    print(f"  {REPRO_RESULTS.relative_to(ROOT)}")
    print(f"  {REPRO_FIGURES.relative_to(ROOT)}")
    print("Historical smoking coefficients:")
    print(hist[["outcome_label", "estimate", "conf_low", "conf_high", "p_value", "n", "r_squared"]].to_string(index=False))
    print("Clean-fuel correlations:")
    print(corr[["y_label", "rho", "p_value", "n"]].to_string(index=False))
    print("PM2.5 residual models:")
    print(env[["model_id", "estimate", "conf_low", "conf_high", "p_value", "n", "r_squared"]].to_string(index=False))


if __name__ == "__main__":
    main()
