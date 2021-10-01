import os
import requests
from settings import pid, apikey, apiurl, watchurl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import vids, engine
from tbot import channel_post

Session = sessionmaker(bind=engine)
session = Session()

def vidindb():
    videos = []
    for vid in session.query(vids):
        videos.append(vid.v_id)
    return(videos)

def dbinsert(title, id, date):
    vid = vids(title, id, date)
    session.add(vid)
    session.commit()

def get_videos(url):
    resp = requests.get(url)
    data = resp.json()
    return(data['items'])

def telegram_notify(content, v_date):
    channel_post(content, v_date)

if __name__ == '__main__':
    videos = get_videos(apiurl)
    vidsindb = vidindb()

    for video in videos:
        v_title = video['snippet']['title']
        v_id = video['snippet']['resourceId']['videoId']
        v_date = video['snippet']['publishedAt']

        if v_id not in vidsindb:
            dbinsert(v_title, v_id, v_date)
            content = watchurl + v_id
            telegram_notify(content, v_date)
