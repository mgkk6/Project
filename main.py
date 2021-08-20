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
