import pandas as pd

# === Load binary matrix ===
df = pd.read_csv("arg_matrix_relaxed/clinical_only_matrix.csv", index_col=0)

# Convert all values to string (0/1)
df = df.astype(str)

# === Generate short taxon names ===
short_names = {original: f"S{i+1}" for i, original in enumerate(df.index)}
df_short = df.rename(index=short_names)

# Save the mapping so you can recover original names
pd.Series(short_names).to_csv("arg_matrix_relaxed/phylip_taxon_map.csv", header=["short_name"])

# === Build PHYLIP lines ===
phylip_lines = []
num_taxa = df_short.shape[0]
num_chars = df_short.shape[1]

phylip_lines.append(f"{num_taxa} {num_chars}")

for isolate, row in df_short.iterrows():
    padded_name = isolate.ljust(10)
    data_line = "".join(row.values)
    phylip_lines.append(f"{padded_name}{data_line}")

# === Write to PHYLIP file ===
with open("arg_matrix_relaxed/clinical_ARGs.phy", "w") as f:
    f.write("\n".join(phylip_lines))

print("✅ Converted ARG matrix to PHYLIP format with short taxon names.")
print("🔁 Taxon name mapping saved to phylip_taxon_map.csv.")

