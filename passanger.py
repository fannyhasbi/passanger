#!/usr/bin/env python3
import os.path
import sys

import parser

def main():
  arg_parser = parser.init()

  # Execute the parse_args() method
  args = arg_parser.parse_args()

  input_path = args.Path

  if not os.path.exists(input_path) or not os.path.isfile(input_path):
    print('The path specified does not exist')
    sys.exit()


if __name__ == '__main__':
    main()