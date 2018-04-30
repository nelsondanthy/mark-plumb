#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import daemon
import time
import os
import getpass
from datetime import datetime
import pdb

import plumb

def do_something():
    while True:
        defaults = plumb.GetDefaults(False)
        begin = defaults['begin_time']
        if (begin is None):
            begin = "08:30"
        end = defaults['end_time']
        if (end is None):
            end = "16:00"
        weekno = datetime.today().weekday()
        ct = datetime.now().time()
        if "AM" in begin or "PM" in begin:
            bt = datetime.strptime(begin, '%I:%M%p').time()
        else:
            bt = datetime.strptime(begin, '%H:%M').time()
        if "AM" in end or "PM" in end:
            et = datetime.strptime(end, '%I:%M%p').time()
        else:
            et = datetime.strptime(end, '%H:%M').time()
        filename = "/tmp/{0}_folder_daemon.txt".format(getpass.getuser())
        if weekno < 5 and ct > bt and ct < et:
            plumb.Update(False)
            with open(filename, "w") as f:
                f.write("pid: {0}, {1} updated on: {2}. (sleeping for {3} seconds)".format(os.getpid(), defaults['aim_folder'], time.ctime(), defaults['daemon_seconds']))
        else:
            with open(filename, "w") as f:
                f.write("pid: {0}, open: {1}, close: {2}".format(os.getpid(), bt, et))
        if (defaults['daemon_seconds'] is None):
            time.sleep(1200)        # 20 minutes (1200 seconds)
        else:
            time.sleep(defaults['daemon_seconds'])

def run():
    with daemon.DaemonContext(working_directory=os.getcwd()):
        do_something()

if __name__ == "__main__":
    run()

