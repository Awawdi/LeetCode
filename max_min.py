def max_delta_finder(values_list:list)-> list[int,int,int]:
    """
    This function tries to find maximum delta between values
    """
    max_index_value:int=0

    min_index_value:int = 0
    min_value = values_list[0]

    max_delta:int=0

    for i in range(len(values_list)):

        if values_list[i] - min_value > max_delta:
            max_delta = values_list[i] - min_value
            max_index_value = i

        if values_list[i] < min_value:
            min_value = values_list[i]
            min_index_value = i

    return [max_delta, min_index_value, max_index_value]



values = [100, 250, 550, 340, 100, 23, 280, 690, 258, 100, 400, 500, 500]

result = max_delta_finder(values)
delta, min_idx, max_idx = result[0],result[1],result[2]
print(f"The maximum delta is {delta}, occurring between index {min_idx} and {max_idx}.")
