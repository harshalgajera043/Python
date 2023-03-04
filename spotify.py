import datetime as dt
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("what date would you like to travel(YYYY-MM-DD): ")


spotify_API_endpoint = "http:example.com"

date_elements = (date.split("-"))
travelling_year = int(date_elements[0])
travelling_month = int(date_elements[1])
travelling_date = int(date_elements[2])

travel_date = dt.date(year=travelling_year, month=travelling_month, day=travelling_date)


URL = f"https://www.billboard.com/charts/hot-100/{travel_date}/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [git.getText().strip() for git in song]  # strip to remove the additional space present in the string.
print(song_list)

# spotify = SpotifyOAuth(client_id=spotify_API_id, client_secret=spotify_API_key, redirect_uri=spotify_API_endpoint,
#                        scope="playlist-modify-private")
# print(spotify.get_access_token())
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_API_id,
        client_secret=spotify_API_key,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
with open("token.txt") as token:
    code = token.read()
    # print(code)

track_link = []
for git in song_list:
    try:
        track = sp.search(git)
    except:
        track_link.append("SONG NOT FOUND")
    else:
        song_addrace = track["tracks"]["items"][0]["uri"]
        track_link.append(song_addrace)
print(track_link)
print(len(track_link))

sp_user = sp.current_user()
user_name = sp_user['uri'].split(":")[2]
print(user_name)

song_playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False)
song_playlist_id = song_playlist["id"]


sp.playlist_add_items(song_playlist_id, track_link)



