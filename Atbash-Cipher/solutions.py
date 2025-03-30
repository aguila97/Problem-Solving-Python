def atbash(txt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetUpper = alphabet.upper()

    alphabetUpper_reverse_order = alphabetUpper[::-1]
    alphabet_reverse_order = alphabet[::-1]

    reference_code = {}
    for i in zip(alphabet,alphabet_reverse_order):
            reference_code[i[0]] = i[1]

    for j in zip(alphabetUpper,alphabetUpper_reverse_order):
            reference_code[j[0]] = j[1]


    output = ""
    for i in txt:
            if i in reference_code.keys():
                    code_value = reference_code[i]
                    output += code_value
            else:
                    output+=i

    return output