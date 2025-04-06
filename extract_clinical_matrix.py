import pandas as pd

# === File paths ===
matrix_file = "arg_matrix_relaxed/arg_matrix_annotated.csv"
metadata_file = "sample_metadata.tsv"

# === Load files ===
df = pd.read_csv(matrix_file, index_col=0)
meta = pd.read_csv(metadata_file, sep="\t")

# === Filter to clinical samples ===
clinical_ids = meta[meta['source'] == "Clinical"]["sample_id"]
df_clinical = df.loc[df.index.isin(clinical_ids)]

# === Save output ===
df_clinical.to_csv("arg_matrix_relaxed/clinical_only_matrix.csv")
print("✅ Saved clinical-only matrix to arg_matrix_relaxed/clinical_only_matrix.csv")

