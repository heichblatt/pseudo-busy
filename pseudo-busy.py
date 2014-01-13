#!/usr/bin/env python

import sys
import time
from random import randrange
from random import choice

with open('verbs') as f:
    verbs = f.read().splitlines()

with open('nouns') as f:
    nouns = f.read().splitlines()


with open('outcomes') as f:
    outcomes = f.read().splitlines()

try:
    while True:
    	sys.stdout.write(choice(verbs) + " " + choice(nouns) + "..    ")
    	sys.stdout.flush()
        time.sleep(randrange(3))
        print choice(outcomes)
except KeyboardInterrupt:
    exit("bye")