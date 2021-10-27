#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    
    #print(*[str(key)+" "+str(val) for key,val in Counter(s).most_common()[0:3]],sep="\n")
    
    for key,val in sorted(sorted(Counter(s).items(), key=lambda x: x[0]), key=lambda x: x[1] ,reverse=True)[0:3]:
        print(key,val)

