# youtube-telegram-bot
This [Telegram](https://telegram.org/) bot will message your group when a youtube user uploads a video. It's all written in Python3.6. SQLAlchemy is used to store uploaded video data, such as title, date and the video id.

You are going to have to generate a few apikeys to get this script working (the tricky part). See `settings.py` for more information.

# Installation
Create virtualenv and install requirements:
```
$ mkvirtualenv --python=/usr/bin/python3 youtube-telegram-bot
$ pip install -r requirements.txt
```
Edit `settings.py`.
Create database:
```
$ python db.py
```
Test your bot:
```
$ python yt-telegram-bot.py
```
Add this to `crontab` to schedule the script (will execute every 5th minute).
```
*/5 * * * *	virtualenvs/youtube-telegram-bot/bin/python /home/user/youtube-telegram-bot/yt-telegram-bot.py
```
