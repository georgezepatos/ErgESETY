def remove_punctuation(text: str) -> str:
    out: str = ""
    for character in text:
        if character == "\n": out += " "
        elif character.isalpha() or character.isspace(): out += character
    return out

def remove_pairs(word_list: list) -> list:
    out: list = word_list
    for word in out:
        for other_word in out:
            if len(word) + len(other_word) == 20 and word != other_word and word in out and other_word in out:
                # print(word, other_word)
                out.remove(word)
                out.remove(other_word)
    return out

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

def length_stats(word_list: list) -> list:
    out: list = [0 for _ in range(maximum_length(word_list))]
    for word in word_list: out[len(word) - 1] += 1
    return out

def report(stats_list: list) -> None:
    for index in range(len(stats_list)):
        print("There are " + str(stats_list[index]) + " words with length " + str(index + 1))
    return


if __name__ == "__main__":
    data: list[str] = remove_punctuation(open("C:/texts/zep.txt", 'r', encoding="utf-8").read()).split()
    data = remove_pairs(data)
    # print(data)
    report(length_stats(data))