import spotipy
import spotipy.util as util
import csv

NUM_TRACKS = 10
GENRES = ['jazz','blues','country','classical','french','alternative','rock','pop','electro','r-n-b','hip-hop','soul','techno','hard-rock','reggae','folk','indie','punk','heavy-metal','psych-rock']

SPOTIPY_CLIENT_ID='09545564279049d6a48a476ee8a2163f'
SPOTIPY_CLIENT_SECRET='5941931004de4fd6ba6daf7deb81be6b'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
username = 'benoit.lafon'
scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

def writeToCSV(tracks):
#	keys = tracks[0].keys()
	keys =['artist', 'track', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature', 'valence', 'genre']
	with open('music_collection.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, keys)
	
		writer.writeheader()
		writer.writerows(tracks)

def collectTracks():
	tracks = []
	for genre in GENRES:
		unprocessedTracks = sp.recommendations(seed_genres=genre, limit=NUM_TRACKS)
		for i in range(NUM_TRACKS):
			tracks.append(buildTrack(unprocessedTracks['tracks'][i], genre))
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
	processedTrack['genre'] = genre

	return processedTrack

writeToCSV(collectTracks())


