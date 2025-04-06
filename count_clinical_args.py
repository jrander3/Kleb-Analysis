import pandas as pd
import matplotlib.pyplot as plt

# === Load matrix ===
df = pd.read_csv("arg_matrix_relaxed/clinical_only_matrix.csv", index_col=0)

# === Count number of ARGs per isolate ===
arg_totals = df.sum(axis=1).sort_values(ascending=False)

# === Save to file ===
arg_totals.to_csv("arg_matrix_relaxed/clinical_ARG_counts.csv", header=["num_args"])

# === Plot ===
plt.figure(figsize=(12, 5))
arg_totals.plot(kind='bar')
plt.ylabel("Number of Resistance Genes")
plt.xlabel("Clinical Isolate")
plt.title("Total Resistance Genes per Clinical Klebsiella Isolate")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("arg_matrix_relaxed/clinical_ARG_counts.png")
print("✅ Saved ARG counts to clinical_ARG_counts.csv and clinical_ARG_counts.png")

