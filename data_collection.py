import pandas as pd
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Process a VCF file.')

# Add argument for file
parser.add_argument('-f', '--file', type=str, required=True, help='Path to the VCF file (e.g., supporting_variants_for_nstd186.csv.gz)')

# Parse arguments
args = parser.parse_args()

# Load the data from the specified file
vcf_data = pd.read_csv(args.file)

# Display the first few rows of the data
print(vcf_data.head())

