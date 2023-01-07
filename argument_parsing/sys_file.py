import sys

file_name = sys.argv[0]
other_data = sys.argv[1:]

if '-h' in other_data or '--help' in other_data:
    print('this is help message')
elif '-i' in other_data or '--install' in other_data:
    print('Modul installed')
