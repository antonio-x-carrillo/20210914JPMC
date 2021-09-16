from timeit import Timer

REPEATS = 1000000

setup_code = """
more_letters = 'l m n o p'.split()
"""

code_snippets = [
"""
letters = 'a b c d e f g h i j k'.split()
for letter in more_letters:
    letters.append(letter)
""",
"""
letters = 'a b c d e f g h i j k'.split()
letters.extend(more_letters)
"""
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup_code)
    print("{:60.60s}{}".format(code_snippet, t.timeit(REPEATS)))
    print('-' * 60)
