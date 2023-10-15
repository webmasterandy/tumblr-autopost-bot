import requests
import os
import json
import random
import time
from pytumblr import TumblrRestClient
from requests_oauthlib import OAuth1Session

# Set up Tumblr API credentials
consumer_key = "insert"
consumer_secret = "insert"
access_token = "insert"
access_secret = "insert"
client = TumblrRestClient(consumer_key, consumer_secret, access_token, access_secret)

# Set up Meme API endpoint
meme_api_endpoint = "https://api.behfus.de/v1/memes/?no-gif"

# Define function to post meme on Tumblr
def post_meme_on_tumblr(title, image_path):
    response = client.create_photo(
        "insert_here_your_tumblr_blog_name",
        caption=title,
        state="published",
        data=image_path,
        tags=selected_tags  # Tags anpassen
    )
    if 'id' in response:
        print("Meme posted on Tumblr!")
    else:
        print("Error posting meme on Tumblr.")

# Start the loop to get meme, download, post on Tumblr and delete image
while True:
    # Get a random meme from the Meme API
    response = requests.get(meme_api_endpoint)
    if response.status_code == 200:
        meme_data = response.json()
        title = meme_data.get("title")
        image_url = meme_data.get("url")

        if title and image_url:
            # Download the image
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_path = "temp_meme.jpg"
                with open(image_path, "wb") as f:
                    f.write(image_response.content)
                
                available_tags = ['memes', 'funny', 'humor', 'tumblr', 'instagood', 'memelabor', '#meme', '#memes', '#funny', '#dankmemes', '#memesdaily', '#funnymemes', '#lol', '#humor', '#follow', '#dank', '#love', '#like', '#memepage', '#comedy', '#instagram', '#dankmeme', '#tiktok', '#anime', '#lmao', '#dailymemes', '#edgymemes', '#fun', '#ol', '#offensivememes', '#memestagram', '#bhfyp', '#funnymeme', '#instagood', '#shitpost', '#memer', '#viral', '#explorepage', '#funnyvideos', '#jokes', '#fortnite', '#explore', '#art', '#haha', '#followforfollowback', '#trending', '#memesespa', '#likeforlikes', '#f', '#memeita', '#youtube', '#gaming', '#memez', '#laugh', '#edgy', '#memeaccount', '#animememes', '#gamer', '#minecraft', '#dankmemesdaily', '#india', '#cute', '#music', '#memelord', '#life', '#spicymemes','#dankmemes', '#memesdaily', '#lol', '#funnymemes', '#dank', '#lmao', '#love', '#comedy', '#follow', '#fortnite', '#dankmeme', '#edgymemes', '#humor', '#like', '#anime', '#edgy', '#fun', '#instagood', '#cringe', '#art', '#offensivememes', '#hilarious', '#instagram', '#offensive', '#music', '#funnyvideos', '#bhfyp']  # Liste aller verfügbaren Tags
                selected_tags = random.sample(available_tags, 10)  # Wähle 15 zufällige Tags

                # Post the meme on Tumblr
                post_meme_on_tumblr(title, image_path)

                # Delete the downloaded image
                os.remove(image_path)
            else:
                print("Error downloading image from URL.")
        else:
            print("No title or image URL found in meme data.")
    else:
        print("Error getting meme from Meme API.")

    sleep_time = random.randint(10000, 11600)
    print(f"Warte für {sleep_time} Sekunden...")
    # Warte eine Stunde, bevor das nächste Meme abgerufen wird
    time.sleep(sleep_time)
