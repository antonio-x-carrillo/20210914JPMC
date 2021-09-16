import re
ignore_case = True

#  A ? B : C
# B if A else C

actor = "Chris Hemsworth"

m = re.search("^chr", actor, re.I if ignore_case else 0)
if m:
    print(m.group())
