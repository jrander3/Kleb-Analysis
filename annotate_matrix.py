import pandas as pd
import os

# === FILE LOCATIONS ===
matrix_file = "arg_matrix/arg_presence_absence.csv"
aro_index_file = "CARD/aro_index.tsv"

# === LOAD DATA ===
df = pd.read_csv(matrix_file, index_col=0)
aro_index = pd.read_csv(aro_index_file, sep="\t")

# === MAP ARO IDs to Gene Names ===
protein_to_name = dict(zip(aro_index['Protein Accession'], aro_index['ARO Name']))

# Replace column headers
df.columns = [protein_to_name.get(col, col) for col in df.columns]

# === SAVE ANNOTATED MATRIX ===
df.to_csv("arg_matrix/arg_matrix_annotated.csv")
print("✅ Annotated matrix saved to arg_matrix/arg_matrix_annotated.csv")

