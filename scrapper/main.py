from dotenv import load_dotenv
import os
from websites.ville_data import VilleDataHandler


load_dotenv()

env = "prod"

websites={"ville_data":"https://ville-data.com/terrain-de-petanque/"}

if __name__ == "__main__":
    
    ville_data = VilleDataHandler(driver_path=os.environ.get("DRIVER_PATH"), url=websites["ville_data"])
    ville_data.get_terrain_urls()
    
    # if env == "prod":
    #     bestsellers = boomkat.get_bestsellers_list()
    # if env == "dev":
    #     bestsellers = [
    #         "Moritz Von Oswald Trio Dissent",
    #         "Bendik Giske Cracks",
    #         "Felisha Ledesma Fringe",
    #         "Dijit Tapes & Krikor Remixes",
    #         "Ultravillage Elements",
    #         "THE CARETAKER Everywhere At The End Of Time Stages 1-3 (Vinyl Set)",
    #         "LUC FERRARI Labyrinthe de Violence",
    #     ]
    # spotify = SpotifyHandler()

    # albums = spotify.get_albums_urls(bestsellers)

    # albums_with_tracks = spotify.get_albums_tracks(albums)
    # spotify.create_playlist(albums_with_tracks, "test_api")