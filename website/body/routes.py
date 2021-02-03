from website import app
from flask import Flask, render_template, request, flash, redirect, url_for
import json, os,datetime


basedir = os.getcwd()
profiles_path = basedir+"\\website\\data\\contributors\\"
# print(profiles_path)
profiles = os.listdir(profiles_path)
# print(profiles)
# for p in profiles:
    # print(p)

class profile:
    # def __init__(self,name,avatar,cover,github,linkedin,twitter):
    def __init__(self,name,avatar,cover,lang,github,linkedin,twitter):
        self.name = name
        self.avatar = avatar
        self.cover = cover
        self.lang = lang
        self.github = github
        self.linkedin = linkedin
        self.twitter = twitter
        
contributors = []

for p in profiles:
        with open(profiles_path + p, 'r') as c:
            params = json.load(c)
        contributors.append( profile(params['name'],params['avatar'],params['cover'],params['lang'],params['github'],params['linkedin'],params['twitter']) )

now = datetime.datetime.now()
curr_yr = now.year

@app.route('/')
def home():
    
    return render_template('/index.html',contributors=contributors,curr_yr=curr_yr)