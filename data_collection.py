# coding: utf-8
#exec(open("./data_collection.py").read())

from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import sys
import time
import spotipy
import spotipy.util as util
from sys import argv
import csv

NUM_TRACKS = 10
GENRE = 'jazz'

SPOTIPY_CLIENT_ID='09545564279049d6a48a476ee8a2163f'
SPOTIPY_CLIENT_SECRET='5941931004de4fd6ba6daf7deb81be6b'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
username = 'benoit.lafon'
scope = 'user-library-read'



token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

#	track = sp.search(q='roadhouse', type='track', limit=1)
#	print(sp.recommendation_genre_seeds())
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
	tracks.append({})
	tracks[i]['artist'] = track_inf['tracks'][i]['artists'][0]['name']
	tracks[i]['track'] = track_inf['tracks'][i]['name']
	features = sp.audio_features([track_id])[0]
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

with open('music_collection.csv', 'w') as csvfile:
	fieldnames = ['artist', 'track', 'danceability','energy','key','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature','genre']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	for i in tracks:
		writer.writerow({'artist':i['artist'], 'track':i['track'], 'danceability':i['danceability'],'energy':i['energy'],'key':i['key'],'loudness':i['loudness'],'speechiness':i['speechiness':],'acousticness':i['acousticness'],'instrumentalness':i['instrumentalness'],'liveness':i['liveness'],'valence':i['valence'],'tempo':i['tempo'],'duration_ms':i['duration_ms'],'time_signature':i['time_signature'],'genre':i['genre']})


