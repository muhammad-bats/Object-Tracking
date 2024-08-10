import cv2
import sys

if __name__ == "__main__" :
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Could not open video")
        sys.exit(1)

    count = 0
    for count in range(15):
        count += 1
    
    ok, frame = video.read()
    if not ok:
        print("Could not read video")
        sys.exit(1)

    box = cv2.selectROI(frame, False)

    tracker_list = ['BOOSTING', 'MIL', 'TLD', 'KCF', 'GOTURN', 'CSRT' ]
    tracker_type = tracker_list[5]
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    elif tracker_type == 'CSRT':
        tracker = cv2.TrackerCSRT_create()
    ok = tracker.init(frame, box)

    while True:
        ok, frame = video.read()
        if not ok:
            print("Failed to grab frame.")
            break
        print(frame.shape)
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

        q = cv2.waitKey(1) and 0xff
        if q == 27:
            break

video.release()
cv2.destroyAllWindows()