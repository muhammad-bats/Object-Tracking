import cv2
import sys

if __name__ == "__main__" :
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Could not open video")
        sys.exit(1)

    count = 0                       #skips first 30 frames, added due to exposure issues in webcam frame when selecting ROI
    for count in range(30):         #Comment out if you do not face exposure issues or if you are using an external webcam, not the internal webcam with laptop systems.
        count += 1
    
    ok, frame = video.read()
    if not ok:
        print("Could not read video")
        sys.exit(1)

    box = cv2.selectROI(frame, False)

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
    elif trackerid == 'GOTURN':
        tracker = cv2.TrackerGOTURN_create()
    elif trackerid == 'CSRT':
        tracker = cv2.TrackerCSRT_create()

    ok = tracker.init(frame, box)

    while True:
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

        q = cv2.waitKey(1) and 0xff     #To end process, press 'esc'key and the tracking process will be automatically stopped and all data cleared. 
        if q == 27:
            video.release()
            cv2.destroyAllWindows()
            break

video.release()
cv2.destroyAllWindows()
