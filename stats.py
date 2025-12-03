def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    characters = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            characters[char] = characters.get(char, 0) + 1
    return characters


def sort_on(d):
    return d["num"]


def get_sorted_char_list(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
