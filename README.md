# Data Modelling with Postgres

This project focuses on modelling data with Postgress for a made up music streaming company named Sparkify.

## Getting Started

There are two datasets available for this project (Log Data and Songs Data) and they are both JSON files. This project leverages on Python, SQL, and PostgreSQL to creating an ETL pipeline to ingest song and user data into a Postgres DB.

## Schema

The Sparkify Database  uses a star schema optimized for queries on song play analysis which includes the following tables:
### Fact Table
* __songplays__ - records in log data associated with song plays i.e. records with page NextSong (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

### Dimension Tables
* __users__ - users in the app (user_id, first_name, last_name, gender, level)
* __songs__ - songs in music database (song_id, title, artist_id, year, duration)
* __artists__ - artists in music database (artist_id, name, location, latitude, longitude)
* __time__ - timestamp of records in songplays broken down into specific units (start_time, hour, day, week, month, year, weekday)

## Prerequisites

Python 3 is the environment utilized with the addition of the following libraries:

* __postgresql__ (+ dependencies) 
* __jupyter__ (+ dependencies) 

## Installing

```
import os
import glob
import psycopg2
import pandas as pd
from query2 import *
```

## Deployment

* **etl.ipynb**: Jupyter Notebook for creating/testing the core logic implemented in etl.py file.
* **test.ipynb**: Jupyter Notebook for testing the accuracy of SQL queries.
* **create_tables.py**: This file drops and creates your tables. It is executed to reset tables before each time ETL script is run.
* **etl.py**: This file reads and processes a single file from song_data and log_data and loads the data into the tables. 
* **sql_queries.py**: Contains the data description language (DDL) syntax for creation/dropping of table as well as the data manipulation language (DML) for inserting data.


### _Acknowledgments_

* Chapeau to StackOverflow, GitHub, and Udacity Knowledge platforms for providing some guidance code.
