#!/usr/bin/env python

import tail

def print_line(txt):
    ''' Prints received text '''
    print(txt)

t = tail.Tail('/root/a.txt')
# Register a callback function to be called when a new line is found in the followed file.
# If no callback function is registerd, new lines would be printed to standard out.
t.register_callback(print_line)
 
# Follow the file with 2 seconds as sleep time between iterations.
# If sleep time is not provided 1 second is used as the default time.
t.follow(s=1)

