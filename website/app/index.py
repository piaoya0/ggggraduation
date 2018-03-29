#-*-coding:utf8-*-

from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import hashlib
import sql

app = Flask(__name__)
app.debug = True

@app.route('/index')
def index():
    # music_info = {}
    # comments = {"11630":["info", {"cc":"123456", "dd":"111111"}], "11631":["info2", {"yy":"123456789", "zz":"999999999"}]}
    return render_template("index.html", info = comments)

@app.route('/usermap')
def usermap():
    area = sql.sql('cs')
    nw = {}
    for x in area.get_nw():
        nw[x[0].encode('utf8')] = x[1:]
    usermap = []
    name = 'name'
    value = 'value'
    for x in area.get_usermap():
        usermap.append({name:x[0],value:x[1]})
    # maxnum = max([x for x in usermap])
    # usermap = area.get_usermap()
    return render_template("render.html", nw = nw)

@app.route('/signin', methods = ['POST'])
def signin(data):
    user = sql.sql('cs')
    password = hashlib.sha224(password).hexdigest()
    # user.insert(user,name)


if __name__ == "__main__":
    app.run()