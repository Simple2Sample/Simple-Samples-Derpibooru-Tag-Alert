#Gather info from Derpibooru

from derpibooru import Search, user
import smtplib, ssl
import time


#### USERCONFIG ####
###Write the required strings between the quotes!

port = 587  # For starttls. Don't touch unless you know what you are doing
smtp_server = "smtp.gmail.com" #Don't touch unless you are not using Gmail.

hostMail = "" #The email sending the email.
receivingMails = [""] #The emails you want to receive the email. It can be the same as the host mail but it is smart to have a separate email for scripts. You can have multiple receiving emails by writing them as ["email1","email2"]. Great if you want to share the alerter with multiple people. You just need their email.
key = "" #API key at https://derpibooru.org/registrations/edit
searchFilter = "" #Find the filter ID you want to use at https://derpibooru.org/filters. The ID is the numbers behind the URL. I recommend using "everything" in case you want full freedom. Watch out for unexpected lewd!
password = "" #The password for your email. Don't worry, I will not and I cannot steal it. I barely know how to program this stuff, let alone a password stealer. Now that I think about it, I can make the program send your info to me pretty easily. DW I haven't done that. Just check the code below lol.

delaytime = 15 #Minutes between each check. DO NOT SET THIS TO A VERY LOW AMOUNT. You can be banned.
oldPicTolerance = 0.8 #Decrease this value if you experience old pics popping up from time to time. 0.5-0.9 should be fine. Keep the value as high as possible for extremely popular tags. Never set it above 1!!!
tags = "" #The tags you want to apply to your search. Separate them by comma. Ex: "Safe, Spitfire, best pony"

subject = "New Images!"   #The subject of the message you want to send!
text = """URL(s):

"""#The text you want to send. The links comes after this

#### END OF CONFIG. DO NOT TOUCH ANYTHING ELSE UNLESS YOU WANT TO CHANGE THE FUNCTIONALITY ####









print("Running!")
oldValues = []
newValues = []
try:
    for image in Search().key(key).filter(searchFilter).query(tags): #Initialising the initial value
        oldValues.append(image.url)
except:
    print("Error initialising picture search. Check your internet connection")
while True:
    time.sleep(60*delaytime)
    try:

        for image in Search().key(key).filter(searchFilter).query(tags): #Fetch all image urls on first page
            newValues.append(image.url)

            checkForNewImages = set(newValues[0:int((len(newValues)*oldPicTolerance))]).difference(set(oldValues)) #Checks for the difference in NEW pics uploaded, not old ones. Might cause some bugs if a huge number of pics are uploaded in the span of delaytime.
    except:
        print("Error connecting to the Derpibooru servers")
        newValues = []
        continue
    

    if checkForNewImages: #Any new images?
        print("New images found!")
        differenceInImages = str(checkForNewImages) #Removes the images found in OldImages from NewImages and outputs the remaining images.
        oldValues = newValues #Stores the new value for next iteration.
       
        newValues = []
        differenceInImages = differenceInImages.replace("'",'')

  
        messagetext = text+" "+differenceInImages[1:-1]#Combines the URLs from set to string.

        message = 'Subject: {}\n\n{}'.format(subject, messagetext)#Formats the subject and text into a format understood by the function.
        while True:
            try:
                for emails in receivingMails:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:#Magic magic sendy-email-thingy
                        server.ehlo()
                        server.starttls(context=context)
                        server.ehlo()
                        server.login(hostMail, password)
                        server.sendmail(hostMail, emails, message)
                break
            except:
                print("Something is wrong with the email sender. Check your internet connection or info if everything is correct. Retrying...")
                time.sleep(60)
    else:
        if newValues: #Doesn't change the old value if the list is empty. This happens in case of server problems.
            oldValues = newValues #Stores the new value for next iteration.
        newValues = []
        print("No new images")  