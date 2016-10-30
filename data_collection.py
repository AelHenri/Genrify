import spotipy
import spotipy.util as util
import csv
import time

NUM_TRACKS = 100
GENRES = ['jazz','blues','country','classical','french','alternative','rock','pop','electro','r-n-b','hip-hop','soul','techno','hard-rock','reggae','folk','indie','punk-rock','heavy-metal','psych-rock']
COLUMNS = ['artist','track','danceability','energy','key','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature']

SPOTIPY_CLIENT_ID='f380296eefe34641ba6601f235f24c85'
SPOTIPY_CLIENT_SECRET='c13a31dcc76f43c792f6b7cd266450c2'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
username = 'Alkinn'
scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

def writeToCSV(tracks):
	keys = tracks[0].keys()
	with open('music_collection.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = COLUMNS+GENRES)
	
		writer.writeheader()
		writer.writerows(tracks)

def collectTracks():
	tracks = []
	for genre in GENRES:
		unprocessedTracks = sp.recommendations(seed_genres=genre, limit=NUM_TRACKS)
		n = NUM_TRACKS
		length = len(unprocessedTracks['tracks'])
		if (length != NUM_TRACKS):
			print("Got less than " + str(NUM_TRACKS) + " tracks.")
			n = length
		for i in range(n):
			tracks.append(buildTrack(unprocessedTracks['tracks'][i], genre))
		time.sleep(1)
	return tracks

def buildTrack(unprocessedTrack, genre):
	processedTrack = {}
	track_id = unprocessedTrack['id']
	features = sp.audio_features([track_id])[0]
	processedTrack['artist'] = unprocessedTrack['artists'][0]['name']
	processedTrack['track'] = unprocessedTrack['name']
	processedTrack['danceability'] = features['danceability']
	processedTrack['energy'] = features['energy']
	processedTrack['key'] = features['key']
	processedTrack['loudness'] = features['loudness']
	processedTrack['speechiness'] = features['speechiness']
	processedTrack['acousticness'] = features['acousticness']
	processedTrack['instrumentalness'] = features['instrumentalness']
	processedTrack['liveness'] = features['liveness']
	processedTrack['valence'] = features['valence']
	processedTrack['tempo'] = features['tempo']
	processedTrack['duration_ms'] = features['duration_ms']
	processedTrack['time_signature'] = features['time_signature']
	for g in GENRES:
		processedTrack[g] = 1 if g == genre else 0

	return processedTrack

writeToCSV(collectTracks())


