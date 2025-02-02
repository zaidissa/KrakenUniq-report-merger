#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 00:38:08 2024

@author: syedzaidi
"""



import pandas as pd
import os
import argparse

def read_and_filter_taxa_names(directory, rank):
    taxa_list = []
    for filename in os.listdir(directory):
        if filename.endswith(("_report", "_report.txt")):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path, sep='\t', header=None, skiprows=3)
            df.columns = ['percent', 'reads', 'taxReads', 'kmers', 'dup', 'cov', 'taxID', 'rank', 'taxName']
            # Create a copy of the filtered DataFrame to avoid SettingWithCopyWarning
            filtered = df[df['rank'] == rank].copy()
            filtered['taxName'] = filtered['taxName'].str.strip()
            taxa_list.extend(filtered[['rank', 'taxName']].drop_duplicates().values.tolist())

    unique_taxa = set(tuple(i) for i in taxa_list)
    return list(unique_taxa)

def merge_read_counts(directory, unique_taxa, rank, output_file):
    unique_taxa_df = pd.DataFrame(unique_taxa, columns=['rank', 'taxName'])
    all_data = unique_taxa_df.copy()

    for filename in os.listdir(directory):
        if filename.endswith(("_report", "_report.txt")):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path, sep='\t', header=None, skiprows=3)
            df.columns = ['percent', 'reads', 'taxReads', 'kmers', 'dup', 'cov', 'taxID', 'rank', 'taxName']
            # Create a copy of the filtered DataFrame to avoid SettingWithCopyWarning
            filtered = df[df['rank'] == rank].copy()
            filtered['taxName'] = filtered['taxName'].str.strip()
            filtered = filtered[['reads', 'rank', 'taxName']]
            merged = pd.merge(unique_taxa_df, filtered, on=['rank', 'taxName'], how='left')
            merged.rename(columns={'reads': filename}, inplace=True)
            all_data = pd.merge(all_data, merged, on=['rank', 'taxName'], how='left')

    all_data.fillna(0, inplace=True)
    # all_data.to_csv(output_file, index=False)
    all_data.to_csv(output_file, index=False, sep='\t')
    print(f"Output has been saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Merge KrakenUniq report files based on a specific taxonomic rank.")
    parser.add_argument('directory', help="Directory containing the report files. Report file names must end with '*_report'")
    parser.add_argument('output_file', help="Output file path/name.txt")
    parser.add_argument('rank', help="Taxonomic rank to filter (e.g., phylum, class, order, family, specie, genus).")
    args = parser.parse_args()

    print("Reading and filtering taxa names...")
    unique_taxa = read_and_filter_taxa_names(args.directory, args.rank)
    print(f"Found {len(unique_taxa)} unique taxa entries at the rank of {args.rank}.")

    print("Merging read counts and writing output...")
    merge_read_counts(args.directory, unique_taxa, args.rank, args.output_file)

if __name__ == "__main__":
    main()



    

