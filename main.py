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


# элемент из букв и цифр
def get_random_letter_and_number_element(number): # элемент из букв и цифр
    letters_and_number = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_number, number)) # в пустую строку записывает 29ю строку в кол-ве number раз
    return rand_string
    # print("Alphanum Random string of length", number, "is:", rand_string)

array_of_random_elements = []


# массив случайных чисел и букв
def get_array_of_random_elements(lengthOfArray, number):
    for i in range(lengthOfArray):
        random_element = str(get_random_number_element(- pow(10, round(number / 2)) + 1, pow(10, round(number / 2)) - 1)) \
                         + get_random_letter_and_number_element(round(number / 2)) + '.' \
                         + get_random_letter_and_number_element(number)
        array_of_random_elements.append(random_element)
    return array_of_random_elements


array_of_random_elements_negative = []


# массив случайных чисел и букв с возможно отрицательным значением
def get_array_of_random_elements_negative(lengthOfArray, number):
    for i in range(lengthOfArray):
        random_element = get_random_letter_and_number_element(number) + '.' \
                         + get_random_letter_and_number_element(number)
        array_of_random_elements_negative.append(random_element)
    return array_of_random_elements_negative


get_array_of_random_elements(10, 4)
print(array_of_random_elements)

# get_array_of_random_number_elements(10)
# print(array_of_random_number_elements)