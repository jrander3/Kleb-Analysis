import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Load matrix ===
df = pd.read_csv("arg_matrix_relaxed/clinical_only_matrix.csv", index_col=0)

# === Co-occurrence matrix ===
co_matrix = df.T.dot(df)  # gene-by-gene dot product gives co-occurrence counts

# === Save matrix ===
co_matrix.to_csv("arg_matrix_relaxed/clinical_ARG_cooccurrence.csv")

# === Heatmap of top co-occurring genes (top 20 by total occurrence) ===
top_genes = df.sum().sort_values(ascending=False).head(20).index
co_top = co_matrix.loc[top_genes, top_genes]

plt.figure(figsize=(10, 8))
sns.heatmap(co_top, cmap="Purples", linewidths=0.5, annot=True, fmt="d")
plt.title("ARG Co-occurrence (Top 20 Genes) - Clinical Isolates")
plt.tight_layout()
plt.savefig("arg_matrix_relaxed/clinical_ARG_cooccurrence_heatmap.png")
print("✅ Saved ARG co-occurrence matrix and heatmap.")

