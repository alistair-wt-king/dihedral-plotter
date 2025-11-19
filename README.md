# dihedral-plotter
A set of python scripts to create Ramachandran plots from CREST-xTB '-entropy- search outputs

The initial dihedral extraction is based on 'https://github.com/dsvatunek/dihedral'

In total the scripts require 'python3, 'numpy', 'pandas', 'matplotlib', 'openpyxl' & 'adjustText'.


**Usage**:

**Step 1** - Make a record of the atom numbers you wish to use for your Ramachandran plot dihedrals


The saccharide torsion angles are defined as ϕ = C1-C2-C3-C4, and ψ= C2-C3-C4-C5
for .xyz files. For examples:
ϕ (phi)
12,7,9,16 (Avogadro)
ψ (psi)
7,9,16,17 (Avogadro)


**Step 2** - Copy the crest outputs 'crest.energies' and 'crest_conformers.xyz' into your working directory

**Step 3** - execute 'python3 dihedral-glyco-phi.py'
**Step 4** - execute 'python3 dihedral-glyco-phi.py'

**Step 5** - execute 'python3 dihedral-data-combine.py'

**Step 6** - execute 'python3 dihedral-scatter.py arg1' where 'arg1' is the number of conformers that you wish to plot, based on the .csv output created in the previous steps.

with 'python3 dihedral-scatter-labels.py arg1 arg2', 'arg1' is the same as for the previous script but 'arg2' is the number of low energy conformers that you wish to label on the plot.

