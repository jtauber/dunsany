#!/usr/bin/env python3

sections = open("raw-pg/pg7477.txt").read().split("\n\n\n\n")
n = 0
for num, section in enumerate(sections):
    if num in range(5, 21):
        with open(f"raw-text/02_{n:02d}.txt", "w") as g:
            print(section, file=g)
        n += 1


sections = open("raw-pg/pg8129.txt").read().split("\n\n\n\n\n")

n = 0
for num, section in enumerate(sections):
    if num in range(6, 23):
        with open(f"raw-text/01_{n:02d}.txt", "w") as g:
            print(section, file=g)
        n += 1


sections = open("raw-pg/pg13821.txt").read().split("\n\n\n\n\n\n")

n = 0
for num, section in enumerate(sections):
    if num in range(2, 22):
        first_line = section.split("\n")[0]
        with open(f"raw-text/03_{n:02d}.txt", "w") as g:
            print(section, file=g)
        n += 1
