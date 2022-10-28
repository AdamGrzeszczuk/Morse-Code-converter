from morse_source import morse_src


def convert(dots_dashes):
    converted_text = ""
    for dot in dots_dashes:
        if dot == " ":
            converted_text = converted_text + " "
        elif dot == ".":
            converted_text = converted_text + "·"
        elif dot == "-":
            converted_text = converted_text + '–'
        else:
            print(f"The character: {dot} is not a dot nor dash! Try again!")
            exit()
    return converted_text


def translate(text, direction):
    result_text = ""
    for letter in text:
        if letter == " ":
            char = " "
        else:
            if direction == "M":
                if letter.isalnum():
                    char = morse_src[letter.upper()]
                else:
                    print(f"The character: {letter} is non-alphanumeric! Try again")
                    exit()
            else:
                proper_morse_code = convert(letter)
                char = list(morse_src.keys())[list(morse_src.values()).index(proper_morse_code)]
        result_text = result_text + char
    return result_text


flag = True
while flag:
    direction = input(
        "Do you want to translate the text to Morse or Latin? Please select Morse (M) to translate to Morse or Latin "
        "alphabet (L) to translate Morse to Latin: ").upper()

    if direction != "M" and direction != "L":
        print("Provide correct selection input!")
    else:
        flag = False
text_to_translate = input("What would you like to translate? If Morse, separate each letter with a space. ")
if direction == "M":
    text_to_translate = [*text_to_translate]
else:
    text_to_translate = text_to_translate.split()

print("".join(translate(text_to_translate, direction)))
