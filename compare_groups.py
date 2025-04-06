import pandas as pd
import os

# === FILE LOCATIONS ===
matrix_file = "arg_matrix/arg_matrix_annotated.csv"
metadata_file = "sample_metadata.tsv"

# === LOAD FILES ===
df = pd.read_csv(matrix_file, index_col=0)
meta = pd.read_csv(metadata_file, sep="\t")

# === MERGE ===
df = df.merge(meta, left_index=True, right_on="sample_id")
df.set_index("sample_id", inplace=True)

# === GROUP COMPARISON ===
grouped = df.groupby("source")
group_mean = grouped.mean()

# === OUTPUT ===
output_path = "arg_matrix/group_comparison.csv"
group_mean.to_csv(output_path)

print(f"✅ Group comparison table saved to {output_path}")

