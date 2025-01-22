# Interactive Data Visualizer

A Streamlit web application that allows users to upload CSV files, filter data, and create interactive visualizations.

## Features

- CSV file upload
- Interactive data filtering:
  - Numeric columns: Range, Greater than, Less than, and Equals filters
  - Text/Categorical columns: Multi-select filters
- Multiple visualization options:
  - Scatter plots
  - Line charts
  - Bar charts
  - Pie charts
- Dynamic data preview
- Interactive chart customization

## Installation

1. Clone this repository
2. Install the required packages:


pip install streamlit pandas plotly


## Usage

1. Run the application:


streamlit run app.py


2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload a CSV file using the file uploader

4. Use the sidebar to select visualization options:
   - Choose columns for X and Y axes
   - Select the desired chart type

5. Use the filtering options to explore specific data ranges or categories

## Requirements

- Python 3.6+
- Streamlit
- Pandas
- Plotly Express

## File Structure

- `app.py`: Main application file
- `charts.py`: Chart creation utilities"# data-vis-ver-2" 
