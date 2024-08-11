# Object-Tracking
Object Tracking using cv2 Trackers

This code uses python-opencv liberary to track objects. The code performs realtime tracking using webcams connected to the system. 
The code includes a list of different trakcers which can be used. 

## Tracker Working

User is first prompted to draw a bounding box around the object they want to track, the bounding box is drawn using mouse commands. 

![image](https://github.com/user-attachments/assets/e9c6ea7d-3ade-4ba9-848d-e8d29f71c65c)

Then the user is prompted to select which tracker they want to use from a list of trackers. The user has to input the index number of the tracker they want to use, index starts from 0. 

![image](https://github.com/user-attachments/assets/3ebec8e3-1b75-4e22-9361-7cc640981e51)

After selecting the tracker, the object is tracked using the selected tracker. 

![image](https://github.com/user-attachments/assets/344370b9-f0b6-4b94-9720-c4fd4bd19b49)

The code displays when the object cannot be detected if it is not within the webcam feed. 

![image](https://github.com/user-attachments/assets/27f11dcc-536a-424e-b37a-cfec91dbb024)


Press *'esc'* key to terminate process. 

## Code Explanation


Importing modules
```
import cv2  
import sys
```

Selecting Webcam feed for video source. Includes error handling incase webcam cannot be opened.

```
video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Could not open video")
        sys.exit(1)
```

Reads the frame and displays it. Includes error handling incase the frame cannot be read properly.

The `cv2.selectROi` function allows the user to draw the bounding box

```
ok, frame = video.read()
    if not ok:
        print("Could not read video")
        sys.exit(1)

    box = cv2.selectROI(frame, False)
```

Allows user to select the tracker they want to use and loads it. These trackers are built-in the cv2 module

```
tracker_list = ['BOOSTING', 'MIL', 'TLD', 'KCF', 'GOTURN', 'CSRT' ]
    print(tracker_list)
    trackerid = input("Enter tracker id ")
    if trackerid == '0':
        tracker = cv2.TrackerBoosting_create()
    elif trackerid == '1':
        tracker = cv2.TrackerMIL_create()
    elif trackerid == '2':
        tracker = cv2.TrackerTLD_create()
    elif trackerid == '3':
        tracker = cv2.TrackerKCF_create()
    elif trackerid == '4':
        tracker = cv2.TrackerGOTURN_create()
    elif trackerid == '5':
        tracker = cv2.TrackerCSRT_create()

    ok = tracker.init(frame, box)
```

Reads the next frame and builds the bounding box using the `cv2.rectangle` function

`cv2.putTect` function displays text on the feed and takes args to customise the text. The try-except provides error handling. 

```
ok, frame = video.read()
if not ok:
    print("Failed to grab frame.")
    break
try:
    ok, box = tracker.update(frame)
    if ok:
        # tracking is successfull
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "Tracking", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    else:
        # failure to track
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
except Exception as e:
    print("Error", e)
    break

cv2.imshow("Tracking", frame)
```

Allows user to terminate the program and end tracking by pressing the '*esc*' key. 

The `cv2.waitkey` function allows this to happen.

```
q = cv2.waitKey(1) and 0xff
if q == 27:
    video.release()
    cv2.destroyAllWindows()
    break
```

The `video.release()` and `cv2.DestroyAllWindows` clear any data from the tracking process.
