import random
file = open("glossor.txt", 'r')
h = file.read().split('\n')
random.shuffle(h)
for i in h:
    input(i)
