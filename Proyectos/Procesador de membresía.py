from doctest import ELLIPSIS_MARKER
from sqlite3 import enable_shared_cache


name_box = "Alice Bentall"
age_box = "20"
uni_box = ""
subs_box = "1.99"
mkt_box = "0"

name_entered = bool(name_box)
print(name_entered)

if name_entered:
    name = name_box
else:
    name = "Unknown"
print(name)

age = int(age_box)
student = bool(uni_box)
print(age)
print(student)

subscription = float(subs_box)
print(subs_box)

marketing = bool(int(mkt_box))
print(marketing)

profile = name + ', ' + str(age)
print(profile)

