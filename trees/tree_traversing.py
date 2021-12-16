"""
Нода дерева - кортеж из трех элементов:
(левое подерево, значение в ноде, правое поддерево)
"""

tree = (
    ((None, "C", None), "B", ((None, "E", None), "D", None)),
    "A",
    (None, "F", None),
)


def traverse_tree_infix(tree: tuple[tuple, str, tuple]):
    left, value, right = tree
    if left:
        traverse_tree_infix(left)
    print(value)
    if right:
        traverse_tree_infix(right)


def traverse_tree_prefix(tree: tuple[tuple, str, tuple]):
    left, value, right = tree
    print(value)
    if left:
        traverse_tree_prefix(left)
    if right:
        traverse_tree_prefix(right)


def traverse_tree_postfix(tree: tuple[tuple, str, tuple]):
    left, value, right = tree
    if left:
        traverse_tree_postfix(left)
    if right:
        traverse_tree_postfix(right)
    print(value)


print("infix")
traverse_tree_infix(tree)
print("prefix")
traverse_tree_prefix(tree)
print("postfix")
traverse_tree_postfix(tree)
