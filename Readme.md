
Hey and thanks for checking this out!

Made by Simple Sample

# WARNING
As of 4th of March 2022, Google will remove "Less Secure App Access" which the script relies on. To make it work again after 30th of May, use "App Password" as shown here https://support.google.com/accounts/answer/185833?

## What does this script do?
This script lets the user be notified whenever a new image on Derpibooru has been posted. When it detects a change, it will send an email to the user with a link to the new images found!

That way you will never have to check Derpibooru repeatedly for new images of your best pony.

Pretty simple, right?

## Why did you make this?
Ok, I admit it. I'm kind of obsessed over Spitfire. I noticed that I was checking Derpibooru's tag of her very often, so instead I let this script do it for me.

Yes I know it's weird. About one image of her is made every one or two days, so I usually never find anything new whenever I look at Derpibooru. This script thus frees my time.

# INSTRUCTIONS

I recommend running this script on a Raspberry Pi or a server of some sort.

1. Install [Python3](https://www.python.org/). Linux users usually already have this.
2. Install [pip](https://pypi.org/project/pip/). This is usually included in Python3.
	- If not, follow these [instructions](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py)


This script also uses one external library because I could not be bothered to properly learn how one uses the JSON API for Derpibooru. Thanks a lot to https://github.com/joshua-stone/DerPyBooru.

3. Run:
	`pip3 install derpybooru`
4. Create a throwaway GMAIL account or use a GMAIL account you do not care about.
	The script needs a Gmail account because they have some fancy stuff.
5. Enable "App Password" as shown in https://support.google.com/accounts/answer/185833? The app password provided by Google will be the password for the script.
7. Fill in the empty variables in the userconfig part of the script.
	- The comments in the script should explain it well enough.
8. Once everything is filled in. Run the program and let it run 24/7 using the command:
	`Python3 DerpibooruTagAlert.py` (Assuming you are in the same folder as the file)

*I recommend letting it check every couple of minutes in the beginning to see if it works as it should.*
## Known Bugs
1. ~~There are some brackets around the URLs in the message sent.~~ FIXED

2. ~~The script sends an old image if it scans an image that later gets deleted.~~ FIXED

All bugs have been fixed! It now works as originally intended!
---
*Spitfire is the best pony*
