__author__ = 'bruno'


def recursive_sort(unordered):
    if unordered == []:
        return unordered
    return recursive_sort([x for x in unordered[1:] if x < unordered[0]]) + unordered[0:1] + \
           recursive_sort([x for x in unordered[1:] if x >= unordered[0]])


def iterative_sort(unordered):
    if len(unordered) == 0:
        return unordered

    stack = [unordered]
    ordered = []

    while len(stack):
        temp = stack.pop()
        tl = len(temp)

        if tl == 1:
            ordered.append(temp[0])
            continue

        pivot = temp[0]
        left = []
        right = []

        for i in range(1, tl):
            if temp[i] <= pivot:
                left.append(temp[i])
            else:
                right.append(temp[i])

        left.append(pivot)

        if len(right):
            stack.append(right)
        if len(left):
            stack.append(left)

    return ordered
