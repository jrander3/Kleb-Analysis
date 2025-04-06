import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Load clinical-only matrix ===
df = pd.read_csv("arg_matrix_relaxed/clinical_only_matrix.csv", index_col=0)

# === Plot clustermap ===
sns.set(font_scale=0.6)
g = sns.clustermap(
    df,
    figsize=(12, 10),
    cmap="Blues",
    col_cluster=True,
    row_cluster=True,
    linewidths=0.2,
    cbar_pos=(0.02, 0.8, 0.03, 0.18)
)

g.fig.suptitle("Clustermap of Clinical Klebsiella Isolates by ARG Profile", fontsize=12)
plt.tight_layout()

# === Save plot ===
g.savefig("arg_matrix_relaxed/clinical_clustermap.png")
print("✅ Clustermap saved to arg_matrix_relaxed/clinical_clustermap.png")

