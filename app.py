import spotipy
from spotipy.oauth2 import SpotifyPKCE
import time
from pynput.keyboard import Key, Controller
import os

try:
    import constants
except ImportError:
    constants = None
keyboard = Controller()
'''
keyboard.press(Key.media_volume_mute)
keyboard.release(Key.media_volume_mute)
time.sleep(5)  # Wait for a second

keyboard.press(Key.media_volume_mute)
keyboard.release(Key.media_volume_mute)
'''

# Spotify API credentials - replace with your own
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID") or getattr(constants, "CLIENT_ID", None)
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI") or getattr(constants, "REDIRECT_URI", None)

if not CLIENT_ID or not REDIRECT_URI:
    raise RuntimeError(
        "Missing Spotify configuration. Set SPOTIFY_CLIENT_ID and SPOTIFY_REDIRECT_URI "
        "environment variables (or define CLIENT_ID and REDIRECT_URI in constants.py)."
    )

# Set up Spotify authentication (PKCE flow for public clients)
sp = spotipy.Spotify(auth_manager=SpotifyPKCE(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URI,
    scope='user-read-playback-state user-modify-playback-state'
))

def is_ad_playing():
    """
    Check if an advertisement is currently playing.
    Returns True if ad is playing, False otherwise.
    """
    try:
        current = sp.current_playback()
        
        if current is None:
            print("No playback detected")
            return False
        
        # Ads typically have these characteristics:
        # 1. currently_playing_type is 'ad'
        # 2. track is None or has no URI
        # 3. is_playing is True but track info is limited
        
        playing_type = current.get('currently_playing_type')
        
        if playing_type == 'ad':
            return True
        
        # Additional check: if track is None while playing
        if current.get('is_playing') and current.get('item') is None:
            return True
            
        return False
        
    except Exception as e:
        print(f"Error checking playback: {e}")
        return False

def monitor_ads(check_interval=2):
    """
    Continuously monitor Spotify for advertisements.
    
    Args:
        check_interval: Seconds between checks (default: 2)
    """
    print("Starting Spotify ad monitor...")
    print("Press Ctrl+C to stop\n")
    
    ad_playing = False
    
    try:
        while True:
            is_ad = is_ad_playing()
            
            if is_ad and not ad_playing:
                print("🔴 Advertisement detected!")
                keyboard.press(Key.media_volume_mute)
                keyboard.release(Key.media_volume_mute)


                ad_playing = True
            elif not is_ad and ad_playing:
                print("🟢 Advertisement ended, music resumed")
                ad_playing = False
                keyboard.press(Key.media_volume_mute)
                keyboard.release(Key.media_volume_mute)
            
            time.sleep(check_interval)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped")

if __name__ == "__main__":
    # Simple usage example
    print("Checking if ad is currently playing...")
    if is_ad_playing():
        print("Yes, an advertisement is playing")
    else:
        print("No advertisement detected")
    
    print("\n" + "="*50)
    print("Starting continuous monitoring...")
    print("="*50 + "\n")
    
    # Start continuous monitoring
    monitor_ads(check_interval=2)
