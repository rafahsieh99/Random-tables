# Random Tables Generator

A Python script that helps assign students to tables/groups in a balanced way.

## Description

This script takes a CSV file containing student information and automatically assigns them to tables/groups with a balanced number of members. It specifically:
- Reads student data from a CSV file
- Filters for active students
- Randomly assigns students to tables
- Ensures balanced group sizes
- Exports the results to an Excel file

## Requirements

- Python 3.x
- pandas
- openpyxl

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/random-tables.git
cd random-tables
```

2. Install the required packages:
```bash
pip install pandas openpyxl
```

## Usage

1. Prepare your CSV file with student data. The file should have:
   - A column containing student names (column name should include "nombre")
   - A column indicating student status (should contain "Activo" for active students)

2. Run the script:
```bash
python sorteo_mesas.py
```

By default, the script will:
- Look for a file named "alumnos.csv"
- Create groups of 4 students each
- Generate an output file named "mesas.xlsx"

## Customization

You can modify the script parameters by editing the following variables in `sorteo_mesas.py`:
- `miembros_por_mesa`: Number of students per table (default: 4)
- `salida_excel`: Name of the output Excel file (default: "mesas.xlsx")

## License

This project is open source and available under the MIT License.
