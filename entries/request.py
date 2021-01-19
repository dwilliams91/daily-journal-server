import json
import sqlite3
from models import Entry

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            j.id,
            j.date,
            j.topic, 
            j.entry,
            j.mood_id
        FROM Journal_Entries j
        """)

        journalentries=[]

        dataset= db_cursor.fetchall()

        for row in dataset:
            journalentry= Entry(row['id'], row['date'], row['topic'], row['entry'], row['mood_id'])
            journalentries.append(journalentry.__dict__)

    return json.dumps(journalentries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            j.id,
            j.date,
            j.topic,
            j.entry,
            j.mood_id
        FROM Journal_Entries j
        WHERE j.id=?
        """, (id,))

        data=db_cursor.fetchone()

        entry=Entry(data['id'], data['date'], data['topic'], data['entry'], data['mood_id'])

    return json.dumps(entry.__dict__)

def delete_entry(id):
     with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Journal_Entries
        WHERE id = ?
        """, (id, ))