alphabet_array = [chr(ord('A') + i) for i in range(26)]
numbers_array = [str(i) for i in range(10)]
all_chr = alphabet_array + numbers_array
morse_code = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..",
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."
]


class Morse:
    def __init__(self):
        self.morse_output = []
        self.output = ""

    def to_morse(self, str_input):
        str_input = str_input.upper().split(" ")
        for word in str_input:
            for i in range(len(word)):
                if word[i] in all_chr:
                    self.morse_output.append(morse_code[all_chr.index(word[i])])
        self.output = " ".join(self.morse_output)
        return self.output

    def reset(self):
        self.output = ""
        self.morse_output = []
