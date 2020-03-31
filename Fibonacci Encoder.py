#Copyright 2019 by Khang Nguyen and Timothy Merrill

#How to use:
#Run the program.
#It will ask you to decode or encode.
#Type de for decode, and en for encode.
#Then type your message. While encoding,
#you can use most punctuation except an
#apostrophe. You can use commas and other
#punctuation. While decoding, you just paste
#the message you got in the prompt.

#When you try to encode an apostrophe, it works as expected.
#However the decoder will not work if there is one.
#This is being fixed soon.

#Please credit me as the original author if you are making something using this.
#Thanks! :)

import sys

complete = False


def translate():
    keys = {" ": "|", "a": "2.", "b": "3.", "c": "5.", "d": "8.", "e": "13.", "f": "21.", "g": "34.", "h": "55.",
            "i": "89.", "j": "144.", "k": "233.", "l": "377.", "m": "610.", "n": "987.", "o": "1597.", "p": "2584.",
            "q": "4181.", "r": "6765.", "s": "10946.",
            "t": "17711.", "u": "28657.", "v": "46368.", "w": "75025.", "x": "121393.", "y": "196418.", "z": "317811.",
            "!": "!", ",": ",", "?": "?", "'": "'.", "|": "|", ":": ":", "": "", "-": "-."}
    encodeNames = ["en", "encode", "En", "Encode"]
    decodeNames = ["de", "decode", "De", "Decode"]
    dekeys = {v: k for k, v in keys.items()}
    cdekeys = {k.replace('.', ''): v for k, v in dekeys.items()}
    task = str(input("Decode or encode?"))
    ask = "lol"
    totranslate = "You did not choose a valid action."
    if task in encodeNames:
        totranslate = str(input("Give me the message."))
        totranslate = totranslate.lower()
        totranslate = totranslate.replace(".", "|||")
        for item in totranslate:
            totranslate = totranslate.replace(item, str(keys[item]))
            totranslate = totranslate.replace(".|", "|")
        if totranslate[len(totranslate) - 1] == ".":
            totranslate = totranslate[:len(totranslate) - 1]
    elif task in decodeNames:
        totranslate = str(input("Give me the message."))
        totranslate = totranslate.replace("|||", "~")
        totranslate = totranslate.replace("|", " ")

        translist = totranslate.split(sep=".")
        for item in translist:
            if " " in item:
                index1 = translist.index(item)
                temp = item.split(" ")
                for item in temp:
                    if "~" in item:
                        temp2 = item.replace("~", "")
                        tempIndex = temp.index(item)
                        temp[tempIndex] = temp2
                        temp2 = str(cdekeys[temp2])  # excuse my messy code here
                        temp[tempIndex] = temp2
                        temp2 = temp2 + ". "
                        temp[tempIndex] = temp2
                    else:
                        index2 = temp.index(item)
                        item = str(cdekeys[item])
                        temp[index2] = item

                item = " ".join(temp)
                translist[index1] = item
            elif "~" in item:
                temp = item.replace("~", "")
                temp = str(cdekeys[temp])
                index = translist.index(item)
                item = temp + ". "
                translist[index] = item
            else:
                index = translist.index(item)
                translist[index] = item.replace(item, str(cdekeys[item]))
        totranslate = "".join(translist)
    else:
        pass
    print(totranslate)
    totranslate = "You did not choose a valid action."
    ask = input("Another task? Y or N")
    return ask


while complete is False:
    ask2 = translate()
    if ask2 == "Yes" or ask2 == "Y":
        translate()
    else:
        complete = True
        sys.exit()
