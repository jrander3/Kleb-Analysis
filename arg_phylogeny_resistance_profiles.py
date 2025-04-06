import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# === Load matrix ===
df = pd.read_csv("arg_matrix_relaxed/clinical_only_matrix.csv", index_col=0)

# === Calculate pairwise distance ===
# Binary Jaccard distance (good for presence/absence data)
dist_matrix = pdist(df, metric="jaccard")

# === Hierarchical clustering (UPGMA)
linkage_matrix = linkage(dist_matrix, method="average")

# === Plot dendrogram ===
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix, labels=df.index, leaf_rotation=90)
plt.title("Phylogeny of Clinical Isolates Based on ARG Presence")
plt.ylabel("Jaccard Distance")
plt.tight_layout()
plt.savefig("arg_matrix_relaxed/clinical_ARG_phylogeny.png")
print("✅ Saved resistance-based phylogeny to clinical_ARG_phylogeny.png")

