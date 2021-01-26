# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id serial PRIMARY KEY
    ,start_time timestamp NOT NULL
    ,user_id varchar(50) NOT NULL
    ,level varchar(100)
    ,song_id varchar(50)
    ,artist_id varchar(50)
    ,session_id int
    ,location varchar
    ,user_agent varchar
)
""")


user_table_create = ("""
CREATE TABLE users(
    user_id varchar(50) PRIMARY KEY
    ,first_name varchar(50)
    ,last_name varchar(50)
    ,gender varchar(10)
    ,level varchar(50)
)
""")


song_table_create = ("""
CREATE TABLE songs(
    song_id varchar PRIMARY KEY
    ,title varchar
    ,artist_id varchar
    ,year int
    ,duration float
)
""")


artist_table_create = ("""
CREATE TABLE artists(
    artist_id varchar PRIMARY KEY
    ,artist_name varchar
    ,artist_location varchar
    ,artist_latitude float
    ,artist_longitude float
)
""")


time_table_create = ("""
CREATE TABLE time(
    start_time timestamp PRIMARY KEY
    ,hour int
    ,day int
    ,week int
    ,month int
    ,year int 
    ,weekday int
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(
    start_time
    ,user_id
    ,level
    ,song_id 
    ,artist_id
    ,session_id
    ,location
    ,user_agent
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users(
    user_id
    ,first_name
    ,last_name
    ,gender
    ,level
)
VALUES(%s,%s,%s,%s,%s)
on conflict(user_id) DO UPDATE SET level= excluded.level
""")

song_table_insert = ("""
INSERT INTO songs(
    song_id 
    ,title
    ,artist_id
    ,year
    ,duration
)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists(
    artist_id
    ,artist_name
    ,artist_location
    ,artist_latitude
    ,artist_longitude
)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time(
    start_time
    ,hour
    ,day
    ,week
    ,month
    ,year
    ,weekday
)
VALUES(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT  s.song_id
        ,s.artist_id
FROM    songs s
        JOIN artists a
            ON s.artist_id = a.artist_id
WHERE   s.title = %s
        AND a.artist_name = %s
        AND s.duration = %s
            
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]