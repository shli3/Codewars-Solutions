#"Twice as Old"
def twice_as_old(dad_years_old, son_years_old):
#the key to finding the father's age when he doubles his son, is to find his age when
#his son was born
    if dad_years_old == son_years_old * 2:                #present day, father doubles
        print("The father is already double the son's age")    #son
        return 0
    dad_son_birth_age = dad_years_old - son_years_old #father's age when son was born
    dad_dad = dad_son_birth_age * 2              #father's age when he doubles his son
    dad_new_age = dad_dad - dad_years_old    #Time elapsed to or from doubling of age
    if dad_new_age < 0:                    #making negative numbers positive
        dad_new_age = dad_new_age * (-1)
    return dad_new_age
    #PROGRAMMER'S NOTE: It's been a while since I actually used python