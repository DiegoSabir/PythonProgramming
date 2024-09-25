word = input("Introduzca una palabra: ")

analysis = word.lower().replace(" ", "")

inverted_word = analysis[::-1]

if(analysis == inverted_word):
    print(word, "es palindromo")

else:
    print(word, "no es palindromo")