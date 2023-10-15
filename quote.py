import requests
import json
import time
from pytumblr import TumblrRestClient
from requests_oauthlib import OAuth1Session

# Set up Tumblr API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_secret = "your_access_token_secret"
client = TumblrRestClient(consumer_key, consumer_secret, access_token, access_secret)

# Set up Quote API endpoint
quote_api_endpoint = "https://api.quotable.io/random"

# Define function to post quote on Tumblr
def post_quote_on_tumblr(quote_data):
    response = client.create_quote(
        "your_blog_name",
        quote=quote_data["content"],
        source=quote_data["author"],
        tags=[quote_data["author"], 'quotes', 'life', 'love', 'important', 'tumblr', 'instagood', 'love', 'aesthetic', 'girl', 'literature', 'sad quotes', 'sad poem', 'zitate'],
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
        post_quote_on_tumblr(quote_data)
    else:
        print("Error getting quote from Quote API.")

    # Wait for an hour before getting the next quote
    time.sleep(10800) #set to 3 hours
