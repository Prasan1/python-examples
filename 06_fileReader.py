
#!/usr/bin/env python

fileName = "story.txt"

with open(fileName) as f:
    content = f.readlines();


print("%s\n" %content);

