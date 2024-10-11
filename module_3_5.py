
def get_multiplied_digits(numger):
    str_numger = str(numger)


    first = int(str_numger[0])
    if len(str_numger)>1:

        return first*get_multiplied_digits(int(str_numger[1:]))
    elif len(str_numger)<2:
        return first




print(get_multiplied_digits(4023))