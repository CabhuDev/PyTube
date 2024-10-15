import yt_dlp

def descargar_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Ejemplo de uso

url_video = "https://youtu.be/4l5Z_uCyBfM"
descargar_video(url_video)

