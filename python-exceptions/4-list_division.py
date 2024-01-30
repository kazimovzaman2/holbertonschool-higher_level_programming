#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            elem = 0
        except (TypeError, ValueError):
            print("wrong type")
            elem = 0
        except IndexError:
            print("out of range")
            elem = 0
        finally:
            result.append(elem)
    return result
