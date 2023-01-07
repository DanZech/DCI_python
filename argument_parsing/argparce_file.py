import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '-f',
    '--first_name',
    metavar='First name',
    type=str,
    nargs='?',
    help='Your first name',
    default='User'
)
parser.add_argument(
    '-a',
    '--age',
    metavar='Age',
    type=int,
    nargs='?',
    help='Enter your age'
)
run = parser.parse_args()
print('Hello', run.first_name)
if run.age:
    print('You are ', run.age, 'years old')
else:
    print('Age is not specified')



