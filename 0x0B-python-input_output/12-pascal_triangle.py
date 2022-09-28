

def pascal_triangle(n):

    if n < 1:
        return []

    p_list = [[1]]

    i = 1

    while (i < n):

        last = p_list[i - 1]
        row = [1] + [last[j] + last[j + 1] for j in range(len(last) - 1)] + [1]
        p_list.append(row)

        i += 1

    return p_list

print(pascal_triangle(5))