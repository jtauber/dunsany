#!/usr/bin/env python3


CONTINUED_QUOTES = [
    ('01_02', 5, 1), ('01_02', 6, 1), ('01_02', 7, 1), ('01_02', 8, 1),
    ('01_02', 9, 1), ('01_02', 10, 1), ('01_02', 12, 1),
    ('01_03', 11, 1), ('01_03', 12, 1), ('01_03', 13, 1), ('01_03', 14, 1),
    ('01_03', 15, 1),
    ('01_08', 5, 1), ('01_08', 6, 1), ('01_08', 7, 1), ('01_08', 8, 1),
    ('01_08', 12, 1), ('01_08', 13, 1), ('01_08', 14, 1), ('01_08', 15, 1),
    ('01_08', 16, 1), ('01_08', 17, 1), ('01_08', 21, 1), ('01_08', 22, 1),
    ('01_08', 23, 1), ('01_08', 24, 1), ('01_08', 25, 1), ('01_08', 28, 1),
    ('01_08', 29, 1), ('01_08', 30, 1), ('01_08', 31, 1), ('01_08', 32, 1),
    ('01_08', 33, 1), ('01_08', 34, 1), ('01_08', 35, 1),
    ('01_09', 5, 6), ('01_09', 6, 1), ('01_09', 7, 1), ('01_09', 8, 1),
    ('01_09', 9, 1), ('01_09', 10, 1), ('01_09', 11, 1), ('01_09', 12, 1),
    ('01_09', 13, 1), ('01_09', 14, 2), ('01_09', 15, 1),
    ('01_10', 4, 1), ('01_10', 5, 1), ('01_10', 6, 1), ('01_10', 7, 1),
    ('01_10', 8, 1), ('01_10', 9, 1), ('01_10', 10, 1), ('01_10', 11, 1),
    ('01_10', 12, 1), ('01_10', 13, 1), ('01_10', 14, 1), ('01_10', 15, 1),
    ('01_10', 16, 1), ('01_10', 17, 1), ('01_10', 18, 1), ('01_10', 19, 1),
    ('01_10', 20, 1), ('01_10', 21, 1), ('01_10', 22, 1), ('01_10', 23, 1),
    ('01_11', 18, 1), ('01_11', 19, 1), ('01_11', 20, 1),
    ('01_16', 19, 2),
    ('03_01', 3, 1), ('03_01', 4, 1), ('03_01', 5, 1), ('03_01', 8, 4),
    ('03_01', 11, 4), ('03_01', 12, 1),
    ('03_13', 4, 1), ('03_13', 5, 1), ('03_13', 6, 1), ('03_13', 7, 1),
]

