import os
import pandas as pd
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id="3233166ec6424efc85ac5fb6c2f4ddf5",
    client_secret="e1f97fd1c0f84246a68a4b50672784df"
))


# Get artist information by ID
artist_id = "7nzSoJISlVJsn7O0yTeMOB"  # Joe Hisaishi
top_tracks = spotify.artist_top_tracks(artist_id)

#Sacamos las 10 más populares
top_10_tracks = top_tracks['tracks'][:10]

# Preparamos la lista de lo que vamos a guardar en el DataFrame

tracks_info = []

for track in top_10_tracks: #Iteramos para guardar de manera efectiva los campos que nos interesan
    track_info = {
        "Track Name": track['name'],
        "Popularity": track['popularity'],
        "Duration (min)": track['duration_ms'] / 60000  # Convert from milliseconds to minutes
    }
    tracks_info.append(track_info)

# Como se pide, convertimos a DF
df_tracks = pd.DataFrame(tracks_info)

#Ordenamos para mostrar las tres mas populares
df_sorted = df_tracks.sort_values(by="Popularity", ascending=False).head(3)
print("Las tres canciones mas populares son:", df_sorted)

#Hacemos el plot para mostrar la posible relación entre duración y popularidad 

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_tracks, x='Duration (min)', y='Popularity')

plt.title('Duration vs Popularity of Songs', fontsize=14)
plt.xlabel('Duration (minutes)', fontsize=12)
plt.ylabel('Popularity', fontsize=12)

plt.show()

print("Como se demuestra en el gráfico, se intuye que hay relación entre popularidad y duración de la canción")

#Y si no que se lo digan a Bohemian Rhapsody, una canción que para sus tiempos era larga y por ello tuvo problemas para 
# publicarse y sin embargo se ha convertido en uno de los referentes de la música rock.

#He visto que se importaba seaborn, y he buscado una manera de darle uso para mostrar de una manera más clara lo que se nos pide

# Scatter plot con linea de regresión

plt.figure(figsize=(8, 6))
sns.regplot(data=df_tracks, x='Duration (min)', y='Popularity', scatter_kws={'s': 100, 'alpha': 0.7}, line_kws={'color': 'red'})

plt.title('Duración VS Popularidad', fontsize=14)
plt.xlabel('Duración (minutos)', fontsize=12)
plt.ylabel('Popularidad', fontsize=12)
plt.show()

#Tal y como se muestra en la linea ascendente, si que está implícito (al menos en un caso con una muestra tan baja como este)
# que, efectivamente, hay una relación entre las canciones mas largas y su popularidad.