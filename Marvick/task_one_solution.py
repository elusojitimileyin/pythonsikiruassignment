my_lists = list(range(10, 20))

def get_length_of_list(value):
    index = 0
    for num in value:
        index += 1
    return index

def get_sum_of_the_even_position_on_the_list(value):
    return sum(value[1::2])


def get_sum_of_the_odd_position_on_the_list(value):
    return sum(value[::2])



def get_average(value):
    return sum(value)/ len(value)

def get_largest(value):
   #    return max(value)
    element = value[0]
    for num in value():
        if num > element:
            element = num
    return element


def get_minium(value):
    # return min(value)
    element = value[0]
    for num in value():
        if num < element:
            element = num
    return element

def get_string(words):
    results =[]
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            results.append(word)
    return results