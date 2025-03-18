def Add(numbers):
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")
    result = 0

    for num in number_list:
        if num.strip():
            result += int(num)
        else:
            raise ValueError("Invalid input")

    return result
