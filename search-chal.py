def linear_search(target, my_list):
    for i in range(len(my_list)):
        if target == my_list[i]:
            print(i)
            break
    else:
        print('not found')


random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

linear_search(18, random_numbers)  # 2 (it returns the position of the number)
linear_search(9, random_numbers)


def global_linear_search(target, my_list):
    result = []
    for i in range(len(my_list)):
        if target == my_list[i]:
            result.append(i)
    print(result)


bananas_arr = list("bananas")  # ["b", "a", "n", "a", "n", "a", "s"]
global_linear_search("a", bananas_arr)   # [1, 3, 5]
