# Basically the same as http://rosettacode.org/wiki/Huffman_coding#Python, but with PriorityQueue

from collections import Counter
from queue import PriorityQueue


def huffman(string):
    count = Counter()
    q = PriorityQueue()

    for letter in string:
        count[letter] += 1

    string_counted = [[weight, [value, '']] for value, weight in count.items()]

    for item in string_counted:
        q.put([item[0], item[1]])

    while q.qsize() > 1:

        left = q.get()
        right = q.get()

        for x in left[1:]:
            x[1] = '0' + x[1]

        for x in right[1:]:
            x[1] = '1' + x[1]

        q.put([left[0] + right[0]] + left[1:] + right[1:])

    tree = q.get()

    tree = tree[1:]
    code = dict()

    for pair in tree:
        code[pair[0]] = pair[1]

    return code

if __name__ == '__main__':

    string = "this is an example for huffman encoding"
    alpha = huffman(string)
    print(string, '\n')
    for letter in string:
        print(alpha[letter], end='')
