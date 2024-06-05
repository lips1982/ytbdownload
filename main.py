import os
from pytube import Playlist,YouTube
import pytube
import re

# Obtener la URL de la playlist
playlist_url = 'https://www.youtube.com/watch?v=2SetvwBV-SU&list=PLvq-jIkSeTUZ6QgYYO3MwG9EMqC-KoLXA'

# Crear un objeto Playlist de pytube
playlist = Playlist(playlist_url)

# Obtener el título de la playlist y crear una carpeta con ese nombre

playlist_title = playlist.title

os.makedirs(playlist_title, exist_ok=True)

#caracteres especiales
special_chars_regex = r'[\"\'\\\/\|\?\-\[\]\&\*<>]'

# Descargar cada video de la playlist
for video in playlist.videos:
    # Verificar que el título del video no tenga caracteres no ASCII
    try:
        video_title = video.title.encode('ASCII', 'ignore').decode('utf-8')
        url= video.watch_url
        if video_title != video.title or re.search(special_chars_regex, video_title):
            video_title = re.sub(special_chars_regex, '', video_title)
            print (f"yt-dlp {url}" )

    except:
        pass
print('Descarga finalizada')
# instalar yt-dlp despues pegar el resultado en el cmd o bash
#pip install yt-dlp 
