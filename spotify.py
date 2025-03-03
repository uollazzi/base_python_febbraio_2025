from music_manager import MusicManager
from datetime import datetime

m = MusicManager("spotify.db")

m.add_album("Queen", datetime(1973, 7, 13), 2)


artists = m.get_artists()

print("*** ELENCO ARTISTI ***")
for artist in artists:
    print(f"- {artist[1]}")
