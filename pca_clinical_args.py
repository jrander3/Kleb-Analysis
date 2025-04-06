import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# === Load matrix ===
df = pd.read_csv("arg_matrix_relaxed/clinical_only_matrix.csv", index_col=0)

# === Standardize (not strictly necessary for binary, but consistent) ===
X = StandardScaler().fit_transform(df)

# === PCA ===
pca = PCA(n_components=2)
components = pca.fit_transform(X)

# === Create PCA DataFrame ===
pca_df = pd.DataFrame(components, columns=["PC1", "PC2"], index=df.index)

# === Save PCA coordinates ===
pca_df.to_csv("arg_matrix_relaxed/clinical_ARG_PCA.csv")

# === Plot ===
plt.figure(figsize=(8, 6))
plt.scatter(pca_df["PC1"], pca_df["PC2"], s=40)
plt.title("PCA of Clinical Isolates Based on ARG Profiles")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("arg_matrix_relaxed/clinical_ARG_PCA_plot.png")
print("✅ PCA complete. Saved to clinical_ARG_PCA.csv and clinical_ARG_PCA_plot.png")

