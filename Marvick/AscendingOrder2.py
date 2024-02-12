def Ascending_Order2(num):
    for count in range(len(num)):
        for index in range(len(num)):
            if num[count] < num[index]:
                num[count], num[index] = num[index], num[count]

    return num


def Descending_Order2(num):
    for count in range(len(num)):
        for index in range(len(num)):
            if num[count] > num[index]:
                num[count], num[index] = num[index], num[count]

    return num


def Search_key(date: list, key: int) -> int:
    print(list(enumerate(date)))
    for index, value in enumerate(date):
        if value == key:
            return index
    return -1


print(Search_key([10, 2, 8, 9, 3, 4, 1, 5], 5))

sample_set = {1, 2.5, 3}
sample_set2 = {9, 2.5, 3}
print(sample_set | sample_set2)

person = {
    'Name': "bolaji",
    'weight': 2.4,
    6: 122,
    'sizes': (1, 2, 3)

}
print([1])
