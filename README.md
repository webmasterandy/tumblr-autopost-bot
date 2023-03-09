# tumblr-autopost-bot
This bot use the Quotable API to post Quotes at Tumblr with the Tumblr API

# Info
To set up the bot, you need a server. The script has been tested under Ubuntu 20.04 LTS and Windows 11.

# Requirements
- A server or computer that runs 24/7.
- You need Python3 to run the script. Download [here](https://www.python.org/downloads/) for Windows or install with `apt-get install python3` with Linux
- Install required Librarys: 
1. requests `pip3 install requests`
2. json `pip3 install json`
3. pytumblr `pip3 install pytumblr`

# Setup
- Visit [Tumblr Developers](https://api.tumblr.com/console/calls/user/info)
- Generate _consumer_key_ and _consumer_secret_ 
- Insert Consumer_Key, Consumer_Secret, Access_Token and Access_Secret in Script
- Insert your Tumblr Blogname
- Setup your Time (in sec) in which intervall the post should post.
- In the code under "Tags" you can specify hashtags for your quotes. These are separated with a comma

# Run
- run the code with `python3 run.py`
The Bot schould print "Quote postet on Tumblr"

# Optional
If you use Linux and want to run the Bot as background process you can use "Screen"
- install screen with `apt-get install screen`
- type `screen` in console
- navigate to the script and start the bot
- close with "strg" + "a" + "d"
You can always control the process by typing `screen -r`

Now your bot should work fine
