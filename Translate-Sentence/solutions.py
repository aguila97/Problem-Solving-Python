from string import punctuation
def translate_word(word):
       if word == "":
              return ""
       u = 0
       a = ["a","e","i","o","u","A","E","I","O","U"]
       if word[0] in a:
              if word[0].isupper():
                     final = word[0].upper() + word[1:] + "yay"
              else:
                     final = word + "yay"
       else:
              
              b = 0
              
              start = ""
              for i in range(len(word)):
                     
                     if word[i] in a:
                            b = i
                            break
                     else:
                            start+=word[i]
              if word[0].isupper():
                     final = word[b].upper() + word[b+1:].lower() + start.lower() + "ay"
              else:
                     if word[len(word)-1] in punctuation:
                            final = word[b:len(word)-1].lower() + start.lower() + "ay" + word[len(word)-1]
                     else:
                            final = word[b:].lower() + start.lower() + "ay"
       
                            
       return final

##print(translate_word("Shrimp"))
##print(translate_word("trebuchet"))
##print(translate_word(""))

def translate_sentence(senten):
       if senten == "":
              return ""
       a = senten.split(" ")
       b = []
       for i in a:
              c = translate_word(i)
              b.append(c)
       final = ""
       for i in b:
              final +=i
              final +=" "

       return final

##print(translate_sentence("I like to eat honey waffles"))
##print(translate_sentence("Do you think it is going to rain today?"))