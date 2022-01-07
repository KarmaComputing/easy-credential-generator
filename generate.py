from random_word import RandomWords
import random
# Example usage

# Generate username:
# user(8,3)
#   Length up to 32
#   Difficulty 1-5 Default is 3

def user(length,entropy,words):
    print("")


def password(length,entropy,words):
    min = (round(length%3)+length+1)
    max = length
    for x in range(words):          ##ERROR HERE
        if x == words:
            word = (genword(min,max,entropy))
            output = word + output
            print(output)
        else:
            word = (genword(min,max,entropy)," ")
            output = word + output
            print(output)


def genword(min,max,entropy):
    lower = RandomWords.minLength(min)
    higher = RandomWords.maxLength(max)
    word = RandomWords(lower,higher,complexity(entropy))
    return word


def complexity(entropy):
    if entropy == "1": #Easiest
        args = hasDictionaryDef("true")
        return args
    elif entropy == "2": #
        args = hasDictionaryDef("true")
        return args
    elif entropy == "3" or entropy is None: #Mid (Default)
        args = hasDictionaryDef("true")
        return args
    elif entropy == "4": #
        print()
        return args
    elif entropy == "5": #Hardest
        print()
        return args
    else:
        print("Invalid complexity value")
