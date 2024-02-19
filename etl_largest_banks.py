from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 


tab_attribs = ["Name","MC_USD_Billion"]
URL="https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
csv_path="./Largest_banks_data.csv"
csv_to_read='./exchange_rate.csv'
db_name="Banks.db"
table_name="Largest_banks"

#log function
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')   


def extract(url, table_attribs):
    page=requests.get(url).text
    data=BeautifulSoup(page,'html.parser')
    df=pd.DataFrame(columns=table_attribs)
    tabs=data.find_all('tbody')
    rows=tabs[0].find_all('tr')
    for row in rows:
        col=row.find_all('td')
        if len(col)>=3:
            if col[1].find('a') is not None:
                data_dict = {"Name": [col[1].text.strip()],
                             "MC_USD_Billion": [float(col[2].contents[0])]}
                df1 = pd.DataFrame(data_dict)
                df = pd.concat([df,df1], ignore_index=True)
    return df

log_progress('Preliminaries complete. Initiating ETL process')
df = extract(URL, tab_attribs)
print(df)
log_progress('Data extraction complete.')


def transform(df,csv_path):
    #create the dictionnary currency/rate
    exchange_rate = pd.read_csv(csv_path)
    dict =exchange_rate.set_index('Currency').to_dict()['Rate']
    #add columns and their values to the df
    df['MC_GBP_Billion'] = [np.round(x*dict['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*dict['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*dict['INR'],2) for x in df['MC_USD_Billion']]
    return df

log_progress('Initiating Transformation process')
df = transform(df,csv_to_read)
print(df)
log_progress('Data transformation complete')

# print(transform(extract(URL,tab_attribs),csv_to_read))
def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

log_progress('Initiating loading process')
load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

log_progress('SQL Connection initiated.')

sql_connection = sqlite3.connect('Banks.db')
def load_to_db(df, sql_connection, table_name):

    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table.')


def run_queries(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

log_progress('Running the query')

run_queries('SELECT * FROM Largest_banks', sql_connection)
run_queries('SELECT AVG(MC_GBP_Billion) FROM Largest_banks', sql_connection)
run_queries('SELECT Name from Largest_banks LIMIT 5', sql_connection)

sql_connection.close()
log_progress('Process Complete.sql connection closed')