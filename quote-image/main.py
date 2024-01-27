import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from requests.auth import HTTPBasicAuth
from webdav4.client import Client
import os
import random
from pathlib import Path
from instagrapi import Client
from instagrapi.types import UserShort
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from pytumblr import TumblrRestClient
from requests_oauthlib import OAuth1Session

blogname = ""
current_path = Path.cwd()
print(current_path)

def split_text(text, font, max_width):
    lines = []
    words = text.split()
    current_line = ''
    for word in words:
        if draw.textbbox((0, 0), current_line + ' ' + word, font=font)[2] > max_width:
            lines.append(current_line.strip())
            current_line = ''
        current_line += ' ' + word
    lines.append(current_line.strip())
    return lines


while True:
    def get_quote(language=None):
        if language is None:
            language = random.choice(['de', 'en'])
            quote_response = requests.get(f'https://api.andyproject.de/v2/quotes/{language}/')
            quote_data = quote_response.json()
            quote = quote_data['quote']
            author = quote_data['author']
            length = quote_data['length']
            id1 = quote_data['id']
            return quote, id1, author, length 

            #gloabal variables
    author = "global author"
    quote = "global quote"

    # Get quote from API
    quote, id1, author, length = get_quote()

    # Check if quote is less than 200 characters
    while length > 200:
        quote, id1, author, length = get_quote()

    page = random.randint(1, 90)
    print(f"Bild wird von Seite {page} runtergeladen.")
    # Get image from Unsplash API
    url = f"https://api.pexels.com/v1/search?query=luxury car audi love life white black heart nature&page={page}&per_page=25&orientation=square"
    #not neccesary  
    #https://api.pexels.com/v1/search?query=audi%20love%20life%20white%20black%20heart%20nature&page={page}&per_page=25&orientation=square
    #querystring = {"query": "nature audi black white", "orientation": "square", "page": page, "per_page": "30"}

    headers = {
        "Authorization": "pexel-authorization-code",
    }
    response = requests.request("GET", url, headers=headers)

    json_data = response.json()
    total_res = json_data['total_results']
    print(f"Picture available: {total_res}")

    while True:
        try:
            rand = random.randint(1, 15)
            photo = json_data['photos'][rand]
            image_url = photo['src']['original']
            total_res = json_data['total_results']
            image = Image.open(requests.get(image_url, stream=True).raw)
            break  # Wenn keine Exception aufgetreten ist, breche die Schleife ab
        except IndexError:
            print(f"IndexError: Bild mit Index {rand} nicht gefunden. Versuche es erneut. Response: {total_res}")
            

    image = image.resize((2500, 2500))

    # Darken image by 40%
    image = ImageEnhance.Brightness(image).enhance(0.4)

    # Draw quote on image
    draw = ImageDraw.Draw(image)

    # Set font size based on image height
    font_size = int(image.height / 18)
    font = ImageFont.truetype(f'{current_path}/IndieFlower-Regular.ttf', font_size)
    

    image_width, image_height = image.size
    max_text_width = image_width - 300
    lines = split_text(quote, font, max_text_width)
    line_height = draw.textbbox((0, 0), 'A', font=font)[3]
    line_spacing = 40 # additional spacing between lines
    total_text_height = (line_height + line_spacing) * len(lines) - line_spacing
    y = (image_height - total_text_height) / 2
    for line in lines:
        text_width, text_height = draw.textbbox((0, 0), line, font=font)[2:]
        x = (image_width - text_width) / 2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height + line_spacing

    # Draw footer on image
    footer_text = f'@{insta_name}'
    footer_font_size = int(image.height / 17)
    footer_font = ImageFont.truetype(f'{current_path}/DancingScript-VariableFont_wght.ttf', footer_font_size)
    footer_width, footer_height = draw.textbbox((0, 0), footer_text, font=footer_font)[2:]
    footer_x = (image_width - footer_width) / 2
    footer_y = image_height - footer_height - 130
    draw.text((footer_x, footer_y), footer_text, fill='white', font=footer_font)

    # Save image
    img = str(f"tumb_") + str(id1) + str(".jpeg")
    # customize folder path
    image.save(f'/mnt/_onedrive_1704741445/public/tumblr_pic/{img}')
    
    # Set up Tumblr API credentials
    consumer_key = "consumer_key"
    consumer_secret = "consumer_secret"
    access_token = "access_token"
    access_secret = "access_secret"
    client = TumblrRestClient(consumer_key, consumer_secret, access_token, access_secret)

    # Define function to post image on Tumblr
    def post_image_on_tumblr(image_path):
        # Check if the file exists
        if not os.path.isfile(image_path):
            print(f"File {image_path} does not exist.")
            return

        #tags
        global author, quote
        #Tags can be changed here if necessary. Only tags_og
        tags_og = ['quotes', 'life', 'love', 'important', 'tumblr', 'instagood', 'aesthetic', 'girl', 'literature', 'sad quotes', 'sad poem', 'zitate', 'tumblrgirl', 'tumblrboy', 'aesthetictumblr', 'tumblrpost', 'tumblraesthetic', 'tumblrtextpost', 'tumblrposts', 'tumblrquotes', 'fotostumblr', 'funnytumblr', 'frasitumblr', 'tumblrgirls', 'tumblrfunny', 'tumblrphoto', 'tumblrpic', 'frasestumblr', 'tumblrtextposts', 'tumblrtee', 'kaostumblr', 'instatumblr', 'grungetumblr', 'tumblrteemurah', 'tumblrlife', 'tumblrpics', 'tumblrlove', 'tumblrstuff', 'cachostumblr', 'tumblrgrunge', 'tumblrphotos', 'tumblrpictures', 'tumblrboys', 'fototumblr', 'tumblrquote', 'tumblrstyle', 'tumblraccount', 'tumblrr', 'tumblrpicture', 'tumblrmemes', 'tumblrgram', 'goodvibes', 'goodvibesonly', 'onlygoodvibes', 'goodvibes✌', 'goodvibesalways', 'goodvibesonly✌', 'goodvibesonly✨', 'goodvibestribe', 'feelgoodvibes', 'spreadgoodvibes', 'instagoodvibes', 'goodvibesquotes', 'justgoodvibes', 'goodvibes✨', 'goodvibess', 'letteringgoodvibes', 'nothingbutgoodvibes', 'socalgoodvibes', 'pampagoodvibes', 'goodvibesplease', 'allgoodvibes', 'goodvibeschallenge', 'sendinggoodvibes', 'goodvibeslang', 'ibizagoodvibes', 'alwaysgoodvibes', 'thegoodvibes', 'goodvibesforever', 'goodvibesonlyplease', 'goodvibestour', 'sendgoodvibes', 'goodvibesforyou', 'goodvibesgoodlife', 'goodtimesgoodvibes', 'onlygoodvibes✨', 'feelinggoodvibes', 'goodvibestoday', 'goodvibesalltheway', 'mundogoodvibes', 'goodpeoplegoodvibes', 'love', 'instalove', 'loveit', 'lovely', 'mylove', 'naturelovers', 'loveyourself', 'loveyou', 'loveher', 'doglover', 'puppylove', 'selflove', 'iloveyou', 'lovehim', 'foodlover', 'catlover', 'ilovemydog', 'inlove', 'lovethem', 'lovelife', 'naturelover', 'lovequotes', 'doglovers', 'loveislove', 'lovemyjob', 'makeuplover', 'catlovers', 'truelove', 'lovedogs', 'ilovemycat', 'photographylovers', 'skylovers', 'babylove', 'loveofmylife', 'booklover', 'coffeelover', 'archilovers', 'ilovemyjob', 'fashionlover', 'lovers', 'smile', 'smiles', 'allsmiles', 'smiley', 'instasmile', 'smilemore', 'thatsmile', 'bigsmile', 'alwayssmile', 'makeyousmilestyle', 'smiler', 'smilealways', 'beautifulsmile', 'justsmile', 'dogsmile', 'keepsmile', 'fakesmile', 'smilers', 'smileyface', 'smileeveryday', 'smilesfordays', 'babysmiles', 'makesmesmile', 'bigsmiles', 'dontsmileatme', 'babysmile', 'smilemakeover', 'smiledesign', 'smilesformiles', 'prettysmile', 'happysmile', 'nosmile', 'hollywoodsmile', 'smilee', 'cutesmile', 'perfectsmile', 'smilesmilesmile', 'behappyandsmile', 'mysmile', 'goodsmilecompany']
        selected_tags = random.sample(tags_og, 15)
        tags = [author] + selected_tags
        # Post the image
        client.create_photo(
            "f'{blogname}'",
            state="published",
            tags=tags,
            data=image_path,
            caption=f"<i>{quote}</i><br><br><strong>~ {author}</strong>"
        )

    # Call the function with the path to your image
    # customize folder path
    post_image_on_tumblr(f'/mnt/_onedrive_1704741445/public/tumblr_pic/{img}')
    #Select a random number of seconds between 10000 and 12000. Can be customized.
    sekunden1 = random.randint(10000, 12000)
    #print(sekunden1)
    #Converting seconds into hours and minutes
    stunden, sekunden = divmod(sekunden1, 3600)
    minuten, sekunden = divmod(sekunden, 60)

    #Output result in hh:mm format
    zeitformat = "{:02d}:{:02d}".format(stunden, minuten)
    #print(zeitformat)
    print("Code-Status: Success")
    print(f"Next Post in {zeitformat} hours.")
    time.sleep(sekunden1)
