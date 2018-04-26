#!/usr/bin/env python3

import sys, getopt
import plumb
import pdb
import os
import pprint

def main(argv):
    verbose = False
    test = False
    dbase = "folder.db"
    cash = ""
    add = ""
    remove = ""
    try:
        opts, args = getopt.getopt(argv, "a:r:d:c:hvt", ["help", "verbose", "test", "dbase=", "cash=", "add=", "remove="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-t", "--test"):
            test = True
        elif o in ("-h", "--help"):
            usage()
            exit()
        elif o in ("-d", "--dbase"):
            dbase = a
        elif o in ("-a", "--add"):
            add = a.upper()
        elif o in ("-c", "--cash"):
            cash = a
        elif o in ("-r", "--remove"):
            remove = a.upper()
        else:
            assert False, "unhandled option"
    if (test):
        testResult = plumb.TestFolder(verbose)
        if (testResult):
            print ("Test result - pass")
        else:
            print ("Test result - fail")
        exit()
    print ("\tdbase: {0}".format(dbase))
    if (cash > ""):
        cashResult = plumb.Cash(cash, dbase, verbose)
        if (cashResult):
            print ("balance updated.")
        else:
            print ("failed.")
        exit()
    if (add > ""):
        addResult = plumb.Add(add, dbase, verbose)
        if (addResult):
            print ("added.")
        else:
            print ("failed.")
        exit()
    if (remove > ""):
        removeResult = plumb.Remove(remove, dbase, verbose)
        if (removeResult):
            print ("removed.")
        else:
            print ("failed.")
        exit()
    usage()

def usage():
    usage = """
    *******************
    **  Folder Tool  **
    *******************

    -h --help           Prints this help
    -v --verbose        Increases the information level
    -t --test           tests the folder routines
    -d --dbase          override database name (folder.db is the default)
    -c --cash           enter your cash balance in dollars
    -a --add            add company by ticker symbol
    -r --remove         remove company by ticker symbol
    -s --symbol         ticker symbol (used with --number or --balance)
    -n --number         number of shared owned (used with --symbol)
    -b --balance        balance in dollars (used with --symbol)
    """
    print (usage) 

if __name__ == "__main__":
  main(sys.argv[1:])
