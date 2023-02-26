import requests
import json
import time
from pytumblr import TumblrRestClient
from requests_oauthlib import OAuth1Session

# Set up Tumblr API credentials
consumer_key = "insert_consumer_key"
consumer_secret = "insert_consumer_secret"
access_token = "insert_access_token"
access_secret = "insert_access_secret"
client = TumblrRestClient(consumer_key, consumer_secret, access_token, access_secret)

# Set up Quote API endpoint
quote_api_endpoint = "https://api.quotable.io/random"

# Define function to post quote on Tumblr
def post_quote_on_tumblr(quote_text):
    response = client.create_text(
        "justwatchmypussy",
        body=quote_text,
        type='html',
        tags=["quotes, life, love, important, tumblr, instagood, love, aesthetic, girl, literature, sad quotes, sad poem, zitate"],
        state="published",
        )
    if 'id' in response:
        print("Quote posted on Tumblr!")
    else:
        print("Error posting quote on Tumblr.")

# Start the loop to get quote and post on Tumblr every hour
while True:
    # Get a random quote from the Quote API
    response = requests.get(quote_api_endpoint)
    if response.status_code == 200:
        quote_data = json.loads(response.text)
        quote_text = f'<h3>"{quote_data["content"]}"\n\n ~{quote_data["author"]}<h3> '
        post_quote_on_tumblr(quote_text)
    else:
        print("Error getting quote from Quote API.")

    # Wait for an hour before getting the next quote
    time.sleep(10800)
