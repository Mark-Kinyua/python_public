import os
import shutil

# Honestly, i dont want to move things one by one
# Decided to make a script

x = os.listdir(r"/home/mark/Downloads")

for i in x:
    x = ['.txt', '.xlsx', '.pdf', '.zip']
    for y in x:
        if i.endswith(y):
            shutil.move(fr'/home/mark/Downloads/{i}', fr'C:/home/mark/Documents/{i}')
    if i.endswith(".mp3"):
        shutil.move(fr'/home/mark/Downloads/{i}', fr'/home/mark/Music/{i}')
    if i.endswith(".mp4"):
        shutil.move(fr'/home/mark/Downloads/{i}', fr'/home/mark/Videos/{i}')
