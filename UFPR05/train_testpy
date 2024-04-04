import random

# read everything in
lines = open("all.txt").readlines()

# randomise order
random.shuffle(lines)
n = int(len(lines)*0.75) 
# split array up and write out according to desired proportions
open('train.txt', 'w').writelines(lines[:n])
open('test.txt', 'w').writelines(lines[n:])