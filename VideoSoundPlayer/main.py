from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.video import Video
from kivy.core.audio import SoundLoader

Window.clearcolor = (0, 0, 0, 1)

Builder.load_file("player.kv")

class PlayerScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.video = Video(source='assets/sample_video.mp4', state='stop', options={'eos': 'loop'})
        self.ids.video_box.add_widget(self.video)
        self.sound = None

    def play_video(self):
        self.video.state = 'play'

    def stop_video(self):
        self.video.state = 'stop'

    def play_audio(self):
        if not self.sound:
            self.sound = SoundLoader.load('assets/sample_audio.mp3')
        if self.sound:
            self.sound.play()

    def stop_audio(self):
        if self.sound:
            self.sound.stop()

class VideoSoundApp(MDApp):
    def build(self):
        self.title = "3D Smooth Video & Sound Player"
        return PlayerScreen()

VideoSoundApp().run()
