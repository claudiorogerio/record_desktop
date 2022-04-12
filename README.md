# Record your personal desktop, audio or both
## *You can record your personal desktop, audio, microfone or cam with python3 and ffmpeg*


* *Dependencies:*
- [x] sudo apt install ffmpeg
- [x] sudo apt install python3
- [x] pip3 install ffmpeg-python

* *User Mode general:*
> python3 record_file.py output desktop_area webcam desktop microphone audio quality

* *User Mode to record Desktop area and microphone:*
> python3 record_file.py output='file.mp4' desktop_area='600x480' webcam=False microphone=True audio=False quality=3

* *User Mode to record microphone:*
> python3 record_file.py output='file.wav' desktop_area=0 webcam=False microphone=True audio=False quality=3

Note 1: Record Stop pressing: < crtl > + < c >

Note 2: Audio is a sound playing in the desktop, which in this version code it can't be to record as same way audio and microphone.
