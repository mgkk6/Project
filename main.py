import random
import string
# случайное число
def get_random_number_element(FromNumber=-100, toNumber=100):
    greaterThan = FromNumber
    lessThan = toNumber
    rounded_number = round(random.uniform(greaterThan, lessThan))  # round округление
    return rounded_number


rounded_number = get_random_number_element()
print(rounded_number)