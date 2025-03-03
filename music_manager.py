import sqlite3


class MusicManager:
    def __init__(self, db_path):
        # TODO: creare le tabelle se non esistenti
        self.db_path = db_path

    def add_artist(self, name, year_since):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                """
                INSERT INTO artists (name, year_since)
                VALUES (?, ?)
                """,
                (name, year_since),
            )

    # TODO: aggiungere la possibilità di cercare
    def get_artists(self):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                """
                SELECT * FROM artists
                """
            ).fetchall()

    def add_album(self, title, release_date, artist_id):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                """
                INSERT INTO albums (title, release_date, artist_id)
                VALUES (?, ?, ?)
                """,
                (title, release_date.timestamp(), artist_id),
            )
