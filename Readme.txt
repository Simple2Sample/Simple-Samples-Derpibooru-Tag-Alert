
Hey and thanks for checking this out!

Made by Simple Sample
Check out my art if you feel like it: https://derpibooru.org/profiles/Simple%2BSample

####What does this do?####

This program lets the user be notified whenever a new image on Derpibooru has been posted.
When it detects a change, it will send an email to the user with a link to the new images found!
That way you will never have to check Derpibooru repeatedly for new images of your best pony.

Pretty simple, right?

######

####Why did you make this?####

Ok, I admit it. I'm kind of obsessed over Spitfire. I noticed that I was checking Derpibooru's tag of her very often, so instead I let this script do it for me.
Yes I know it's weird. About one image of her is made every day, so I usually never find anything new. This script frees my time.

#####INSTRUCTIONS#####

Install Python3. Linux users usually already have this.
https://www.python.org/

Install pip. This is usually included in Python3.
If not, run: 

sudo install pip


This script also uses one external library because I could not be bothered to properly learn
how one uses the JSON API for Derpibooru. Thanks a lot to https://github.com/joshua-stone/DerPyBooru

Run:
sudo pip install derpybooru


Create a throwaway GMAIL account or use a GMAIL account you do not care about.
The script needs a Gmail account because they have some fancy stuff.
Enable "Less Secure App Access" at https://myaccount.google.com/u/1/security
This is to make sure the script can use the Gmail account.


Fill in the empty variables in the userconfig part of the script.
The comments in the script should explain it well enough.

Once everything is filled in. Run the program and let it run 24/7.
I recommend letting it check every couple of minutes in the beginning to see if it works as it should.
####################

####Known Bugs####

1. There are some brackets around the URLs in the message sent.
2. The script sends an old image if it scans an image that later gets deleted. One can avoid this by letting the scanning interval be larger.
#####################

Spitfire is the best pony

#####################
