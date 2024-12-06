from itertools import combinations


def all_variants(text):
    for i in range(1, len(text)+1):
        obj = combinations(text, i)
        for j in obj:
            if ''.join(list((j))) in text:
                yield ''.join(list((j)))



a = all_variants("abcdfj")
for i in a:
    print(i)

