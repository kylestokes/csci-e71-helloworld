import sys

# Check that there are 2 command line arguments
# Referenced: https://www.askpython.com/python/python-command-line-arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide name.')

# Get name from command line
name = sys.argv[1]

# Print to the console
print(f'Hello, {name}!')