import subprocess

original_video = "assets/video/video.mp4"
new_audio = "assets/audio/audio-1.mp3"
output = "assets/video/video_final.mp4"

command = [
    "ffmpeg",
    "-i", original_video,
    "-i", new_audio,
    "-c:v", "copy",      # mantém o vídeo sem reencodar
    "-map", "0:v:0",
    "-map", "1:a:0",
    "-shortest",
    output
]

subprocess.run(command)

print("Novo áudio inserido com sucesso!")