#!/usr/bin/env python

filename = "files/story.txt" # filename

# Let's use context manager for reading/writing a file
# This will remove a headache of opening and closing a file

with open(filename) as f:
    content = f.readlines()
    print(content) # What is the 'type' of the content?



