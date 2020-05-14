#!/usr/bin/env python3
import os.path
import sys
from itertools import permutations

import parser

# final result
result = []


def permutate(words):
  if len(words) == 0 :
    result.append(words[0])

  possible_pass = permutations(words)
  possible_pass = list(possible_pass)
  
  for i in possible_pass:
    print(''.join(i))
  

def main():
  arg_parser = parser.init()

  # Execute the parse_args() method
  args = arg_parser.parse_args()

  input_path = args.Path

  if not os.path.exists(input_path) or not os.path.isfile(input_path):
    print('The path specified does not exist')
    sys.exit()

  words = []
  with open(input_path) as fp:
    for line in fp: 
      line = line.strip()
      words.append(line)

  permutate(words)

if __name__ == '__main__':
    main()