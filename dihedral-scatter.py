import pandas as pd
import matplotlib.pyplot as plt
import sys

# Check for command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 script.py <number_of_rows>")
    sys.exit(1)

# Parse number of rows
try:
    num_rows = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer for the number of rows.")
    sys.exit(1)

# Load Excel file (skip first row)
file_path = 'combined_output.xlsx'  # Replace with your actual file name
df = pd.read_excel(file_path, engine='openpyxl', skiprows=1)

# Limit to specified number of rows and reverse the order
df = df.head(num_rows).iloc[::-1]

# Extract columns
x = df.iloc[:, 2]  # Column 3 becomes x-axis
y = df.iloc[:, 3]  # Column 4 becomes y-axis
colors = df.iloc[:, 1]  # Column 2 for colormap


# Plot
plt.figure(figsize=(7, 6))
scatter = plt.scatter(x, y, c=colors, cmap='plasma')
plt.colorbar(scatter, label='Relative Energies (kcal/mol)')  
plt.xlabel("φ (deg.) [C1-C2-C3-C4]")
plt.ylabel("ψ (deg.) [C2-C3-C4-C5]")
plt.xlim(-180, 180)
plt.ylim(-180, 180)
plt.xticks(range(-180, 181, 60))
plt.yticks(range(-180, 181, 60))
plt.grid(True)
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.show()
