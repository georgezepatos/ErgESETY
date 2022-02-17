def remove_punctuation(text: str) -> str:
    out: str = ""
    for character in text:
        if character == "\n": out += " "
        elif character.isalpha() or character.isspace(): out += character
    return out.lower()

def maximum_length(word_list: list) -> int:
    maximum: int = len(word_list[0])
    for word in word_list:
        if len(word) > maximum: maximum = len(word)
    return maximum

def sort(word_list: list) -> list:
    out: list = []
    for length in range(maximum_length(word_list)):
        for word in word_list:
            if len(word) == length: out.append(word)
    return out

def occurrences(data: list[str]) -> dict:
    out: dict = {}
    for token in data:
        if token not in out.keys():
            out[token] = 1
        else:
            out[token] += 1
    # print(out)
    return out

def get_popular(data: list[str]) -> list:
    occurrences_dict: dict = {}
    occurrences_dict = occurrences(data)
    values = list(set(occurrences_dict.values()))
    values.sort(reverse=True)
    # print("VALUES: ", values)
    return values

def find_words_by_occurrence(data_dict: dict, amount: int = 10) -> list:
    out: list = []
    sorted_dict = {k: v for k, v in sorted(data_dict.items(), key=lambda item: item[1], reverse=True)}
    for index in range(amount):
        out.append(list(list(sorted_dict.items())[index])[0])
    return out

def popular_prefixes(data, characters: int) -> list[str]:
    prefix_list: list = []
    for word in data:
        if len(word) >= characters: prefix_list.append(word[:characters])
    return find_words_by_occurrence(occurrences(prefix_list), 3)



if __name__ == "__main__":
    data: list[str] = remove_punctuation(open("C:/texts/zep.txt", 'r', encoding="utf-8").read()).split()
    data = sort(data)
    print("10 MOST POPULAR WORDS:", find_words_by_occurrence(occurrences(data)))
    for characters in range(2, 4):
        print("3 MOST POPULAR FIRST", characters, "CHARACTERS:", popular_prefixes(data, characters))