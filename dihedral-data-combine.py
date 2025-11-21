#python3 script for combining csv dihedral text into one excel spreadsheet

import pandas as pd

# Load the space-separated text file and set the first column as index
data_txt = pd.read_csv("crest.energies", sep=r"\s+", header=None, names=["Index", "Value"])
data_txt.set_index("Index", inplace=True)

# Load the CSV files
phi_csv = pd.read_csv("crest_conformers.xyz_dihedrals-phi.csv", header=None, names=["Phi"])
psi_csv = pd.read_csv("crest_conformers.xyz_dihedrals-psi.csv", header=None, names=["Psi"])

# Ensure the indices match for proper alignment
phi_csv.index = data_txt.index
psi_csv.index = data_txt.index

# Combine all data into one DataFrame
combined_df = pd.concat([data_txt, phi_csv, psi_csv], axis=1)

# Export the combined DataFrame to an Excel file
combined_df.to_excel("combined_output.xlsx", index=True)

print("The data has been successfully combined and saved to 'combined_output.xlsx'.")
