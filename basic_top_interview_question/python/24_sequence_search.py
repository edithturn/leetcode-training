def secuence_search(_str, key):
    max_ = 0
    tmp_cursor = 0
    is_secuence = False
    f_list = ""
    sub_string = _str
    for letter in key:
        if letter in sub_string:
            max_ = sub_string.index(letter)
            print(max_)
            sub_string = sub_string[max_:len(_str)]
            f_list += letter
            print(f_list)
            if f_list == key:
                print(f_list)
                return True
            else:
                return False
        else:
            return False


# TO DO
str1= "arcata"
key1 = "cat"

str2= "c1a2t3"
key2 = "cat"

str3= "caat"
key3 = "cat"

str4= "cta"
key4 = "cat"

print(secuence_search(str1, key1))
print(secuence_search(str2, key2))
print(secuence_search(str3, key3))
print(secuence_search(str4, key4))


