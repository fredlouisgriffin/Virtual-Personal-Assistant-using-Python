import subprocess

paths = {
    'vlc': "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
}


def open_vlc(file_path):
    subprocess.call([paths['vlc'], file_path, '--no-loop', '--no-repeat', '--play-and-exit'])


local_target_dir = "D:\\_PYTHON_PC\\PycharmProjects\\Virtual-Personal-Assistant-using-Python\\examples\\podcast"
