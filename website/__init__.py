from flask import Flask, render_template, request, flash
import json, os



app = Flask(__name__)
app.secret_key = 'magnewskey'




from website.body import routes