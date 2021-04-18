#Gather info from Derpibooru

from derpibooru import Search, user
import smtplib, ssl
import time

port = 587  # For starttls
smtp_server = "smtp.gmail.com" #change the smtp server to something different if you are not using gmail.
Hostmail = "" #The email sending the email.
ReceivingMail = "" #The email you want to receive the email. It can be the same as the host mail but it is smart to have a separate email for scripts.
key = "" #API key at https://derpibooru.org/registrations/edit
password = "" #The password for your email
tags = "" #The tags you want to apply to your search. Separate them by comma.
# Create a secure SSL context
context = ssl.create_default_context()




oldValues = []
newValues = []





for image in Search().query(tags): #Initialising the initial value
  oldValues.append(image.url)

while True:
    time.sleep(180)
    for image in Search().query(tags): #Fetch all image urls on first page
        newValues.append(image.url)

    if newValues != oldValues: #Any new images?
        
        differenceInImages = set(newValues).difference(set(oldValues)) #Turn the new images into a list
        oldValues = newValues
        newValues = []

        subject = "New Images!"   
        text = """URL(s):

        """+str(differenceInImages)

        message = 'Subject: {}\n\n{}'.format(subject, text)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(Hostmail, password)
            server.sendmail(Hostmail, ReceivingMail, message)
    else:
        newValues = []
        print("No new images")  