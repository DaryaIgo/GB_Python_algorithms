# Урок 8 Деревья. Хеш-функция

# 1. Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib
import re


def func_hash(test_str):
    n = len(test_str)
    r = set()

    for i in range(n):
        if i == 0:
            n = len(test_str) - 1
        else:
            n = len(test_str)
        for j in range(n, i, -1):
            r.add(hashlib.sha1(S[i:j].encode('utf-8')).hexdigest())

    print(f"Количество различных подстрок в строке '{test_str}' равно {len(r)}")
    return r


if __name__ == "__main__":
    # S = "Nobody inspects the spammish repetition"
    S = "nobody inspects the spammish repetition"
    # S = "11 nobody inspects the spammish repetition"

    if re.match('[0-9]', S):
        print('Введена неподходящяя строка')
    elif S == str(S).lower():
        func_hash(S)
    else:
        print('Введена неподходящяя строка')

# 2. Закодировать любую строку по алгоритму Хаффмана.

string = 'la laa laaa'


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def make_tree(node, code=""):
    if isinstance(node, str):
        return {node: code}

    l, r = node.children()

    result = {}
    result.update(make_tree(l, code + "0"))
    result.update(make_tree(r, code + "1"))

    return result


frequencies = {}
for char in string:
    if char not in frequencies:
        frequencies[char] = 0

    frequencies[char] += 1

tree = frequencies.items()


while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append((Node(char1, char2), count1 + count2))

code_table = make_tree(tree[0][0])

coded = []
for char in string:
    coded.append(code_table[char])

print(f"Закодированная строка: {''.join(coded)}")
