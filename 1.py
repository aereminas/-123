from typing import List, Union

def calculate_average(number_list: List[Union[int, float]]) -> Union[float, str]:
    for index, item in enumerate(number_list):
        if not isinstance(item, (int, float)):
            try:
                number_list[index] = float(item)
            except ValueError:
                return "Некорректный ввод"
    return round(sum(number_list) / len(number_list), 2)

assert calculate_average([1, 1]) == 1.0
assert calculate_average([2.5, 3.5]) == 3.0
assert calculate_average([1.1, 2.2, 3.3]) == 2.2
assert calculate_average([1, 2, 3, 4, '5']) == 3.0
assert calculate_average([1, 2, "abc"]) == "Некорректный ввод"
assert calculate_average([1, 2, [1,2]]) == "Некорректный ввод"
assert calculate_average([-1, -2]) == -1.5
assert calculate_average([1, 2, 3, 4, 5]) == 3.0
assert calculate_average([100, 200, 300]) == 200.0
assert calculate_average([0.1, 0.2, 0.3]) == 0.2
assert calculate_average([1,2,3,"4.5"]) == 2.62
assert calculate_average("123") == "Некорректный ввод"

