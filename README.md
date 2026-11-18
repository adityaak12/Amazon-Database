(https://github.com/user-attachments/files/35009475/README.1.md)# Amazon Product Data Analyzer

A beginner-friendly Python mini project that analyzes Amazon product data using **NumPy** and **Pandas**. The project explores product prices, discounts, ratings, categories, and customer reviews, and exports cleaned data and a statistical summary.

## Project Overview

The project uses an Amazon product dataset containing **1,465 records and 16 original columns**. It performs data cleaning and exploratory data analysis to help understand product pricing, discounts, ratings, and category-level information.

## Features

- Load the Amazon dataset from a CSV file.
- Display the dataset dimensions, columns, first records, missing values, and data types.
- Remove duplicate records and clean column names and text values.
- Convert price, discount, rating, and rating-count fields into numeric values.
- Calculate statistical measures such as mean, median, standard deviation, minimum, and maximum.
- Calculate product savings using actual price minus discounted price.
- Display the 10 products with the highest savings.
- Analyze product counts and average ratings by category.
- Search for products by name or keyword.
- Review product rating information.
- Generate a correlation matrix for numeric columns.
- Detect possible outliers using the IQR method.
- Export cleaned data and a descriptive statistical summary as CSV files.

## Technologies Used

- **Python** – programming language
- **NumPy** – numerical computing
- **Pandas** – data loading, cleaning, manipulation, and analysis
- **Jupyter Notebook / JupyterLab** – development environment

## Project Files

```text
Amazon-Product-Data-Analyzer/
│
├── amazon.csv              # Original Amazon product dataset
├── AmazonDatabase.ipynb    # Main project notebook
├── AmazonDatabase.py       # Python script (work in progress)
├── cleaned_data.csv        # Exported cleaned dataset
├── summary.csv             # Descriptive statistical summary
└── README.md               # Project documentation
```

> The Jupyter Notebook (`AmazonDatabase.ipynb`) is the main project file. The current `AmazonDatabase.py` script is incomplete; use the notebook to run the complete analysis.

## Installation

Make sure Python and JupyterLab or Jupyter Notebook are installed.

Install the required libraries:

```bash
pip install numpy pandas jupyterlab
```

## How to Run

1. Download or clone this repository.
2. Keep `amazon.csv` in the same folder as `AmazonDatabase.ipynb`.
3. Open a terminal in the project folder.
4. Start JupyterLab:

   ```bash
   jupyter lab
   ```

5. Open `AmazonDatabase.ipynb`.
6. Run the notebook cells from top to bottom.
7. Enter a product name or keyword when the product-search cell asks for input.

After running the export cell, the notebook creates `cleaned_data.csv` and `summary.csv` in the working directory.

## Analysis Sections

| Section | Description |
|---|---|
| Dataset Overview | Displays dataset size, columns, missing values, duplicates, and data types |
| Data Cleaning | Cleans column names and text, converts numeric fields, and removes duplicates |
| Statistical Analysis | Calculates descriptive statistics for prices, discounts, and ratings |
| Price Analysis | Calculates savings and lists the top 10 products by savings |
| Category Analysis | Counts products and calculates average ratings by category |
| Product Search | Searches product names using a user-entered keyword |
| Rating Analysis | Displays average, highest, and lowest ratings |
| Correlation Analysis | Shows correlations between numeric columns |
| Outlier Detection | Identifies possible outliers using the Interquartile Range (IQR) method |
| Export Reports | Saves cleaned data and a descriptive summary as CSV files |

## Output Files

- **`cleaned_data.csv`** – cleaned dataset with an additional `Savings` column.
- **`summary.csv`** – descriptive statistics generated using `DataFrame.describe()`.

## Formula Used

**Product Savings**

```text
Savings = Actual Price - Discounted Price
```

**IQR Outlier Detection**

```text
IQR = Q3 - Q1

Lower Limit = Q1 - 1.5 * IQR
Upper Limit = Q3 + 1.5 * IQR
```

Values below the lower limit or above the upper limit are flagged as possible outliers.

## Learning Outcomes

Through this project, I practiced:

- Reading and working with CSV datasets.
- Cleaning and preparing real-world data.
- Using NumPy and Pandas for data analysis.
- Applying descriptive statistics.
- Grouping and filtering data.
- Searching and analyzing product information.
- Detecting possible outliers.
- Exporting analysis results into CSV files.

## Future Improvements

- Add data visualizations using Matplotlib and Seaborn.
- Build an interactive dashboard.
- Add more advanced product and category comparisons.
- Improve the command-line interface and reporting.

## Author

**Aditya Kshirsagar**  
B.E. Artificial Intelligence & Data Science Student

---

*This project was developed as a mini project for learning Python-based data analysis.*
