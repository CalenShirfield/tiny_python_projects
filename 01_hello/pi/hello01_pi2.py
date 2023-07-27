#! /usr/bin/env python3
#shebang above tells OS which program to use to execute this program
#Purpose: Program to greet any user depending on input

#parser will figure out arguments
#name is now an optional argument and there is now a default value  
#description will appear in the help message


import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n','--name',metavar='name',default='World',
help='Name to greet')

args = parser.parse_args()

print('Hello, ' + args.name + '!')
