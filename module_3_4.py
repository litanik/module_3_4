# 1. Создаем функцию single_root_words, которая принимает одно обязательное
# слово в параметр root_word, а далее неограниченную последовательность
# в параметр *other_words.
def single_root_words(root_word, *other_words):
    # 2. Создаем внутри функции single_root_words пустой список same_words,
    # который будет пополняться нужными словами.
    same_words = []
    root_word_ = root_word.lower()
    # 3. При помощи цикла for перебераем предполагаемо подходящие слова.
    for i in other_words:
        other_words_ = i.lower()
        if root_word_ in other_words_ or other_words_ in root_word_:
            # 4. Пропишите корректное относительно задачи условие, при котором добавляются
            # слова в результирующий список same_words.
            same_words.append(i)
    # 5. После цикла возвращаем образованный функцией список same_words.
    return same_words


# Вызов функции single_root_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

# Примечания:
# При проверке наличия одного слова в составе другого стоит учесть,
# что регистр символов не должен влиять ни на что. ('Disablement' - 'Able')
# ('Able', 'able', 'AbLe' - все подходят).
# В этой задаче вам могут понадобиться следующие методы строк/ключевые слова:
# а. Оператор in или count()
# b. lower()/upper().
