#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    radius = int(input())

    height = int(input())
    
    ans=3.14*radius*radius*height
    print("%.2f" %ans)
