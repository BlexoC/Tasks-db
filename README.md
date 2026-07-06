## Database connection
Create a databse connection and then create cursor object to execute SQL commmands
"""Create Tables And Insert Data"""
Creates a table if it does not exist and then create a delete command to clear the table before inserting new data, afterwwards is when data is inserted. Commit the changes to the database by conn.commit()

## Linting By pandas As For Now
Read the data from the database into a pandas DataFrame and then select only the columns we want to keep. The df = df[columns] filters the DataFrame to include only the selected columns and then close the data base connection

## How to Run
Execute this command to view the query result

python3 main.py 



