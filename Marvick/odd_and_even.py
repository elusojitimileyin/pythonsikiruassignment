try:

    number = int(input("Enter an integer:"))
    sum_even = sum(list(range(1, number))[1::2])
    sum_odd = sum(list(range(1, number))[::2])
    print(sum_even, sum_odd)
#
# except ValueError:
#     print("invalid input")
except (ValueError, TypeError) as e:
    print(e)

# even_number = 0
# odd_number = 0
# for number in range(1, number):
#     if number % 2 == 0:
#         even_number += number
#     else:
#         odd_number += number
#
# print(even_number)
# print(odd_number)

# odd = sum([num for num in range(1, number) if num % 2 != 0])
# even = sum([num for num in range(1, number) if num % 2 ==0])
# print(even)
# print(odd)

