import sqlite3


class MusicManager:
    def __init__(self, db_path):
        self.db_path = db_path

        with sqlite3.connect(db_path) as conn:
            sql_artists = """
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER NOT NULL,
                name TEXT NOT NULL,
                year_since INTEGER NOT NULL,
                CONSTRAINT artists_pk PRIMARY KEY (id)
            );
            """
            conn.execute(sql_artists)

            sql_albums = """
            CREATE TABLE IF NOT EXISTS albums (
                id INTEGER NOT NULL,
                title TEXT NOT NULL,
                release_date INTEGER NOT NULL,
                artist_id INTEGER NOT NULL,
                CONSTRAINT albums_pk PRIMARY KEY (id),
                CONSTRAINT albums_artists_FK FOREIGN KEY (artist_id) REFERENCES artists(id)
            );
            """
            conn.execute(sql_albums)

    def add_artist(self, name, year_since):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                """
                INSERT INTO artists (name, year_since)
                VALUES (?, ?)
                """,
                (name, year_since),
            )

    def get_artists(self, search=""):
        with sqlite3.connect(self.db_path) as conn:

            if search != "":
                sql = "SELECT * FROM artists WHERE name LIKE ?"
                return conn.execute(sql, (f"%{search}%",)).fetchall()  # %Queen%
            else:
                sql = "SELECT * FROM artists"
                return conn.execute(sql).fetchall()

    def add_album(self, title, release_date, artist_id):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                """
                INSERT INTO albums (title, release_date, artist_id)
                VALUES (?, ?, ?)
                """,
                (title, release_date.timestamp(), artist_id),
            )
