import time
import yaml
from download import download
class main:
    tags = yaml.safe_load(open('./config.yml','r'))
    video_file_path = (tags['Settings']['Video'])
    audio_file_path = (tags['Settings']['Audio'])
    logs_file_path = (tags['Settings']['Logs'])
    video_urls = open(video_file_path).readlines()
    audio_urls = open(audio_file_path).readlines()
    yt_download = download()
    for video_url in video_urls:
        yt_download.video(video_url, './downloads', logs_file_path)
        time.sleep(60)

    for audio_url in audio_urls:
        yt_download.audio(audio_url, './downloads', logs_file_path)
        time.sleep(60)
