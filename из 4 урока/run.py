import os
import time
import random
import numpy
import sys
import math
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--name', type = str)
parser.add_argument('--age', type = int)
parser.add_argument('--data_path', type = str, default = None)
parser.add_argument('--place', type = str, default='Shop')

args = parser.parse_args()
print(f"In our args {args}. Type {type(args.age)}")
print(f"Hello, {args.name}! You are {args.age}. You work in {args.place}")

