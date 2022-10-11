# Sparkify Postgres ETL

## Details
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 
The analytics team is particularly interested in understanding what songs users are listening to. 
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

---------------Your role is to create a database schema and ETL pipeline for this analysis-----------------------
### Data
- **Song datasets**: all json files are nested in subdirectories under */data/song_data*. A sample of this files is:

```{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

- **Log datasets**: all json files are nested in subdirectories under */data/log_data*. A sample of a single row of each files is:

```{"artist":"Slipknot","auth":"LoggedIn","firstName":"Aiden","gender":"M","itemInSession":0,"lastName":"Ramirez","length":192.57424,"level":"paid","location":"New York-Newark-Jersey City, NY-NJ-PA","method":"PUT","page":"NextSong","registration":1540283578796.0,"sessionId":19,"song":"Opium Of The People (Album Version)","status":200,"ts":1541639510796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.1) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"20"}
```

## Schema

#### Fact Table
**songplays** - records in log data associated with song plays i.e. records with page NextSong

#### Dimension Tables
**users** - users in the app
**songs** - songs in music database
**artists** - artists in music database
**time** - timestamps of records in songplays broken down into specific units


## files structure

**test.ipynb**- displays the first few rows of each table to let you check your database.

**create_tables.py**- drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.

**etl.ipynb**- reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.

**etl.py**- reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.

**sql_queries.py**- contains all your sql queries, and is imported into the last three files above.
README.md provides discussion on your project.

## steps to run this project
**Create Tables**
1] Write CREATE statements in sql_queries.py to create each table.
2] Write DROP statements in sql_queries.py to drop each table if it exists.
3] Run create_tables.py to create your database and tables.
4] Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook

**Build ETL Processes**

Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.

**Build ETL Pipeline**

Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.