import pandas as pd
import matplotlib.pyplot as plt

# === Load clinical matrix ===
df = pd.read_csv("arg_matrix_relaxed/clinical_only_matrix.csv", index_col=0)

# === Count how many isolates have each gene ===
arg_counts = df.sum(axis=0).sort_values(ascending=False)

# === Plot top 20 ARGs ===
top_n = 20
top_args = arg_counts.head(top_n)

plt.figure(figsize=(10, 6))
top_args.plot(kind='bar')
plt.ylabel("Number of Clinical Isolates")
plt.title(f"Top {top_n} Resistance Genes in Clinical Klebsiella Isolates")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("arg_matrix_relaxed/top_clinical_args_barplot.png")
plt.show()

