def main():
    user_sentence = get_sentence()
    real_sentence = ""
    listik = "АУОЫИЭЯЮЁЕБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

    for letter in user_sentence:
        if letter.isupper():
            letter = letter.lower()
            letter = " " + letter
            real_sentence += letter
        else:
            real_sentence += letter

    #real_sentence = real_sentence[1].upper()
    real_sentence = real_sentence[1:]
    new_char = real_sentence[0].upper()
    real_sentence = real_sentence[1:]
    real_sentence = new_char + real_sentence



    print(real_sentence)



def get_sentence():
    sentence = input("Введите предложение без пробелов, началло слова - ПРОПИСНАЯ буква: ")
    return sentence

main()

