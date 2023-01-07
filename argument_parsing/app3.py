'''

# The application in this file will read the command line options using argparse.
# This application should support positional arguments and be called like this: ./app3.py [FIRST_NAME] [LAST_NAME] [AGE]
# If age is not specified, it should be assumed that it is 100.
# If the last name is not specified, it should be assumed that it is "Hanson".
# If the first name is not specified, should be assumed that it is "Larry".
# This application should also support the option --fast. It should print "fast mode enabled"
# if this is one of the options.
# The app should then output the text "Hello [FIRST_NAME] [LAST_NAME]! I see that you have had [AGE + 1] birthdays.".

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '-f',
    '--first_name',
    metavar='First name',
    type=str,
    nargs='?',
    help='Your first name',
    default='Larry'
)
parser.add_argument(
    '-ln',
    '--last_name',
    metavar='last name',
    type=str,
    nargs='?',
    help='Enter your last name',
    default='Hanson,'
)

parser.add_argument(
    '-a',
    '--age',
    metavar='Age',
    type=int,
    nargs='?',
    help='enter your age',
    default=99,
)

parser.add_argument(
    '--fast',
    metavar='Fast mode',
    type=str,
    nargs='?',
    help='fast mode enable',
    default='fast mode enabled'
)


run = parser.parse_args()
# print('fast mode enabled')
print('Hello', run.first_name, run.last_name, "! I see that you have had ", run.age +1, "birthdays." )
print(run.fast)

'''