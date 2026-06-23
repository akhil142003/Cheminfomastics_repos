# Molecular Weight Filter

A Python tool that processes PubChem CSV files and separates chemical compounds based on molecular weight threshold.

## Features

- Reads PubChem CSV files
- Filters compounds by nolecular weight (default : 300 g/mol)
- Saves results to text files
- Shows sorted compounds, heaviest/lightest and average weight
- Handles errors gracefully

## How to use

1. Download a CSV file from PubChem
2. Run the script:
3. Enter the CSV filename with path when prompted
4. Check the output files: 'light_drugs.txt', 'heavy_drugs.txt' and 'sorted_drugs.txt'

## Example output

Enter the CSV filename with path : "C:\Users\HP\Downloads\AkhiL\Cheminfomatics_repos\PubChem_compound_aspirin.csv"

Processing : C:\Users\HP\Downloads\AkhiL\Cheminfomatics_repos\PubChem_compound_aspirin.csv....
Complete!
Light Compounds (<300 g/mol): 45
Heavy Compounds (>=300 g/mol): 98

Check 'light_drugs.txt' and 'heavy_drugs.txt' for results.
Check 'sorted_drugs.txt' for sorted list of compounds.
==================================================

Heaviest : Bayro vas : (1504.7) g/mol
Lightest : 4-Hydroxybutanal : (88.11)g/mol
Average molecular weight : 396.92 g/mol
-----------Analysis complete----------

## requirements

- Python 3.x
- No external libraries needed

## Author

Akhil Kumar
Github: akhil142003
