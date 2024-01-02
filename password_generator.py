import argparse
import random
import string



# --------------------- Create a parser and add options --------------------- #

# Creating a parser using the ArgumentParser class
parser = argparse.ArgumentParser(
    prog='Password Generator',
    description='Utility for generating passwords according to a given template that supports the CLI interface.',
    epilog='Thanks for using %(prog)s!')

# Adding options
parser.add_argument('-n', type=int,
                    help='''Set length of password and generate random password
                    from set {small lateral ASCII, big lateral ASCII, digit}''')

parser.add_argument('-t', '--template',
                    help='Set template for generate passwords')

parser.add_argument('-f', '--file',
                    help='Getting list of patterns from file and generate for each random password')

parser.add_argument('-c', '--count', nargs='?', default=1, type=int,
                    help='Number of passwords')

parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='Verbose mode (-v |-vv |-vvv )')

parser.add_argument('-S', '--set', nargs='?', default='',
                    help='Character set')

parser.add_argument('-p', '--permute',
                    help='Randomly permute characters of password')

# Call .parse_args() on the parser to get the Namespace of arguments.
args = parser.parse_args()
# print(args)
# print(type(args))
# print(args.set)


# ------------------------ Definition of placeholders ------------------------ #

# Digit
# d = '0123456789'
d = string.digits

# Lower-Case Letter
# l = 'abcdefghijklmnopqrstuvwxyz'
l = string.ascii_lowercase

# Upper-Case Letter
# u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
u = string.ascii_uppercase

# Mixed-Case Letter
# L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
L = string.ascii_letters

# Punctuation
#---   string.punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~  ---#
p = string.punctuation


# ------------------------------ Random method ------------------------------ #

# Function that extends the Unicode character set or set {small lateral ASCII, big lateral ASCII, digit}
# from a user defined characters specified in the argument line
def extend_charset(charset):
    pick_set = input('Use characters from set {small lateral ASCII, big lateral ASCII, digit, punctuation}? (y/yes): ').lower()
    if pick_set == 'y' or pick_set == 'yes':
        extended_charset = set(charset) | set(L + d + p)
        return ''.join(extended_charset)

# Function that generates a random password from the Unicode character set and user defined character set
def generate_password(lenght_password, num_password, charset):
    extended_charset = extend_charset(charset)
    passwords = []
    for i in range(num_password):
        password = ''.join(random.choices(extended_charset, k=lenght_password))
        passwords.append(password)
    
    if num_password > 1:
        return f'List of passwords: {passwords}'
    else:
        return f'Password: {passwords[0]}'


# Calling the "generate_password" function
try:
    print(generate_password(args.n, args.count, args.set))
    
except Exception:
    print('# for more information call -h(--help) command')


# ----------------------- Pattern-based generation method ----------------------- #