'''
The application in this file will read the command line options using `sys.argv`.

If one of the options is `--help`, it should output a small help text.

If one of the options is `--fast` is should print the text "fast mode enabled" to the command line.

If `--fast` is not one of the options it should print the text "slow mode enabled" to the command line.

'''

import sys

file_name = sys.argv[0]
other_data = sys.argv[1:]

if '--help' in other_data:
    print('What is your problem?')

elif '--fast' in other_data:
    print('fast mode enabled')

else:
    print('slow mode enabled')

