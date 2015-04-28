#!/usr/bin/env python
# Author: Cody L. Kochmann
# Created: Sun Apr 26 15:34:51 PDT 2015
# Description: Clipboard tracker for OSX
# Version: 1.0

# Enter the path that you want via clipboard database 
# to be stored here.
clipboard_watcher_path = "/Users/$USER/"

import base64, subprocess, datetime, csv, time

def timestamp():
	return str(datetime.datetime.now()).split(".")[0]
	import os
	return os.popen("date").read().split("\n")[0]

def getClipboardData():
	p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
	retcode = p.wait()
	data = p.stdout.read()
	return data

def write_to_csv(input_array):
	global clipboard_watcher_path
	with open( clipboard_watcher_path + '/clipboard_watcher.csv', 'a') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter='|')
	    # Uncomment this if you need verbose logging to debug anything
	    # print "appending %s to clipboard_watcher.csv" % (input_array)
	    spamwriter.writerow(input_array)

previous_clipboard = ""

while True:
	tmp_clipboard = base64.b64encode(getClipboardData())
	if tmp_clipboard != previous_clipboard and len(tmp_clipboard) > 6:
		previous_clipboard = tmp_clipboard
		ts = timestamp()
		row_data = ts.split(' ') + [tmp_clipboard]
		write_to_csv(row_data)
	time.sleep(10)
