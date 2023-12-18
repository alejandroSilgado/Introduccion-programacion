word1 = input("Ingrese palabra 1: ")
word2 = input("Ingrese palabra 2: ")

num_word1 = len(word1)
num_word2 = len(word2)

if num_word1 > num_word2:
    print("La palabra '{}' es más larga que la palabra '{}'.".format(word1, word2))
else:
    print("La palabra '{}' es más larga que la palabra '{}'.".format(word2, word1))
