from random import random as R
file = open("glossor.txt", 'r')

print(R.shuffle(file.read().split('\n')[:-1]))
