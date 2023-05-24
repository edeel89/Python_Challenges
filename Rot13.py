def rot13(message):
    out2 = ""
    for i in message:
        if i.isalpha():
            if i.isupper():
                if ord(i) <= ord("M"):
                    out = ord(i) + 13
                    out = chr(out)
                    out2 = out2 + out
                    out2 = out2.replace("-", " ")
                else:
                    out = ord(i) - 13
                    out = chr(out)
                    out2 = out2 + out
                    out2 = out2.replace("-", " ")
            else:
                if ord(i) <= ord("m"):
                    out = ord(i) + 13
                    out = chr(out)
                    out2 = out2 + out
                    out2 = out2.replace("-", " ")
                else:
                    out = ord(i) - 13
                    out = chr(out)
                    out2 = out2 + out
                    out2 = out2.replace("-", " ")
        else:
            out2 = out2 + i

    print(out2)

rot13("aA bB zZ 1234 *!?%")