#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        num = 0
        try:
            num = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("dividson by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(num)
    return new_list
