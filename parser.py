import argparse

def init():
  # Create the parser
  arg_parser = argparse.ArgumentParser(description='List the content of a folder')

  # Add the arguments
  arg_parser.add_argument('Path',
              metavar='path',
              type=str,
              help='the path to wordlist'
            )

  return arg_parser