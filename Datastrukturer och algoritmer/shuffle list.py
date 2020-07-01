import random
file = open("glossor.txt", 'r')
h = file.read().split('\n')[:-1]
random.shuffle(h)
for i in h:
    print(i)
