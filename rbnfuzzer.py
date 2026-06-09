import argparse

import requests


parser: argparse.ArgumentParser = argparse.ArgumentParser(prog='Fuzzer',
                                                          description='Fuzzing for directories list',
                                                          epilog='Help you')

parser.add_argument('-u', '--url')
parser.add_argument('-w', '--wordlist')

args: argparse.Namespace = parser.parse_args()

