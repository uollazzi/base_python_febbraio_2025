from music_manager import MusicManager
from datetime import datetime


def main():
    m = MusicManager("spotify.db")

    # m.add_artist("Queen", 1963)
    # m.add_album("Queen", datetime(1973, 7, 13), 1)

    artists = m.get_artists("Queen")

    print("*** ELENCO ARTISTI ***")
    for artist in artists:
        print(f"- {artist[1]}")


# variabili dunder __main__
if __name__ == "__main__":
    main()
