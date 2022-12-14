# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs "
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create =("""
    CREATE TABLE IF NOT EXISTS songplays
    (
        songplay_id serial primary key ,
        start_time timestamp references time(start_time),
        user_id int references users(user_id),
        level varchar,
        song_id varchar references songs(song_id) ,
        artist_id varchar references artists(artist_id),
        session_id int,
        location text,
        user_agent text
    )
""")

user_table_create = (""" 
    CREATE TABLE IF NOT EXISTS users
    (
        user_id int primary key, 
        first_name varchar, 
        last_name varchar, 
        gender varchar,
        level varchar
    )
""")

song_table_create = (""" 
    CREATE TABLE IF NOT EXISTS songs
    (
        song_id varchar primary key,
        title text not null, 
        artist_id varchar not null, 
        year int,
        duration float not null 
    )
""")

artist_table_create = (""" 
    CREATE TABLE IF NOT EXISTS artists
    (
        artist_id varchar primary key,
        name varchar, 
        location text, 
        latitude float, 
        longitude float
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (
        start_time TIMESTAMP PRIMARY KEY,
        hour int, 
        day int, 
        week int, 
        month int, 
        year int, 
        weekday varchar
    )
""")

# INSERT RECORDS
songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
     ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING
""")
# FIND SONGS

song_select = ("""
    select song_id, artists.artist_id
    from songs join artists on songs.artist_id = artists.artist_id
    WHERE songs.title = %s and artists.name = %s and songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