A = [  # apostrope
    ('01_04', 20, 1, 20, None),
    ('01_06', 56, 2, 53, None),
    ('01_06', 57, 0, 18, None),
    ('01_06', 57, 2, 41, None),
    ('01_06', 58, 11, 67, None),
    ('01_09', 16, 21, 34, 1),
    ('01_10', 20, 5, 28, 1),
    ('01_12', 6, 16, 65, None),
    ('01_12', 47, 3, 41, None),
    ('01_15', 1, 12, 16, None),
    ('01_16', 8, 5, 67, 2),
    ('02_01', 5, 2, 69, None),
    ('02_01', 6, 9, 52, None),
    ('02_01', 6, 18, 36, None),
    ('02_01', 6, 19, 25, None),
    ('02_02', 2, 10, 22, 1),
    ('02_02', 3, 5, 49, None),
    ('02_04', 5, 4, 60, None),
    ('02_06', 12, 6, 47, None),
    ('02_07', 2, 1, 19, None),
    ('02_07', 4, 10, 67, None),
    ('02_07', 5, 0, 59, None),
    ('02_09', 2, 2, 69, None),
    ('02_09', 4, 2, 51, None),
    ('02_09', 5, 2, 9, None),
    ('02_09', 10, 1, 33, None),
    ('02_09', 15, 4, 9, None),
    ('02_09', 15, 5, 9, None),
    ('02_10', 10, 8, 62, None),
    ('02_12', 8, 3, 49, None),
    ('02_14', 22, 6, 30, None),
    ('03_01', 8, 4, 24, 2),
    ('03_02', 7, 5, 34, None),
    ('03_02', 13, 2, 13, None),
    ('03_02', 13, 9, 53, None),
    ('03_02', 15, 1, 9, 2),
    ('03_02', 23, 9, 30, None),
    ('03_03', 10, 6, 39, None),
    ('03_03', 16, 35, 5, None),
    ('03_06', 1, 1, 46, None),
    ('03_06', 12, 23, 66, None),
    ('03_06', 13, 0, 1, 1),
    ('03_06', 13, 1, 36, 2),
    ('03_07', 9, 11, 8, None),
    ('03_07', 11, 13, 10, None),
    ('03_11', 1, 0, 29, None),
    ('03_11', 1, 7, 11, None),
    ('03_11', 3, 6, 37, None),
    ('03_12', 7, 3, 9, None),
    ('03_12', 14, 15, 15, None),
    ('03_12', 23, 5, 15, 2),
    ('03_12', 32, 1, 13, 2),
    ('03_12', 36, 13, 34, None),
    ('03_12', 38, 7, 37, None),
    ('03_12', 44, 5, 60, None),
    ('03_12', 44, 10, 41, None),
    ('03_12', 52, 8, 25, None),
    ('03_12', 52, 13, 62, None),
    ('03_12', 69, 1, 53, None),
    ('03_12', 71, 0, 8, None),
    ('03_12', 74, 5, 7, None),
    ('03_13', 4, 6, 23, 1),
    ('03_17', 4, 2, 65, None),
    ('03_17', 8, 1, 66, None),
    ('03_17', 10, 4, 18, None),
    ('03_17', 18, 0, 17, None),
    ('03_17', 21, 3, 59, None),
    ('03_17', 21, 11, 66, None),
    ('03_18', 1, 16, 66, None),
    ('03_19', 2, 1, 23, None),
    ('03_19', 6, 3, 44, None),
]

B = [  # open single quote
    ('01_01', 7, 0, 60, 1),
    ('01_02', 2, 10, 65, 1),
    ('01_02', 6, 0, 31, 1),
    ('01_02', 8, 0, 1, 1),
    ('01_02', 10, 0, 1, 1),
    ('01_08', 5, 7, 42, 1),
    ('01_08', 6, 1, 0, 1),
    ('01_08', 13, 0, 54, 1),
    ('01_08', 14, 0, 64, 1),
    ('01_08', 15, 0, 1, 1),
    ('01_08', 15, 0, 38, 1),
    ('01_08', 16, 0, 67, 1),
    ('01_08', 23, 0, 1, 1),
    ('01_08', 23, 0, 42, 1),
    ('01_08', 26, 3, 8, 1),
    ('01_08', 29, 0, 1, 1),
    ('01_08', 31, 0, 1, 1),
    ('01_09', 5, 37, 48, 6),
    ('01_11', 18, 6, 0, 1),
    ('01_11', 18, 6, 36, 1),
    ('03_01', 6, 5, 46, 1),
    ('03_19', 29, 1, 29, 1),

]

C = [  # close single quote
    ('01_01', 7, 0, 64, 1),
    ('01_02', 2, 11, 24, 1),
    ('01_02', 6, 0, 63, 1),
    ('01_02', 8, 0, 24, 1),
    ('01_02', 10, 0, 20, 1),
    ('01_08', 5, 9, 18, 1),
    ('01_08', 6, 2, 41, 1),
    ('01_08', 13, 2, 10, 1),
    ('01_08', 14, 3, 23, 1),
    ('01_08', 15, 0, 7, 1),
    ('01_08', 15, 2, 24, 1),
    ('01_08', 16, 4, 50, 1),
    ('01_08', 23, 0, 12, 1),
    ('01_08', 23, 2, 43, 1),
    ('01_08', 26, 3, 30, 1),
    ('01_08', 30, 0, 1, 1),
    ('01_09', 5, 38, 7, 6),
    ('01_11', 18, 6, 3, 1),
    ('01_11', 18, 6, 44, 1),
    ('03_01', 6, 5, 62, 1),
    ('03_19', 29, 2, 35, 1),
]



