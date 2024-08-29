import pandas as pd
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Process SV and eQTL files.')

# Add arguments for files
parser.add_argument('-s', '--sv-file', type=str, required=True, help='Path to the SV CSV file (e.g., sv_data.csv.gz)')
parser.add_argument('-e', '--eqtl-file', type=str, required=True, help='Path to the eQTL file (e.g., eqtl_table.csv)')

# Parse arguments
args = parser.parse_args()

# Load the SV data from the specified file
sv_data = pd.read_csv(args.sv_file)

# Load the eQTL data from the specified file
eqtl_data = pd.read_csv(args.eqtl_file)

# Display the first few rows of each dataframe to confirm
print("SV Data:")
print(sv_data.head())

print("\neQTL Data:")
print(eqtl_data.head())

