Sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
for count in range(0, len(Sample_list)):
    for index in range(count +1, len(Sample_list)):
        if Sample_list[count] >= Sample_list[index]:
            Sample_list[count], Sample_list[index] = Sample_list[index], Sample_list[count]

print(Sample_list)
