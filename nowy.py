#1
def sweap_max(a: list) -> list:
    max_pos = 0
    for i in range(1, len(a)):
        if a[i] >= a[max_pos]:
            max_pos = i
    temp = a[0]
    a[0] = a[max_pos]
    a[max_pos] = temp
    return a

result = sweap_max([1, 6, 30, 918, 200, 10])
print(result)
