# KrakenUniq Report Merger

## Introduction
The KrakenUniq Report Merger is a Python tool designed for merging KrakenUniq microbiome analysis reports based on specific taxonomic ranks. This script facilitates the aggregation of KrakenUniq output across multiple samples, allowing for comprehensive comparative analysis.

## Features
- **Multiple File Handling:** Efficiently processes hundreds of files in a single command.
- **Taxonomic Filtering:** Allows merging based on different taxonomic ranks (e.g., Genus, Species).
- **Customizable Output:** Generates a consolidated report tailored to the specific needs of microbial diversity studies.

## Prerequisites
Before you run this script, make sure you have Python installed on your machine. The script is compatible with Python 3.6 or higher. You will also need Pandas library for handling data structures. You can install Python and Pandas using the following commands:

```bash
# Install Python
# Visit https://www.python.org/downloads/ for details based on your Operating System.

# Install Pandas
pip install pandas
```

## Installation
Clone this repository to your local machine to get started with the script:

```bash
git clone https://github.com/yourusername/KrakenUniqReportMerger.git
cd KrakenUniqReportMerger
```

## Usage
Run the script from the command line by navigating to the script directory and using the following command:

```bash
python krakenuniqreportfilemerger.py <directory> <output_file> <rank>
```

### Parameters:
- `<directory>`: This is the path to the directory containing your KrakenUniq report files.
- `<output_file>`: Desired name or path for the output file where the merged data will be saved.
- `<rank>`: Taxonomic rank at which to merge reports (e.g., 'genus', 'species').

### Example:
```bash
python krakenuniqreportfilemerger.py ./data output_merged.txt genus
```

This will merge all report files in the `./data` directory into a single file named `output_merged.txt`, consolidating data at the genus level.

## Contributing
Contributions to enhance KrakenUniq Report Merger are welcome. Please fork the repository and submit a pull request with your enhancements. Make sure to add a brief description of your changes.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support
If you encounter any problems or have suggestions, please open an issue on the GitHub repository.

