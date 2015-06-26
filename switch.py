#!/usr/bin/python

# import required libraries
from bottle import route, run, get, static_file, redirect
from subprocess import call

@route('/')
@route('index.html')
def index():
    return static_file("index.html",root='/home/m/dev/remote/static/')

# static files
@route('/static/<filename>')
def server_static(filename):
        return static_file(filename,root='/home/m/dev/remote/static/')

@route ('/<mode>/<code>/<pin>/<pos>')
def switch(mode,code,pin,pos):
    call(["./rcswitch-pi/send",code,pin,pos])
    state="off"
    if pos == "1":
        state="on"
    if mode == "verbose":
        return '<!doctype html><html><p style="font-family:sans-serif;font-size:18px">code: %s<br/>turned switch %s %s</p></html>' % (code,pin,state)
    return '<!doctype html><html><p style="font-family:sans-serif;font-size:18px">%s</p></html>' % (state)

run (host='0.0.0.0', port=8080)
