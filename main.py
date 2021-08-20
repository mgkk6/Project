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
        random_element = str(get_random_number_element(- pow(10, round(number / 2)) + 1 , pow(10, round(number / 2)) - 1 )) \
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


#get_array_of_random_elements(10, 4)
#print(array_of_random_elements)

# get_array_of_random_number_elements(10)
# print(array_of_random_number_elements)

ParametrArr = ['1: Force', '2: Length', '3: Hardness', '4: NumOfElements']
arr = []
checked_arr = []
bad_arr = []
additionalArr = []


# поиск ошибок и возвращение проверенного массива
def check_array_for_mistakes(arr, parametr):
    # сгенерированный массив
    print(arr)
    # делаем массив только из цифр с плавающей запятой и отрицательными значениями
    for value in range(len(arr) - 1):
        if '.' in arr[value] and arr[value].split('.')[0].isdigit() and arr[value].split('.')[1].isdigit() \
                or arr[value][0] == '-' and '.' in arr[value] and arr[value].split('.')[0].split('-')[1].isdigit() \
                and arr[value].split('.')[1].isdigit():
            checked_arr.append(float(arr[value]))
        else:
            bad_arr.append(arr[value])
    if parametr == ParametrArr[0].split(' ')[1] or parametr == '1':
        print('Force')

        # делаем массив только из цифр с плавающей запятой и без отрицательных значений
    elif parametr == ParametrArr[1].split(' ')[1] or parametr == '2':
        for value in range(len(checked_arr) - 1, -1, -1):
            if checked_arr[value] <= 0:
                bad_arr.append(checked_arr[value])
                checked_arr.remove(checked_arr[value])
        print('Length')

        # тоже самое что и предыдущее
    elif parametr == ParametrArr[2].split(' ')[1] or parametr == '3':
        for value in range(len(checked_arr) - 1, -1, -1):
            if checked_arr[value] <= 0:
                bad_arr.append(checked_arr[value])
                checked_arr.remove(checked_arr[value])
        print('Hardness')

        # делаем массив только из целых цифр и без отрицательных значений
    elif parametr == ParametrArr[3].split(' ')[1] or parametr == '4':
        for value in range(len(checked_arr) - 1, -1, -1):
            if str(checked_arr[value]).split('.')[1] != '0':
                bad_arr.append(checked_arr[value])
                checked_arr.remove(checked_arr[value])
        for value in range(len(checked_arr) - 1, -1, -1):
            checked_arr[value] = int(checked_arr[value])
        print('NumOfElements')

    else:
        print('Введите слово из списка')

    return checked_arr


get_array_of_random_elements(1000, 1)
parametr = input('Введите какой величине должен соответсвовать каждый элемент в массиве: ' + ', '.join(ParametrArr)
                 + '\n')
check_array_for_mistakes(array_of_random_elements, parametr)
print('Массив неправильных значений: ' + str(bad_arr))
print('Массив правильных значений: ' + str(checked_arr))
# print(valueArr[0].split(' ')[1])