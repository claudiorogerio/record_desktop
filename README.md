# Record your personal desktop, audio or both
## *You can record your personal desktop, audio, microfone or cam with python3 and ffmpeg*


* *Dependencies:*
- [x] sudo apt install ffmpeg
- [x] sudo apt install python3
- [x] pip3 install ffmpeg-python

* *User Mode general:*
> python3 record_video.py output desktop_area webcam desktop microphone audio quality

* *User Mode to record Desktop area and microphone:*
```shell
output='out.mp4'    
video_size='600x480'
webcam=False
microphone=True
audio=False
quality=3       
python3 record_video.py output video_size webcam microphone audio quality
```

* *User Mode to record microphone:*
```shell
output='out.wav'   
video_size=0
webcam=False
microphone=True
audio=False
quality=3       
python3 record_video.py output video_size webcam microphone audio quality
```

Note 1: Video Output extensions accepted: mp4, mkv, mov; Audio Output extensions accepted: wav, ogg, mp3

Note 2: Quality variation from 0 (worse) to 3 (best)

Note 3: Record Stop pressing: <kbd>Ctrl</kbd> + <kbd>C</kbd> 

Note 4: Audio is a sound playing in the desktop, which in this version code it can't be to record as same way audio and microphone.
