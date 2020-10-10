from re import search
from sys import argv

def is_email(txt):
    return not search("[a-z]+[.]{1}[a-z]+@{1}northeastern.edu$", txt) is None


def is_username(txt):
    return not search("[a-z]+[.]{1}[a-z]+", txt) is None


def get_username(email):
    return email.split('@')[0]


if is_email(argv[1]):
    print(get_username(argv[1]))
elif is_username(argv[1]):
    print(argv[1])
else:
    print("Wasn't a username or email")