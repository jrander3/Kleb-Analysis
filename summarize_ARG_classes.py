import pandas as pd
import matplotlib.pyplot as plt

# === File paths ===
matrix_file = "arg_matrix_relaxed/clinical_only_matrix.csv"
aro_index_file = "CARD/aro_index.tsv"

# === Load data ===
df = pd.read_csv(matrix_file, index_col=0)
aro_index = pd.read_csv(aro_index_file, sep="\t")

# === Map each gene to resistance class ===
# Use ARO Name and ARO Category
protein_to_class = dict(zip(aro_index['ARO Name'], aro_index['Drug Class']))

# Sum gene counts across all clinical isolates
arg_totals = df.sum(axis=0)

# Build class-level summary
class_counts = {}
for gene, count in arg_totals.items():
    resistance_class = protein_to_class.get(gene, "Unknown")
    class_counts[resistance_class] = class_counts.get(resistance_class, 0) + count

# Convert to DataFrame and save
class_df = pd.DataFrame.from_dict(class_counts, orient='index', columns=["Total_Count"])
class_df = class_df.sort_values("Total_Count", ascending=False)
class_df.to_csv("arg_matrix_relaxed/clinical_ARG_class_summary.csv")

# === Plot ===
plt.figure(figsize=(10, 6))
class_df.head(15).plot(kind='bar', legend=False)
plt.ylabel("Total Gene Hits")
plt.title("Top Resistance Classes in Clinical Klebsiella Isolates")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("arg_matrix_relaxed/clinical_ARG_class_summary.png")
print("✅ Saved ARG class summary to clinical_ARG_class_summary.csv and PNG")

