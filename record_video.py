import os
import time
import platform
import subprocess

"""
claudiorogerio@unifap.br
24.05.2020

funcao de gravacao com suas opções
    nome do arquivo
    dimensão 1366x736
    webcam      0 ou 1
    desktop     0 ou 1
    microphone  0 ou 1
    audio       0 ou 1
"""

def record( out_file="", video_size=0, webcam=False, desktop = True, microphone = False, audio = False, quality = 3 ):

    cmd = "ffmpeg "

    if quality == 1 :
        rate_cam = 30
        rate_desk = 20
        audio_ext = ".ogg"
    else:
        if quality == 3:
            rate_cam = 100
            rate_desk = 60
            audio_ext = ".wav"
        else:
            rate_cam = 50
            rate_desk = 25
            audio_ext = ".mp3"

    if out_file == "":
        out_file = "video.mp4"
    if video_size == 0:
        video_size = "1366x768"
    [vd_x, vd_y] = video_size.split( "x" )

    if webcam :
        cmd += "-f v4l2 -framerate " + str(rate_cam) + " -video_size 320x240 -i /dev/video0 "
        cmd += '-filter_complex ' + '"[0:v]pad=iw:' + str(vd_y) + ':0:(oh-ih)/3[left];[left][1:v]hstack" '
    if desktop :
        cmd += "-f x11grab -framerate "+ str(rate_desk) + " -video_size " + video_size + " -i :0.0 "
    if microphone :
        cmd += "-f alsa -ac 2 -ar 44100 -i default "

    if audio :
        # find board
        cmd2 = "pactl list sources | grep 'Name: alsa_output'| awk '{print $2}' > conf.audio "
        os.system( cmd2 )
        file_object  = open( "conf.audio", "r" )
        driver = file_object.read()
        driver= driver[:-1]     # get off '\n'
        file_object.close()
        cmd += "-f pulse -i " + driver + " "


    if not webcam and not desktop :
        out_file = out_file[:-4] + audio_ext

    cmd += out_file + " -y "    # overwrite files

    print ( "Running", cmd )
    os.system( cmd )        # execute command


