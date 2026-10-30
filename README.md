# 🛒 Amazon Product Data Analyzer

## 📌 About the Project

The **Amazon Product Data Analyzer** is a beginner-friendly data analysis project developed using Python, NumPy, and Pandas in JupyterLab.

This project analyzes Amazon product data to explore prices, discounts, ratings, and product categories. It demonstrates fundamental data analysis techniques and statistical calculations using real-world data.

## 🛠️ Technologies Used

- **Python** — Programming logic and data processing
- **NumPy** — Numerical and statistical calculations
- **Pandas** — Data cleaning, manipulation, and analysis
- **JupyterLab** — Interactive coding environment

## ✨ Features

- **Dataset Overview:** Displays the dataset's rows, columns, data types, missing values, and duplicate records.
- **Data Cleaning:** Removes duplicate records and prepares numeric columns for analysis.
- **Statistical Analysis:** Calculates mean, median, standard deviation, minimum, and maximum using NumPy.
- **Price Analysis:** Compares actual prices with discounted prices and calculates estimated savings.
- **Category Analysis:** Counts products by category and calculates average ratings.
- **Product Search:** Searches for products using names or keywords.
- **Rating Analysis:** Examines product ratings and identifies highly rated products.
- **Correlation Analysis:** Explores relationships between numeric columns.
- **Outlier Detection:** Uses the Interquartile Range (IQR) method to identify unusual values.
- **Report Generation:** Exports cleaned data and descriptive statistics into CSV files.

## 📂 Project Structure

```text
Amazon-Database/
│
├── AmazonDatabase.ipynb
├── amazon.csv
└── README.md
```

- `AmazonDatabase.ipynb` — Jupyter Notebook containing the project code.
- `amazon.csv` — Dataset used for analysis.
- `README.md` — Project documentation.

The program can also generate `cleaned_data.csv` and `summary.csv` when the report-exporting feature is executed.

## 📊 Dataset

This project uses an Amazon product dataset available on Kaggle.

**Dataset source:**  
https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset

Download the dataset and place the CSV file in the project directory. Make sure its filename matches the one used in the notebook.

## ⚙️ Installation

Install the required libraries using:

```bash
pip install numpy pandas
```

## 🚀 How to Run

1. Download or clone this repository.
2. Open JupyterLab.
3. Open `AmazonDatabase.ipynb`.
4. Make sure `amazon.csv` is available in the same folder.
5. Run the notebook cells in order.
6. Explore the analysis results.

## 🧠 Concepts Learned

- Python programming
- NumPy arrays and statistical operations
- Pandas DataFrames and Series
- Data cleaning and preprocessing
- Data filtering and grouping
- Exploratory Data Analysis (EDA)
- Correlation analysis
- Outlier detection using IQR
- CSV file handling
- Data interpretation

## ⚠️ Limitations

- Results depend on the dataset's quality and available columns.
- Listed prices and ratings may not reflect current Amazon information.
- Price differences do not represent verified sales, revenue, or profit.
- Correlation does not necessarily imply causation.

## 🔮 Future Improvements

- Add more detailed product comparisons.
- Improve missing-value handling.
- Analyze relationships between ratings and discounts.
- Support additional product datasets.
- Build an interactive dashboard in a future version.

## 👨‍💻 Author

**Aditya Kshirsagar**

Aspiring Data Science and AI/ML professional interested in Python programming and data analysis.

---

⭐ If you find this project useful, consider giving the repository a star!
