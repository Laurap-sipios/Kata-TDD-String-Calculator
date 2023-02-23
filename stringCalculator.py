

def sumStringArray(numbers):
    return sum([ int(number) for number in numbers  ])

def Add(numbers):

    if numbers == "":
        return 0

    else : 
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
        else:
            delimiter = ','
            numbers = numbers.replace("\n", ",")

        splitNumbers = numbers.split(delimiter)

        negatives = [number for number in splitNumbers if int(number) < 0]
        
        if negatives != []:
            raise ValueError("negatives number : ", negatives)


        return sumStringArray(splitNumbers)    






        
