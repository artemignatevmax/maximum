def is_palindorm(string):
    return string.lower() == string[::-1].lower()

print(is_palindorm('шрерш'))

