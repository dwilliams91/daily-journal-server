import json
import sqlite3
from models import Mood

def get_all_moods():
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.mood
        FROM Moods m
        """)

        moods=[]

        dataset= db_cursor.fetchall()

        for row in dataset:
            mood= Mood(row['id'], row['mood'])
            moods.append(mood.__dict__)

    return json.dumps(moods)