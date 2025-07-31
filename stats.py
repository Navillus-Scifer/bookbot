def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    count = text.split()
    len(count)
    return len(count)

def character_count(letters):
    letters_count = letters.lower()
    my_counts = {}
    for char in letters_count:
        if char in my_counts:
            my_counts[char] +=1
        else:
            my_counts[char] =1
    return my_counts

def numb_value(alpha_dict):
    return alpha_dict["num"]

def sorted_count(sorted_letters):
    alpha_character = []
    for chara, count in sorted_letters.items():
        list_count = {"char": chara, "num": count}
        alpha_character.append(list_count)
    alpha_character.sort(reverse=True, key=numb_value)
    return alpha_character


