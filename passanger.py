#!/usr/bin/env python3
import argparse

import os.path
import sys


def main():
  # Create the parser
  arg_parser = argparse.ArgumentParser(description='List the content of a folder')

  # Add the arguments
  arg_parser.add_argument('Path',
                        metavar='path',
                        type=str,
                        help='the path to wordlist')

  # Execute the parse_args() method
  args = arg_parser.parse_args()

  input_path = args.Path

  if not os.path.exists(input_path) or not os.path.isfile(input_path):
    print('The path specified does not exist')
    sys.exit()


if __name__ == '__main__':
    main()