def convert_text(identifier):
    global next_quote_continues

    with open(f"xml/{identifier}.xml", "w") as g:
        text = open(f"raw-text/{identifier}.txt").read()

        next_quote_continues = False

        def print_para(n, para):
            global next_quote_continues

            in_quote = None
            in_italics = False
            quote_count = 0
            print(f'  <p n="{n}">', end="", file=g)
            for line_num, line in enumerate(para.strip().split("\n")):
                line = line.replace("--", "—")
                converted_line = ""
                for ch_num, ch in enumerate(line):
                    if ch == "'":
                        if line[ch_num - 1].isalpha() and ch_num + 1 < len(line) and line[ch_num + 1] == "s":
                            converted_line += "’"
                        elif line[ch_num - 1] == "n" and ch_num + 1 < len(line) and line[ch_num + 1] == "t":
                            converted_line += "’"
                        elif (identifier, n, line_num, ch_num, in_quote) in A:
                            converted_line += "’"
                        elif (identifier, n, line_num, ch_num, in_quote) in B:
                            converted_line += "<q>"
                        elif (identifier, n, line_num, ch_num, in_quote) in C:
                            converted_line += "</q>"
                        else:
                            print()
                            print(line)
                            print((" " * ch_num) + "^")
                            print(identifier, n, line_num, ch_num, in_quote)
                            quit()
                    elif ch == '"':
                        if not in_quote:
                            quote_count += 1
                            in_quote = quote_count
                            if (identifier, n, quote_count) in CONTINUED_QUOTES:
                                if next_quote_continues:
                                    converted_line += '<q type="continued" rend="noclose">'
                                else:
                                    converted_line += '<q rend="noclose">'
                                next_quote_continues = True
                            else:
                                if next_quote_continues:
                                    converted_line += '<q type="continued">'
                                else:
                                    converted_line += "<q>"
                                next_quote_continues = False
                        else:
                            converted_line += "</q>"
                            in_quote = None
                    elif ch == "_":
                        if not in_italics:
                            if ch_num == 0 or line[ch_num - 1] in " —\"":
                                converted_line += "<hi>"
                                in_italics = True
                            else:
                                print()
                                print(line)
                                print((" " * ch_num) + "^")
                                print(identifier, n, line_num, ch_num, in_quote)
                                quit()
                        else:
                            if ch_num == len(line) - 1 or line[ch_num + 1] in " .,?'\"":
                                converted_line += "</hi>"
                                in_italics = False
                            else:
                                print()
                                print(line)
                                print((" " * ch_num) + "^")
                                print(identifier, n, line_num, ch_num, in_quote)
                                quit()
                    else:
                        converted_line += ch
                print(file=g)
                print(f"    {converted_line}", end="", file=g)
            if in_quote:
                if (identifier, n, in_quote) in CONTINUED_QUOTES:
                    print("</q>", end="", file=g)
                else:
                    print("@@@", identifier, n, in_quote)
                    quit()
            print(file=g)
            print("  </p>", file=g)

        print("<div>", file=g)
        state = 0
        n = 1
        for para in text.split("\n\n"):
            if state == 0:
                print(f"  <head>{para}</head>", file=g)
                state = 1
            elif state == 1:
                print_para(n, para)
                n += 1
                state = 2
            elif state == 2:
                print_para(n, para)
                n += 1
        print("</div>", file=g)


for story_num in range(17):
    if story_num != 8:
        convert_text(f"01_{story_num:02d}")
for story_num in range(16):
    convert_text(f"02_{story_num:02d}")
for story_num in range(20):
    convert_text(f"03_{story_num:02d}")
