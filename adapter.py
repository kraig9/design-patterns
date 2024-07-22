# Target interface
class MediaPlayer:
    def play(self, audio_type, file_name):
        pass

# Adaptee class
class AdvancedMediaPlayer:
    def play_vlc(self, file_name):
        print("Playing VLC file:", file_name)

    def play_mp4(self, file_name):
        print("Playing MP4 file:", file_name)

# Adapter class
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == 'vlc':
            self.advanced_player = AdvancedMediaPlayer()
        elif audio_type == 'mp4':
            self.advanced_player = AdvancedMediaPlayer()

    def play(self, audio_type, file_name):
        if audio_type == 'vlc':
            self.advanced_player.play_vlc(file_name)
        elif audio_type == 'mp4':
            self.advanced_player.play_mp4(file_name)

# Concrete class implementing the target interface
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, file_name):
        if audio_type == 'mp3':
            print("Playing MP3 file:", file_name)
        elif audio_type == 'vlc' or audio_type == 'mp4':
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)
        else:
            print("Invalid media type:", audio_type)

# Usage
audio_player = AudioPlayer()
audio_player.play('mp3', 'song.mp3')
audio_player.play('vlc', 'movie.vlc')
audio_player.play('mp4', 'video.mp4')
audio_player.play('avi', 'video.avi')