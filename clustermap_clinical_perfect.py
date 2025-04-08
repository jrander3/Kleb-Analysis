import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

# === Load data ===
input_path = sys.argv[1]
df = pd.read_csv(input_path, index_col=0)

# === Generate clustermap ===
sns.set(context='notebook', style='white')
g = sns.clustermap(df, cmap="viridis", figsize=(14, 12), col_cluster=False)

# === Save output ===
out_dir = os.path.dirname(input_path)
out_path = os.path.join(out_dir, "clinical_clustermap_perfect.png")
plt.savefig(out_path, dpi=300)
plt.close()
print(f"🌟 Clustermap saved to {out_path}")

