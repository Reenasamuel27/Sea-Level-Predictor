# Sea-Level-Predictor

This project analyzes historical sea level data and predicts future sea level rise through the year 2050. The data comes from the US Environmental Protection Agency and includes measurements from 1880 to 2014.

## 📁 Files

- `sea_level_predictor.py` - Main script that generates the sea level rise plot.
- `main.py` - Runs the `draw_plot()` function and executes unit tests.
- `test_module.py` - Contains unit tests to verify the functionality of your code.
- `epa-sea-level.csv` - Dataset containing global average absolute sea level change data.
- `sea_level_plot.png` - The saved output plot showing historical and predicted sea level rise.

## 📊 What the Code Does

- Imports and reads sea level data using **Pandas**.
- Creates a **scatter plot** of historical sea levels.
- Fits and plots two **lines of best fit**:
  - One using all data from 1880 to 2014.
  - One using data from 2000 to 2014.
- Predicts and visualizes sea level rise through **year 2050** using **SciPy's linear regression**.
- Saves the resulting plot as `sea_level_plot.png`.

## 🛠️ How to Run

1. Make sure you have all dependencies installed:
   ```bash
   pip install pandas matplotlib scipy
Run the project:

bash
Copy
Edit
python main.py
View the output:

Plot image: sea_level_plot.png

Unit test results will appear in the terminal.

📈 Example Output
The plot includes:

A red line predicting sea level rise using data from 1880 to 2014.

A green line predicting sea level rise using data from 2000 to 2014.

📚 Data Source
Title: Global Average Absolute Sea Level Change, 1880-2014

Source: U.S. Environmental Protection Agency (EPA)

Based on data from: CSIRO (2015) and NOAA (2015)
