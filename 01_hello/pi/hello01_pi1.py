#! /usr/bin/env python3
#shebang above tells OS which program to use to execute this program
#Purpose: Program to greet any user depending on input

#parser will figure out arguments 
#description will appear in the help message


import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name',help='Name to greet')
args = parser.parse_args()

print('Hello, ' + args.name + '!')
