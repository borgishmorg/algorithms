s = "((C)B((E)D))A(F)"

"""
Нода дерева - кортеж из трех элементов:
(левое подерево, значение в ноде, правое поддерево)
"""


def build_sub_tree(s: str, pos: int = 0) -> tuple[int, tuple[tuple, str, tuple]]:
    left = None
    value = ""
    right = None
    while pos < len(s):
        if s[pos] == "(":
            if value == "":
                pos, left = build_sub_tree(s, pos + 1)
            else:
                pos, right = build_sub_tree(s, pos + 1)
        elif s[pos] == ")":
            return pos + 1, (left, value, right)
        else:
            value += s[pos]
            pos += 1
    return pos + 1, (left, value, right)


print(s)
print(build_sub_tree(s)[1])
