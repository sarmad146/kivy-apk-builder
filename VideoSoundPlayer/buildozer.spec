[app]
title = VideoSoundApp
package.name = videosoundplayer
package.domain = org.yourdomain
source.include_exts = py,kv,mp3,mp4,png,jpg
requirements = python3,kivy,kivymd,ffpyplayer
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
icon.filename = icon.png
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
