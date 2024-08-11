# Object-Tracking
Object Tracking using cv2 Trackers

This code uses python-opencv liberary to track objects. The code performs realtime tracking using webcams connected to the system. 
The code includes a list of different trakcers which can be used. 

## Code Working

User is first prompted to draw a bounding box around the object they want to track, the bounding box is drawn using mouse commands. 

![image](https://github.com/user-attachments/assets/e9c6ea7d-3ade-4ba9-848d-e8d29f71c65c)

Then the user is prompted to select which tracker they want to use from a list of trackers. The user has to input the index number of the tracker they want to use, index starts from 0. 

![image](https://github.com/user-attachments/assets/3ebec8e3-1b75-4e22-9361-7cc640981e51)

After selecting the tracker, the object is tracked using the selected tracker. 

![image](https://github.com/user-attachments/assets/344370b9-f0b6-4b94-9720-c4fd4bd19b49)

The code displays when the object cannot be detected if it is not within the webcam feed. 

![image](https://github.com/user-attachments/assets/27f11dcc-536a-424e-b37a-cfec91dbb024)


Press *'esc'* key to terminate process. 
