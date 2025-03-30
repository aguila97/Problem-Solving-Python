# First Letter Shift  
def shift_sentence(txt):
    if len(txt) == 1:
        return txt
    sentence_split = txt.split(" ")
    length = len(sentence_split)-1
    new_sentence = sentence_split[length][:1] + sentence_split[0][1:]

    for i in range(length):              
        first_letter = sentence_split[i][:1]
        new_word = first_letter + sentence_split[i+1][1:]
        new_sentence += " "
        new_sentence += new_word 


       
       

    return new_sentence


print(shift_sentence("it should shift the sentence"))