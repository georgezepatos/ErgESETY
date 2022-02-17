import ast


def shortest(input_list: list[str]) -> str:
    shortest = input_list[0]
    for element in input_list:
        if len(element) < len(shortest): shortest = element
    return shortest


def longest(input_list: list[str]) -> str:
    longest = input_list[0]
    for element in input_list:
        if len(element) > len(longest): longest = element
    return longest


if __name__ == "__main__":
    raw_data: list = open("C:/texts/exe7.txt", 'r', encoding="utf=8").readlines()
    data: list[dict] = []
    for line in raw_data: data.append(ast.literal_eval(line.rstrip()))

    choosen_key: str = ""
    while choosen_key not in list(data[0].keys()):
        choosen_key = input("Please select one of the available keys: " + str(list(data[0].keys())) + ": ")

    print("You choose key " + choosen_key + ".")

    values: list = []
    for dictionary in data: values.append(dictionary[choosen_key])
    if len(choosen_key) == 1:
        print(min(values), max(values))
    else:
        print(shortest(values), longest(values))