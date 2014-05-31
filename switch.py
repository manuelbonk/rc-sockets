#!/usr/bin/python

# import required libraries
from bottle import route, run, get, static_file
from subprocess import call
import time

def setSwitch(switch, state):
    return "penis"

""" @route('/switch/<name>/<pos>')
 def index(name, pos):
   name = name.upper()
  pos = pos.upper()
  setSwitch(name, pos)
  return '<!doctype html><html><p style="font-family:sans-serif">%s</p></html>' % (pos)
  return 'Switch %s %s</b>' % (name, pos)
"""
@route ('/')
def index ():
    output = open ('index.html')
    return output

# static files
@route('/static/<filename>')
def server_static(filename):
        return static_file(filename,root='/home/m/dev/remote/static')

@route ('/switch/<code>/<pin>/<pos>')
# def call(["/home/m/dev/raspberry-remote/send",code,pin,pos])
def switch(code,pin,pos):
    call(["send",code,pin,pos])
    state="off"
    if pos == "1":
        state="on"
    return '<!doctype html><html><p style="font-family:sans-serif">code: %s<br/>turned switch %s %s</p></html>' % (code,pin,state)

run (host='0.0.0.0', port=8080)
