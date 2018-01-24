#!/bin/env python2
from remotsylib import api
import argparse
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store", type=str, required=True)
    parser.add_argument("-p", "--password", action="store", type=str, required=True)
    args =  parser.parse_args(sys.argv[1:])

    client = api.Api()

    #Do the login and get the token
    token = client.login(args.username, args.password)
    print "API Token", token

    #Get the list of the controls
    lst_ctl = client.list_controls()
    for ctl in lst_ctl:
        print ctl
        print "id %s Name %s" % (ctl["_id"], ctl['name'])

    #get the list of the available buttons for the first control
    lst_bto = client.list_buttons(lst_ctl[1]["_id"])
    for bto in lst_bto:
        if bto["key"] == "POWER OFF": #Get the Id of the POWER OFF
            print "id %s Key %s" % (bto["_id"], bto["key"])

            #Do the infrared blast using the IDDEV of the first control
            #and the id of the POWER OFF
            client.blast(lst_ctl[1]["iddev"], bto["_id"])
