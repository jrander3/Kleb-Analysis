import pandas as pd
from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests

# === File Paths ===
matrix_file = "arg_matrix_relaxed/arg_matrix_annotated.csv"
metadata_file = "sample_metadata.tsv"

# === Load Data ===
df = pd.read_csv(matrix_file, index_col=0)
meta = pd.read_csv(metadata_file, sep="\t")

# Merge metadata
df = df.merge(meta, left_index=True, right_on="sample_id")
df.set_index("sample_id", inplace=True)

# === Run Fisher’s Exact Test for each ARG ===
results = []
for gene in df.columns[:-1]:  # last column is 'source'
    group_counts = df.groupby("source")[gene].value_counts().unstack().fillna(0)
    
    if group_counts.shape != (2, 2):
        continue  # skip genes only present in one group
    
    table = group_counts.values.astype(int)
    odds_ratio, p_value = fisher_exact(table)
    
    results.append({
        "gene": gene,
        "odds_ratio": odds_ratio,
        "p_value": p_value,
        "clinical_present": int(group_counts.loc["Clinical", 1]) if 1 in group_counts.columns else 0,
        "wastewater_present": int(group_counts.loc["Wastewater", 1]) if 1 in group_counts.columns else 0
    })

# === Multiple Testing Correction ===
df_results = pd.DataFrame(results)
df_results["fdr_corrected_p"] = multipletests(df_results["p_value"], method="fdr_bh")[1]

# === Save Results ===
df_results = df_results.sort_values("fdr_corrected_p")
df_results.to_csv("arg_matrix_relaxed/fisher_enrichment_results.csv", index=False)

print("✅ Fisher's test results saved to arg_matrix_relaxed/fisher_enrichment_results.csv")

