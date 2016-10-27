import spotipy
import spotipy.util as util
import csv

NUM_TRACKS = 100
GENRES = ['jazz','blues','country','classical','french','alternative','rock','pop','electro','r-n-b','hip-hop','soul','techno','hard-rock','reggae','folk','indie','punk','heavy-metal','psych-rock',]

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
		writer = csv.DictWriter(csvfile, keys)
	
		writer.writeheader()
		writer.writerows(tracks)

def  collectTracks():
	for genre in GENRES:
		unprocessedTracks = sp.recommendations(seed_genres=genre, limit=NUM_TRACKS)

def buildTracks()

track_inf = sp.recommendations(seed_genres=GENRE, limit=2)
print(track_inf['tracks'][0])
artist = track_inf['tracks'][0]['artists'][0]['name']
track = track_inf['tracks'][0]['name']
track_id = track_inf['tracks'][0]['id']
#print(artist)
#print(track)
print(artist + ' - ' + track)

print(track_id)
features = sp.audio_features([track_id])[0]
print(features)
	
#	print(track2)


track_inf = sp.recommendations(seed_genres='jazz', limit=NUM_TRACKS)
tracks = []

for i in range(NUM_TRACKS):
	track_id = track_inf['tracks'][i]['id']
	features = sp.audio_features([track_id])[0]
	tracks.append({})
	tracks[i]['artist'] = track_inf['tracks'][i]['artists'][0]['name']
	tracks[i]['track'] = track_inf['tracks'][i]['name']
	tracks[i]['danceability'] = features['danceability']
	tracks[i]['energy'] = features['energy']
	tracks[i]['key'] = features['key']
	tracks[i]['loudness'] = features['loudness']
	tracks[i]['speechiness'] = features['speechiness']
	tracks[i]['acousticness'] = features['acousticness']
	tracks[i]['instrumentalness'] = features['instrumentalness']
	tracks[i]['liveness'] = features['liveness']
	tracks[i]['valence'] = features['valence']
	tracks[i]['tempo'] = features['tempo']
	tracks[i]['duration_ms'] = features['duration_ms']
	tracks[i]['time_signature'] = features['time_signature']
	tracks[i]['genre'] = GENRE


