import json
import requests
from secrets import spotify_user_id
class translatePlaylist:

	def __init__(self):
		self.user_id = spotify_user_id
		self.spotify_token = spotify_token

	#am == apple music
	#Step 1: Get apple music user
	def get_am_client(self):
		pass

	#Step 2: Find the playlist you want to copy
	def get_am_playlist(self):
		pass

	#Step 3: Crete a new spotify playlist
	def create_spotify_playlist(self):
		
		request_body = json.dumps({
			"name":""
		})

		query = "https://api.spotify.com/v1/users/{user_id}/playlists".format(self.user_id)
		response = requests.post(
			query,
			data=request_body,
			headers={
				"Content-Type":"application/jason",
				"Authorization": "Bearer {}".format(spotify_token)
			}
		)
		response_json = response.json()

		#playlist_id 
		return response_json["id"]

	#Step 4: Search for the song
	def get_spotify_uri(self, song_name, artist):
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]

        return uri

	#Step 5: Add this song into the new Spotify playlist
	def add_song_to_playlist(self):
		pass

