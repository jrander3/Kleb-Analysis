import os
import pandas as pd
from glob import glob

# === CONFIGURABLE PARAMETERS ===
blast_dir = "blast_results"
identity_thresh = 80
length_thresh = 50
evalue_thresh = 1e-5

# === COLLECT BLAST HITS ===
arg_hits_per_sample = {}
blast_files = glob(os.path.join(blast_dir, "*_blast.out"))

for file_path in blast_files:
    sample_id = os.path.basename(file_path).replace("_blast.out", "")
    arg_hits = set()

    with open(file_path, "r") as infile:
        for line in infile:
            cols = line.strip().split("\t")
            if len(cols) < 12:
                continue
            pident = float(cols[2])
            length = int(cols[3])
            evalue = float(cols[10])
            sseqid = cols[1]

            if pident >= identity_thresh and length >= length_thresh and evalue <= evalue_thresh:
                arg_hits.add(sseqid)

    arg_hits_per_sample[sample_id] = arg_hits

# === CREATE PRESENCE/ABSENCE MATRIX ===
all_args = sorted(set(arg for hits in arg_hits_per_sample.values() for arg in hits))
matrix = pd.DataFrame(0, index=sorted(arg_hits_per_sample.keys()), columns=all_args)

for sample_id, hits in arg_hits_per_sample.items():
    matrix.loc[sample_id, list(hits)] = 1

# === SAVE MATRIX ===
os.makedirs("arg_matrix_relaxed", exist_ok=True)
matrix.to_csv("arg_matrix_relaxed/arg_presence_absence.csv")
print("✅ ARG presence/absence matrix saved to arg_matrix_relaxed/arg_presence_absence.csv")

