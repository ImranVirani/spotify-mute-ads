To use this script include your authentication details in a file called constants.py, this information should be taken from your Spotify for Developers Dashboard which you use to create apps that use the Spotify API.

The details required from the Dashboard are CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI

For the redirect URI, use I recommend using 'http://127.0.0.1:8000/callback'. Localhost isn't being supported anymore so this will save you trouble. If you use a different url, you have to make sure the variable in the app and the one on the dashboard are the same or it'll throw a confusing error when you run the script.

# NOTE: This script does not violate the Spotify TOS, no adblocker is being used, this just mutes the ads on Spotify by simulating pressing the mute button on your keyboard, the Spotify desktop app is not being modified in any way whatsoever.

This script is compatible with Linux/Mac/Windows, although it has only been tested for Windows

# Using this script

Make sure that Python 3 is installed, then run pip install -r requirements.txt to install the dependencies for the script, and python3 app.py to run the script
