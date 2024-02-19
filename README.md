# ETL_python

This Python ETL (Extract, Transform, Load) project involves web scraping to retrieve data from a specified webpage and from csv file, followed by transformation and loading of the data into a CSV file and a SQLite database. The project utilizes libraries such as BeautifulSoup, requests, pandas, numpy, and sqlite3.

## Project Overview

The project follows the ETL process:

1. **Extract**: Data is extracted from a webpage using web scraping techniques facilitated by the BeautifulSoup library, and from a csv file using pandas.

2. **Transform**: The extracted data undergoes transformation, including currency conversion based on exchange rates obtained from the CSV file.

3. **Load**: The transformed data is loaded into a CSV file and a SQLite database.

## Project Components

### 1. Extract

The `extract` function retrieves data from a specified URL using web scraping techniques. It targets specific elements on the webpage, extracts relevant information, and constructs a DataFrame.

### 2. Transform

The `transform` function processes the extracted data, including applying currency conversion rates obtained from a CSV file. It calculates values in GBP, EUR, and INR based on the exchange rates.

### 3. Load

The data is loaded into two destinations:

- **CSV File**: The transformed DataFrame is saved to a CSV file specified by `csv_path`.

- **SQLite Database**: The transformed DataFrame is loaded into a SQLite database specified by `db_name` and `table_name`.

## Project Execution

To execute the project:

1. Ensure Python and required libraries are installed.
   ```pip install BeautifulSoup4 requests pandas numpy sqlite3 ```
2. Download the CSV file
   **a- on Linux-like systems** 
      ``` wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv ```
   **b- on Windows**
    ``` Invoke-WebRequest -Uri "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv" -OutFile               "exchange_rate.csv" ```
3. Run the Python script containing the functions.
   ``` python .\etl_largest_banks.py ```
4. Monitor the progress and status messages in the log file `etl_project_log.txt`.

## Files and Dependencies

- **Dependencies**: The project requires libraries such as BeautifulSoup, requests, pandas, numpy, and sqlite3 for web scraping, data processing, and database operations. Ensure these libraries are installed and up-to-date.

- **Input Data**: The project uses a webpage URL (`URL`), a CSV file containing exchange rates (`csv_to_read`), and specifies output paths for CSV files (`csv_path`) and SQLite database (`db_name`, `table_name`).

## Web Scraping

The web scraping process involves extracting data from HTML content retrieved from the specified webpage. BeautifulSoup is used to parse the HTML and navigate through its elements to locate and extract the desired information.

## Credits
This project was inspired by the Coursera certification course Python for Data Science and AI offered by IBM. The course provided valuable guidance and opportunities to practice the ETL (Extract, Transform, Load) process through hands-on projects like this one. Special thanks to the instructors and course creators for their comprehensive content and support, enabling learners to acquire essential skills in data manipulation and analysis.

## Conclusion

This Python ETL project demonstrates the integration of web scraping techniques with data processing and database operations. It provides a comprehensive approach to extracting, transforming, and loading data from web sources into structured formats. The project serves as a foundation for automating similar data processing tasks and can be customized to suit specific requirements.
