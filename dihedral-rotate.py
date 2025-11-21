#python3 script for rotation of a dihedral by 45 o for population extraction
import pandas as pd
import matplotlib.pyplot as plt

# Input and output file names
input_file = 'combined_output.xlsx'  # Original file
output_file = 'combined_output_rotated.xlsx'  # Transformed file
output_image = 'rotated_scatter.png'  # Scatter plot image

# Step 1: Read original Excel file
df = pd.read_excel(input_file, engine='openpyxl', header=0)

# Ensure columns exist
if df.shape[1] < 4:
    raise ValueError("The Excel file must have at least 4 columns (A-D).")

# Step 2: Extract original values for columns C and D
orig_c = pd.to_numeric(df.iloc[:, 2], errors='coerce')
orig_d = pd.to_numeric(df.iloc[:, 3], errors='coerce')

# Step 3: Compute new values using original data
mask = orig_c.notna() & orig_d.notna()
new_c = orig_c[mask] - orig_d[mask]  # C = original C - original D
new_d = orig_c[mask] + orig_d[mask]  # D = original C + original D

# Update DataFrame
df.loc[mask, df.columns[2]] = new_c
df.loc[mask, df.columns[3]] = new_d

# Step 4: Save updated DataFrame to new Excel file
df.to_excel(output_file, index=False, engine='openpyxl')

# Step 5: Create scatter plot from transformed columns
col_c = pd.to_numeric(df.iloc[:, 2], errors='coerce')
col_d = pd.to_numeric(df.iloc[:, 3], errors='coerce')

mask_plot = col_c.notna() & col_d.notna()
col_c = col_c[mask_plot]
col_d = col_d[mask_plot]

plt.figure(figsize=(8, 6))
plt.scatter(col_c, col_d, color='blue', alpha=0.6)
plt.title('rotated')
plt.xlabel('Column C')
plt.ylabel('Column D')
plt.grid(True)

# Save and show plot
plt.savefig(output_image)
plt.show()

print(f"Excel file '{output_file}' created and scatter plot saved as '{output_image}'.")
