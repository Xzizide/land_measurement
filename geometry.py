def equal_amount_list(list_1, list_2) -> tuple[list[float], list[float]]:
    obj1_list_copy = list_1[:]
    obj2_list_copy = list_2[:]
    difference = len(obj1_list_copy) - len(obj2_list_copy)

    if difference > 0:
        for _ in range(difference):
            obj2_list_copy.append(0)
    else:
        for _ in range(abs(difference)):
            obj1_list_copy.append(0)

    return obj1_list_copy, obj2_list_copy
