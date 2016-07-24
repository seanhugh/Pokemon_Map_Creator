#!/usr/bin/env python
f = open('maps/map_0.txt', 'w')
f.write("hello")
f.close()
f = open('maps/map_0.txt', 'r')
text = f.read()
f.close()
print text