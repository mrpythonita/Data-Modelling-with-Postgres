import os
import glob
import psycopg2
import pandas as pd
#from sql_queries import *

from query2 import *
def process_song_file(cur, filepath):
    
    ''' 
        This function loops through all the song data files
        to insert data in the songs and artists tables.
        
        Keyword arguments:
        cur -- main function object (to perform data insertion)
        filepath -- string (saved files path)
          
        '''
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].copy().values.tolist()[0]
    
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    ''' 
        This function loops through all the log_data files
        to insert data in the time,users, and songplays tables.
        
        Keyword arguments:
        cur -- main function object (to perform data insertion)
        filepath -- string (saved files path)
        
        '''
    # open log file
    df =  df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df = df[df.page == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df["ts"])
    
    # insert time data records
    time_data = (t,t.dt.hour,t.dt.day,t.dt.week,t.dt.month,t.dt.year,t.dt.weekday)
    column_labels = ('timestamp','hour','day','week','month','year','weekday')
    time_dictionary = dict(zip(column_labels, time_data))
    
    #load the data from dataframe
    time_df = pd.DataFrame.from_dict(time_dictionary) 

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]
    user_df = user_df.drop_duplicates()
    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = ( pd.to_datetime(row.ts)
                        ,str(row.userId)
                        ,str(row.level)
                        ,songid
                        ,artistid
                        ,row.sessionId
                        ,str(row.location)
                        ,str(row.userAgent)
                        ) 
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    
    '''
       This function takes a file path and executes data extraction
       for a specific file extension (i.e. JSON)
       
       Keyword arguments:
       cur -- main function object (to perform data insertion)
       filepath -- string (saved files path)
       conn -- main function to connect to the DB
       func -- is an identity_decorator 
       '''
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    ''' 
        This function connects to the SPARKIFY DB and calls
        the process_data function to insert song and log files
        data into the DB'''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()