#python3 script for plotting the ensemble on a scatter plot
# two arguements are require: 1) the number of conformers to be plotted, & 2) the number of conformers to be labelled, starting with the lowest energy

import pandas as pd
import matplotlib.pyplot as plt

from adjustText import adjust_text
import numpy as np

import sys

# === LOAD DATA ===
file_path = 'combined_output.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')
df.columns = [col.strip() for col in df.columns]

# === COMMAND-LINE ARGUMENTS ===
if len(sys.argv) != 3:
    print("Usage: python3 script.py <number_of_rows> <number_of_points>")
    sys.exit(1)

try:
    number_of_rows = int(sys.argv[1])
    number_of_points = int(sys.argv[2])
except ValueError:
    print("Please provide valid integers for both arguments.")
    sys.exit(1)

# === PROCESS DATA ===
df_plot = df.head(number_of_rows).iloc[::-1].reset_index(drop=True)
df_annotate = df.head(number_of_points).reset_index(drop=True)

# === PLOT ===
plt.figure(figsize=(10, 8))

# Combine both datasets for consistent coloring
combined_df = pd.concat([df_plot, df_annotate], ignore_index=True)

# Create a single scatter plot
scatter = plt.scatter(combined_df['Phi'], combined_df['Psi'], c=combined_df['Value'], cmap='plasma')

plt.colorbar(scatter, label='Relative Energies (kcal/mol)')
plt.xlabel("φ (deg.) [C1-C2-C3-C4]")
plt.ylabel("ψ (deg.) [C2-C3-C4-C5]")
plt.xlim(-180, 180)
plt.ylim(-180, 180)
plt.xticks(range(-180, 181, 60))
plt.yticks(range(-180, 181, 60))
plt.grid(True)

# Annotate selected points using arrows
texts = []
for i in range(len(df_annotate)):
    label = f"Conf.: {df_annotate['Index'].iloc[i]}"
    x = df_annotate['Phi'].iloc[i]
    y = df_annotate['Psi'].iloc[i]
    texts.append(
        plt.text(
            x, y, label,
            fontsize=12,
            color='black',
            ha='center',
            va='bottom'
        )
    )

# Automatically adjust to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle="->", color='blue'))


plt.tight_layout()
filename = f"scatter_plot_{number_of_rows}-conf_{number_of_points}-labelled.png"
plt.savefig(filename)
plt.show()
