def get_word_count(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    return char_count


def sort_chars(char_dict: dict[str, int]) -> list[dict]:
    char_list = [{"char": c, "num": char_dict[c]} for c in char_dict]
    char_list.sort(key=lambda x: x["char"])
    return char_list
