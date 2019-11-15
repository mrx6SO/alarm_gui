#!/usr/bin/python2
# -*- coding: utf-8 -*- 

# the basic modules

import webbrowser #for implementation with some website... if u want this
import Tkinter,easygui
import sys
import string
from time import sleep

# variables 

sa = sys.argv
lsa = len(sys.argv)

while 1: # the loop 

    if lsa != 2: # if arguments are equals or differents from two, show the help
                 # because the variable lsa receive two parameters 
                 # are them, the location to path of script and the time, in minutes 

        print "\nUsage: [python] %s [duration_in_minutes]\n" %(sa)
        print "\nExample: [python] %s 10\n" %(sa)
        print "\nBeeps a few times and pop up a window after the duration is over (Windows only)\n"
        print "\nPress Ctrl-C to terminate the clock early\n"

        sys.exit(5)  

    try:

        minutes = int(sa[1]) # will keep the value passed to the script

    except ValueError: # except if some error occurred...

        print "Invalid numeric value (%s) for minutes" % sa[1]
        print "Should be an integer >= 0"

        sys.exit(5)
    
    if minutes <= 0: # if minutes minor or equal to zero, just pass to next block

        pass

    if minutes < 0: # if minutes minor than zero, put out the error

        print "\nWrong range... %s\nDo the math\n" % sa[1]
        print "\nLeaving...\n"
        sys.exit(0x0)
  
    seconds = minutes * 60 # variable seconds with a logical tought
                           # cause if 1 multiplicated for 60 is equal to 60, whatsoever, we'll be 60...
                           # if i have 1(second) and i multiplicate this number for 60, i'll had 60. 
                           # so this 60 will be keeped in the variable minutes, allready declared in the init of the code
                           # so, this is the 'formula' to check how minutes the user put in the program 

    if minutes == 1: # here is to guaranteed to give minute and minutes correctly
        unit_word = " minute"

    else: # if != 1 will be minutes 
        unit_word = " minutes"

    try:

        if minutes > 0: # if all occurred without errors, this will be executed
            print "\nSleeping for... " + str(minutes) + unit_word
            sleep(seconds) # using the variable seconds

        #print '\n'

        print '\a\a\a\a' # this was supposed to play some sound at the end of loop, but just on Windows is possible

        easygui.msgbox("You have a warning... don't be late.", title="Work time!")

        #webbrowser.open("https://www.youtube.com/watch?v=MeZ8uVIOIhM")
        ## em webbroser.open() você pode escolher qualquer url que reproduza som, vídeo etc. Para lembrá-lo do alarme. 
        #print "\nCheck your DG coins!\n"

        for i in range(5):
            print chr(7),
            sleep(2)
    
    except KeyboardInterrupt:
        print "\nInterrupted by user!\n"
        sys.exit(5)
