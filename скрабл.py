import random


LETTER_SCORES = {
    'А': 1,
    'Б': 3,
    'В': 1,
    'Г': 3,
    'Д': 2,
    'Е': 1,
    'Ё': 3,
    'Ж': 5,
    'З': 3,
    'И': 1,
    'Й': 4,
    'К': 2,
    'Л': 2,
    'М': 2,
    'Н': 1,
    'О': 1,
    'П': 2,
    'Р': 1,
    'С': 1,
    'Т': 1,
    'У': 2,
    'Ф': 10,
    'Х': 5,
    'Ц': 5,
    'Ч': 5,
    'Ш': 8,
    'Щ': 10,
    'Ъ': 10,
    'Ы': 4,
    'Ь': 3,
    'Э': 8,
    'Ю': 8,
    'Я': 3
}


def get_random_letter():
    dect_keys = LETTER_SCORES.keys()
    converted_dictionary = list(dect_keys)
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(letter):
    while True:
        word = input(f"Введите слово на букву {letter}:")
        if letter == word[0].upper():
            return word
        else:
            print("не правильно")


def calculate_score(word):
    all_scores = []
    for letter in word:
        score = LETTER_SCORES.get(letter.upper())
        all_scores.append(score)
    return sum(all_scores)


def main():     
    rand_letter = get_random_letter()
    print("Начальная буква:", rand_letter)

    print("Ходит игрок 1")
    player_1 = get_word_with_letter(rand_letter)
    print("Ходит игрок 2")
    player_2 = get_word_with_letter(rand_letter)

    scores_1 = calculate_score(player_1)
    scores_2 = calculate_score(player_2)

    print(f"Игрок 1 ввёл слово {player_1} и набрал {calculate_score(player_1)}")
    print(f"Игрок 2 ввёл слово {player_2} и набрал {calculate_score(player_2)}")

    if scores_1 > scores_2:
        print("игрок 1 победил")
    elif scores_2 > scores_1:
        print("игрок 2 победил")
    else:
        print("ничья")


if __name__ == '__main__':
    main()
    
