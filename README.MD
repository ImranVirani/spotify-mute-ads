To use this script, configure Spotify auth values from your Spotify for Developers Dashboard.

This app now uses PKCE, so only these values are required:
- CLIENT_ID
- REDIRECT_URI

For the redirect URI, use I recommend using 'http://127.0.0.1:8000/callback'. Localhost isn't being supported anymore so this will save you trouble. If you use a different url, you have to make sure the variable in the app and the one on the dashboard are the same or it'll throw a confusing error when you run the script.

You can provide these values either by:
- Environment variables:
  - SPOTIFY_CLIENT_ID
  - SPOTIFY_REDIRECT_URI
- Or `constants.py` with:
  - CLIENT_ID
  - REDIRECT_URI

# NOTE: This script does not violate the Spotify TOS, no adblocker is being used, this just mutes the ads on Spotify by simulating pressing the mute button on your keyboard, the Spotify desktop app is not being modified in any way whatsoever.

This script is compatible with Linux/Mac/Windows, although it has only been tested for Windows.



