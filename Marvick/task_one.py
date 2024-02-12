my_lists = [1,2,3,4,5,6,7,8,9,10]
def get_length_of_list(value):
    index = 0
    for num in value:
        index += 1
    return index



def get_sum_of_the_even_position_on_the_list(value):
    sum_index = 0
    for num in range(get_length_of_list(value)):
        if num % 2 != 0:
            sum_index += value[num]
    return sum_index
def get_sum_of_the_odd_position_on_the_list(value):
    sum_odd = 0
    for num in range(get_length_of_list(value)):
        if num % 2 == 0:
            sum_odd += value[num]
    return sum_odd

def get_multiply_of_the_third_position_of_the_list(value):
    third_position = 1
    for num in range(get_length_of_list(value)):
        if num % 3 == 0:
            third_position *= value[num]
    return third_position

def get_average_of_the_list(value):
    average = 0
    for num in range(get_length_of_list(value)):
        average /= value[num]
    return average