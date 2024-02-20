# ETL_python

This Python ETL (Extract, Transform, Load) project involves web scraping to retrieve data from a specified webpage and from csv file, followed by transformation and loading of the data into a CSV file and a SQLite database. The project utilizes libraries such as BeautifulSoup, requests, pandas, numpy, and sqlite3.

## Project Overview

The project implements an ETL (Extract, Transform, Load) process to gather data from both web sources and CSV files. Utilizing web scraping with BeautifulSoup and pandas, the Extract phase collects relevant information from a webpage and a CSV file. Following extraction, the Transform phase modifies the data, including currency conversion based on exchange rates from the CSV file. Finally, in the Load phase, the transformed data is stored in both a CSV file and a SQLite database. This comprehensive approach ensures efficient handling and utilization of diverse data sources for further analysis and utilization.

## Project Execution

To execute the project:

1. Ensure Python and required libraries are installed.
   ```pip install BeautifulSoup4 requests pandas numpy sqlite3 ```
2. Download the CSV file

   **a- on Linux-like systems**
   
      ``` wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv ```

   **b- on Windows**
   
      ``` Invoke-WebRequest -Uri "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv" -OutFile               "exchange_rate.csv" ```
4. Run the Python script containing the functions.

      ``` python .\etl_largest_banks.py ```
5. Monitor the progress and status messages in the log file `etl_project_log.txt`.

## Files and Dependencies

- **Dependencies**: The project requires libraries such as BeautifulSoup, requests, pandas, numpy, and sqlite3 for web scraping, data processing, and database operations. Ensure these libraries are installed and up-to-date.

- **Input Data**: The project uses a webpage URL (`URL`), a CSV file containing exchange rates (`csv_to_read`), and specifies output paths for CSV files (`csv_path`) and SQLite database (`db_name`, `table_name`).

## Credits
This project was a part of Coursera IBM Data Engineering Certification : [https://www.coursera.org/learn/python-project-for-data-engineering/]


