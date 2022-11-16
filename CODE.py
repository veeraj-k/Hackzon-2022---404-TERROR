import cv2
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(check):
    if check==10:
        fromaddr = "terrorhome3@gmail.com"
        toaddr = "veerajkuppila2004@gmail.com" #reciever email can be changed from here
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "CAUTION!!! - HOME SECURITY"
        body = "Someone might have entered your house"
        msg.attach(MIMEText(body, 'plain'))
        filename = "10frame.png"
        attachment = open("10frame.png", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "yjioguvqmtnikili")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

reference=None
video=cv2.VideoCapture('burglary.mp4')
check=0
while True:
    _,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if reference is None:
        reference=gray
        continue
    diff=cv2.absdiff(reference,gray)

    thresh_frame = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)[1] 

    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 
    cnts,_=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c)<800:
            continue
        check+=1
        send_mail(check)
        

        cv2.putText(frame,'MOVEMENT DETECTED!!',(10,30),cv2.FONT_ITALIC,1,(0,0,255),1)
        
        (x, y, w, h) = cv2.boundingRect(c) 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if check==10 or check== 20 or check==40 or check==50:
            cv2.imwrite(str(check)+'frame.png', frame)
    cv2.imshow('Live',frame)
    # cv2.imshow("Difference Frame", diff) 
    # cv2.imshow("Binary frame", thresh_frame)
    
    key = cv2.waitKey(10)
    if key==ord('q'):
        break
video.release() 
cv2.destroyAllWindows() 
