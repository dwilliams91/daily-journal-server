import json
import sqlite3
from models import HashTag

def get_all_hashtags():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory=sqlite3.Row
        db_cursor =conn.cursor()

        db_cursor.execute("""
        SELECT 
            h.id,
            h.tag
        FROM HashTags h
        """)

        hashtags=[]

        dataset=db_cursor.fetchall()

        for row in dataset:
            hashtag=HashTag(row['id'], row['tag'])
            hashtags.append(hashtag.__dict__)
        
    return json.dumps(hashtags)

def create_hashtag(new_hashtag):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor=conn.cursor()
        
        id= db_cursor.lastrowid

        db_cursor.execute("""
        INSERT INTO HashTags
            ( tag, id )
        VALUES
            ( ?, ? );
        """, (new_hashtag['hashtag_id'], id))

    return json.dumps(new_hashtag)