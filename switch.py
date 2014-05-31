#!/usr/bin/python

# import required libraries
from bottle import route, run, get, static_file
from subprocess import call

@route ('/')
def index ():
    output = open ('index.html')
    return output

# static files
@route('/static/<filename>')
def server_static(filename):
        return static_file(filename,root='/home/m/dev/remote/static')

@route ('/switch/<code>/<pin>/<pos>')
def switch(code,pin,pos):
    call(["./rcswitch-pi/send",code,pin,pos])
    state="off"
    if pos == "1":
        state="on"
    return '<!doctype html><html><p style="font-family:sans-serif">code: %s<br/>turned switch %s %s</p></html>' % (code,pin,state)

run (host='0.0.0.0', port=8080)
