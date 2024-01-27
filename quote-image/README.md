# tumblr-autopost-bot-picture
This bot uses the Andyproject API, the Pexels API and the Tumblr API to post images with sayings & quotes on Tumblr. Please follow the instructions to set up the bot.

# Info
To set up the bot, you need a server. The script has been tested under Ubuntu 20.04 LTS and Windows 11.

# Requirements
- A server or computer that runs 24/7.
- You need Python3 to run the script. Download [here](https://www.python.org/downloads/) for Windows or install with `apt-get install python3` with Linux
- Install required Librarys: 
1. `pip3 install requests`
2. `pip3 install pillow`
3. `pip3 install requests-auth`
4. `pip3 install instagrapi`
5. `pip3 install secure-smtplib`
6. `pip3 install pytumblr`
7. `pip3 install requests_oauthlib`


# Setup
- Visit [Tumblr Developers](https://api.tumblr.com/console/calls/user/info)
- Generate _consumer_key_ and _consumer_secret_ 
- Insert Consumer_Key, Consumer_Secret, Access_Token and Access_Secret in Script
- Insert your Tumblr Blogname
- Setup your Time (in sec) in which intervall the post should post.
- In code under "tags_og" you can specify hashtags for your quotes. These are separated with a comma
- In the current version of the code, the paths for the images must be adjusted manually. The images are not deleted.

# Run
- run the code with `python3 main.py`
The Bot should print "Code-Status: Success"

# Optional
If you use Linux and want to run the Bot as background process you can use "Screen"
- install screen with `apt-get install screen`
- type `screen` in console
- navigate to the script and start the bot
- close with "strg" + "a" + "d"
You can always control the process by typing `screen -r`<br>

# Auto start
In the following steps, I will explain how to set up the bot so that it starts automatically when the server is started. This instruction is only vor Linux systems.

- Download `tumblr-pic.sh`.
- Put the file on your Server.
- Make the file executable: `sudo chmod +x tumblr-pic.sh`. Make sure you using the right path.
- Put this command in crontab `@reboot /path/to/script/tumblr-pic.sh`.
- Be sure that the path in the tumblr-pic.sh file is the path to the python file. Please also make sure that screen is installed.
<br>
<br>
Now your bot should work fine
