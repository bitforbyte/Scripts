#!/usr/bin/python3
import argparse
import sys
import re


def calcSleepTime(argc, argv):
    match = re.match(r'(\d+):(\d\d)', argv)

    if match is None:
        match = re.match(r'(\d*)', argv)
    hour = int(match.group(1))

    # Make sure input is greater than 12
    if (hour > 12):
        print("Must be between (1-12)")
        exit(1)
    
    count = 8

    # Loop through the 8 hours until 0 is reached and loop time
    while (count > 0):
        #print("hour %d" % hour)
        hour -= 1
        if hour == 0:
            hour = 12

        count -= 1

    # If the match is more than just a number
    if len(match.group()) > 2:
        print("%d:%s" % (hour, match.group(2)))
    else:
        print("%d:00" % (hour))


if __name__ == "__main__":
    # If the arguments aren't 2 print message
    if (len(sys.argv) != 2):
        print("Description: Program will calculate the best time to sleep to get 8 hours of sleep for an alarm\n")
        print("Usage:")
        print(" sleepTime {1-12}")
        print(" sleepTime {1-12}:{00-59}")
        print(" sleepTime {1-12}:{00-59}{am/pm}")
    elif (sys.argv[1] == '0'):
        print("0 not an argument")
    else:
        input = sys.argv[1]
        try:
            val = int(input)
        except ValueError:
            match = re.match(r'(^\d*):(\d\d([ap]m)?$)', input)
            if match is None: 
                print("Error Wrong input")
                exit(1)

        calcSleepTime(len(sys.argv), str(sys.argv[1]))
