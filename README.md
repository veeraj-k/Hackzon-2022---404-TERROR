# Hackzon-2022---404-TERROR
Public Repo for the submission of final project for Hackzon 2022

#Introduction to the idea and the project of the hackathon:
Our project begins by taking a static reference image and then comparing it with the upcoming frames. The upcoming frames are first converted to grayscale image ,thenthe absolute difference is calculated with respect to reference image. This difference is then used to calculate the contour areas using the opencv library. If the areasare comparatively higher then an alert message is sent to the recipient along with an attached  image of the event occurred in the house.


#Steps of execution:

1.Install cv2 , smtp, email module using
    pip install opencv-python
    pip install secure-smtplib
    pip install email
    
2. Run the code using any compiler.
3. Enter a valid email address to recieve the alerts.
4. The movements will be captured and then sent to the entered email address.

#Screenshots:
Enter email
![image](https://user-images.githubusercontent.com/73791070/202212034-f1a0b8e7-d82e-4fd9-9964-8a49ea2e9ec3.png)

Movements Detected
![image](https://user-images.githubusercontent.com/73791070/202212186-7ffd42e5-a689-4dbc-aac6-1d2c62f96ab8.png)

Email sent
![image](https://user-images.githubusercontent.com/73791070/202212443-99b9cef8-b7f1-49c1-811e-a1b8f53d806b.png)



