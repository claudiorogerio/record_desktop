# Record your personal desktop, audio or both
## *You can record your personal desktop, audio, microfone or cam with python3 and ffmpeg*


* *Dependencies:*
- [x] sudo apt install ffmpeg
- [x] sudo apt install python3

* *User Mode general:*
> python3 record_file.py output desktop_area webcam desktop microphone audio quality

* *User Mode to record Desktop area and microphone:*
> python3 record_video.py file.mp4 '600x480' False True False 3

* *User Mode to record microphone:*
> python3 record_video.py file.wav 0 False True False 3

Note 1: It is important to follow this verbate order.

Note 2: Audio is some sound playing in the momment, which in this version it can't be to record as same way than microphone.
