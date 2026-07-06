## Database Connection
Create a database connection, then create a cursor object to execute SQL commands.

## Create Table and Insert Data
Create the table if it doesn't already exist, then run a DELETE command to clear out old data before inserting new rows — this keeps the script idempotent, so running it multiple times won't create duplicates. Finally, commit the changes with `conn.commit()`.

## View Data with pandas
Read the data from the database into a pandas DataFrame, then filter it down to only the columns you want using `df = df[columns]`. Close the database connection once you're done.

## How to Run
Run the following command to execute the script and view the results:

```bash
python3 main.py
```

