def translate(word):
    result = ""
    for letter in word:
        if letter in "awiou":
            result = result + "3"
            else:
                result = result + letter
             return result
            print(translate("speed"))