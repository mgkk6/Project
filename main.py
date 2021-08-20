import random
import string
# случайное число
def get_random_number_element(FromNumber=-100, toNumber=100):
    greaterThan = FromNumber
    lessThan = toNumber
    rounded_number = round(random.uniform(greaterThan, lessThan))  # round округление
    return rounded_number


rounded_number = get_random_number_element()
# print(rounded_number)

# массив случайных чисел
array_of_random_number_elements = []


def get_array_of_random_number_elements(lengthOfArray):
    for i in range(lengthOfArray):
        random_element = get_random_number_element()
        array_of_random_number_elements.append(random_element)
    return array_of_random_number_elements