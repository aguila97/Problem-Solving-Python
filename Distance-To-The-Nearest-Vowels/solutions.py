
'''
Write a function that takes in a string and for each character, returns the distance 
to the nearest vowel in the string. If the character is a vowel itself, return 0.
'''




def find_all_vowels(str):

    vowels = ["a","e","i","o","u"]
    final = []
    for i in range(len(str)):
        if str[i] in vowels:
            final.append(i)

    return final


def distanceToNearestVowel(data):
    index = 0
    vowelPlaces = find_all_vowels(data)

    final = []

    # add dummy data | cause of minus of index in the loop
    vowelPlaces.append(10)
    data = data + "."

    for i in range(len(data)-1):
        vowel = vowelPlaces[index]
        if i == vowel:
            final.append(0)
            if i+1 == vowelPlaces[index+1]:
                index+=1
        else:
            if i+1 == vowelPlaces[index+1]:
                final.append(1)
                index+=1
            else:
                final.append(abs(vowel-i))
    return final


print(distanceToNearestVowel("abbaaaaba"))
