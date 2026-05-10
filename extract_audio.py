import subprocess

video = "assets/video/video.mp4"
audio = "assets/audio/audio.mp3"

command = [
    "ffmpeg",
    "-i", video,
    "-q:a", "0",
    "-map", "a",
    audio
]

subprocess.run(command)

print("Áudio extraído com sucesso!")