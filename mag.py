#!/opt/conda/miniconda/3-python3.9.13/bin/python3.9
import re
import csv

# Open the OUTCAR file
with open('OUTCAR', 'r') as f:
    outcar_lines = f.readlines()

# Open the POSCAR file
with open('POSCAR', 'r') as f:
    poscar_lines = f.readlines()

# Get the atomic species and numbers from the POSCAR file
species = poscar_lines[5].split()
numbers = list(map(int, poscar_lines[6].split()))

# Create a list of atomic species
atoms = [atom for atom, number in zip(species, numbers) for _ in range(number)]

# Find the line numbers of "magnetization (x)"
indices = [i for i, line in enumerate(outcar_lines) if "magnetization (x)" in line]

# Get the lines for the last occurrence
last_mag = outcar_lines[indices[-1]:]

# Extract the magnetization for each atom
mag = []
for line in last_mag:
    if re.match(r'\s+\d+', line):
        mag.append(list(map(float, line.split())))

# Write to a CSV file
with open('mag.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Atom', 'Species', 's', 'p', 'd', 'Total'])
    for i, (atom, m) in enumerate(zip(atoms, mag), start=1):
        writer.writerow([i, atom] + m)
