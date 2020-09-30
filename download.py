from pytube import YouTube
from pytube import Playlist
import re
import time

class download:

    def __download_file(self, url, download_folder, audio_only):
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=audio_only).first()
            stream.download(download_folder)

    def video(self, url, download_folder, logs):
        logs_file = open(logs, 'a')
        x = re.search('list=', url)
        if x is not None:
            playList = Playlist(url)
            if playList is None:
                playList._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            for playlists_url in playList:
                try:
                    print('Downloading...'+playlists_url)
                    playList.download_all(download_folder)
                except Exception as ex:
                    logs_file.write('Unable to download: '+playlists_url+'\t'+str(ex)+'\n')
                    pass
        else:
             try:
                print('Downloading...' + url)
                self.__download_file(url, download_folder, False)
             except Exception as ex:
                 logs_file.write('Unable to download: '+url+'\t'+str(ex))
        logs_file.close()
    def audio(self, url, download_folder, logs):
        logs_file = open(logs, 'a')
        x = re.search('list=', url)
        if x is not None:
            playList = Playlist(url)
            playList._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            for playlists_url in playList:
                try:
                    print('Downloading...' + playlists_url)
                    self.__download_file(playlists_url, download_folder, True)
                    time.sleep(60)
                except Exception as ex:
                    logs_file.writelines('Unable to download: '+playlists_url+'\t'+str(ex)+'\n')
                    pass
        else:
            try:
                print('Downloading...' + url)
                self.__download_file(url, download_folder, True)
            except Exception as ex:
                logs_file.write('Unable to download: '+url+'\t'+str(ex)+'\n')
                pass
        logs_file.close()



