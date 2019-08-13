"""
generic merge function to merge already sorted arrays
"""


def merge_sorted(sa1, sa2, cmp):
    s = []

    j = 0
    k = 0

    while j < len(sa1) and k < len(sa2):
        if cmp(sa1[j], sa2[k]) == -1:
            s.append(sa1[j])
            j += 1
        else:
            s.append(sa2[k])
            k += 1

    while j < len(sa1):
        s.append(sa1[j])
        j += 1

    while k < len(sa2):
        s.append(sa2[k])
        k += 1

    return s


def comr(a, b):
    if a == b:
        return 0
    if a < b:
        return -1
    return 1


print(merge_sorted([1, 2, 4], [1, 3, 5], comr) == [1, 1, 2, 3, 4, 5])


class Test:
    def __init__(self, val):
        self.val = val

    @staticmethod
    def cmp(a, b):
        if a.val < b.val:
            return -1

    def __str__(self):
        return str(self.val)


t = merge_sorted([Test(1), Test(2), Test(4)], [
    Test(1), Test(3), Test(5)], Test.cmp)

for i in t:
    print(i, end=' ')
