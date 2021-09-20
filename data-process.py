import os
import cv2
import csv

total_vids = len(os.listdir('./static/video/'))
radius = 50

with open('./result.csv', 'r', newline='') as f:
    rows = csv.DictReader(f)
    for row in rows:
        try:
            os.mkdir(f'./data/{row["id"]}')
            for i in range(total_vids):
                video = cv2.VideoCapture(f'./static/video/{i+1}.mp4')
                total_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
                framerate = video.get(cv2.CAP_PROP_FPS)
                full_screen_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
                full_screen_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
                if not video.isOpened():
                    print("Can't open the file. Check out file's Avalibility and try again.")
                    exit()
                try:
                    os.mkdir(f'./data/{row["id"]}/{i+1}')
                    if row[f'video{i+1}'] != 'X':
                        for click in list(row[f'video{i+1}'][1:-1].split(', ')):
                            _X, _Y, _s = map(float, click[1:-1].split())
                            _X *= full_screen_width
                            _Y *= full_screen_height
                            print(_X, _Y, _s)
                            intended_frame = int(_s * framerate)
                            video.set(1, intended_frame)
                            ret, frame = video.read()
                            cv2.circle(frame, (int(_X), int(_Y)), radius, (0, 0, 255), 2)
                            cv2.imwrite(f'./data/{row["id"]}/{i+1}/{_s}.jpg', frame)
                except:
                    print('some errors happened when making directory ' + f'./data/{row["id"]}/{i+1}')
        except:
            print(f'directory ./data/{row["id"]} already exists')