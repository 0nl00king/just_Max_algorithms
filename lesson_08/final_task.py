from collections import Counter, deque


def just_tree(s):
    LEFT, RIGHT = 0, 1
    count = Counter(s)
    sorted_deque = deque(sorted(count.items(), key=lambda _: _[RIGHT]))

    if len(sorted_deque) != 1:

        while len(sorted_deque) > 1:
            weight = sorted_deque[LEFT][RIGHT] + sorted_deque[RIGHT][RIGHT]
            combine = {LEFT: sorted_deque.popleft()[LEFT],
                       RIGHT: sorted_deque.popleft()[LEFT]}

            for elm, idx in enumerate(sorted_deque):
                if weight > idx[RIGHT]:
                    continue
                else:
                    sorted_deque.insert(elm, (combine, weight))
                    break
            else:
                sorted_deque.append((combine, weight))
    else:
        weight = sorted_deque[LEFT][RIGHT]
        combine = {LEFT: sorted_deque.popleft()[LEFT], RIGHT: None}
        sorted_deque.append((combine, weight))

    return sorted_deque[LEFT][LEFT]


def haffman(tree, path=''):
    LEFT, RIGHT = 0, 1
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman(tree[LEFT], path=f'{path}0')
        haffman(tree[RIGHT], path=f'{path}1')


if __name__ == '__main__':

    str_to_code = 'It was fun while it lasted.'
    code_table = dict()

    haffman(just_tree(str_to_code))

    for character in str_to_code:
        print(code_table[character], end=' ')
    print()
    # 10110 011 00 1000 1001 1110 00 10111 10100 10101 00 1000 01010 1111 1100 1101 00 1111 011 00 1100 1001 1110 011 1101 01011 0100
    print(code_table)
    # {' ': '00', '.': '0100', 'h': '01010', 'd': '01011', 't': '011', 'w': '1000', 'a': '1001', 'u': '10100',
    # 'n': '10101', 'I': '10110', 'f': '10111', 'l': '1100', 'e': '1101', 's': '1110', 'i': '1111'}
