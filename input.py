# -*- coding: latin-1 -*-

import sys
import base64
import filtre as filt
import codecs
from termcolor import colored, cprint

argv = sys.argv


def utf8len(str):
    return len(str.encode('utf-8'))


class Interface:

    def __init__(self):
        self.parse_args()
        self.init_mode()
        self.get_texts()
        self.get_xored_texts()
        self.get_res()

    def parse_args(self):
        if len(argv) < 2:
            cprint("No cyphertext(s)/mode", 'cyan')
            exit()
        self.n_team = argv[1]
        self.n_ciphertext = int(argv[2])

    def init_mode(self):
        self.mode = argv[-1]
        if self.mode == '1':
            print("Mode 1: search the strings with alphabet and space")
        elif self.mode == '2':
            print("Mode 2: search the strings with alphabet and some typo")

    def xor_offset(self, word, text, n):
        if n <= len(text):
            subtext = text[n:max(n + len(word), len(text))]
            word2 = self.xor_strings(word, subtext)
            while len(word2) != len(word):
                word2 = word2 + " "
        else:
            word2 = " " * len(word)
        return repr(word2)

    def get_texts(self):
        self.texts = list(range(self.n_ciphertext))
        for i in range(self.n_ciphertext):
            n_f = chr(i + 97)
            with open('team' + self.n_team + '/' + 'message' + self.n_team + '_' + n_f + '.txt.enc') as f:
                content = f.read()
            content = content.replace('\n', '')
            content = base64.b64decode(content).decode("latin")
            # print('Message', i + 1, ':', len(content))
            self.texts[i] = content

    def xor_strings(self, xs, ys):
        return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

    def get_xored_texts(self):
        xored_texts = list()
        index_texts = list()
        samplesize = self.n_ciphertext
        for i in range(samplesize):
            for j in range(i + 1, samplesize, 1):
                index_texts.append((i + 1, j + 1))
                xored_texts.append(self.xor_strings(
                    self.texts[i], self.texts[j]))

        self.index_texts = index_texts
        self.xored_texts = xored_texts

    def get_input_word(self):
        if self.input_bis != "":
            self.input_word = self.input_bis
            self.input_bis = ""
        else:
            self.input_word = input("Guess a word or edit the offset: ")
        self.offset = -1
        while self.input_word.isnumeric():
            self.offset = int(self.input_word) - 1
            self.input_word = input("Guess a word or edit the offset: ")
        self.input_word = self.input_word.replace("\\", "0x0a")

    def get_res(self):
        self.offset = -1
        self.input_bis = ""
        while True:
            self.get_input_word()

            if len(self.input_word) != 0:
                while len(self.input_bis) == 0:
                    self.offset += 1

                    self.print_res()
                    self.input_bis = input(
                        "Guess a word or edit the offset. Enter to print the next matching pattern: ")
                    self.is_numeric()
                    self.is_write()
            else:
                self.offset += 1
                if self.offset > 1000:
                    self.input_bis = ""

    def print_res(self):
        self.readable = False
        while self.readable is False:
            self.is_readable()
        if self.readable is True:
            print(self.input_word, 'with offset', self.offset)
            for i in range(len(self.res_texts)):
                if not self.res_texts[i][1:-1].isspace():
                    if self.mode_readable(self.res_texts[i]):
                        cprint(str(i + 1) + ' :  ' +
                               str(self.index_texts[i]) + ' ' + self.res_texts[i], 'white',  'on_cyan', attrs=['bold'])
                        print('\n')
                    else:
                        print(i + 1, ': ',
                              self.index_texts[i], self.res_texts[i] + '\n')
                    print(len(self.res_texts[i]))

    def mode_readable(self, text):
        if ((self.mode == '0') or (self.mode == '1' and filt.is_string_only_letter(text)) or (self.mode == '2' and filt.is_string_correct(text))) and filt.is_string_letter(text):
            return True

    def is_readable(self):
        self.res_texts = []
        for i in range(len(self.xored_texts)):
            text2 = self.xor_offset(
                self.input_word, self.xored_texts[i], self.offset)
            self.res_texts.append(text2)
            if self.mode_readable(text2) is True:
                self.readable = True

        if self.readable is False:
            self.offset += 1
            if self.offset > 1000:
                self.readable = True

    def is_numeric(self):
        if self.input_bis.isnumeric():
            self.offset = int(self.input_bis) - 1
            self.input_bis = ""

    def is_write(self):
        command = self.input_bis.split()
        if len(command) > 0 and command[0] == 'w':
            count = [0] * self.n_ciphertext
            common = int(command[1])
            with_common = list()
            for i in range(len(self.res_texts)):
                if self.index_texts[i][0] == common:
                    with_common.append(
                        (self.index_texts[i][1], self.res_texts[i][1: -1]))
                if self.index_texts[i][1] == common:
                    with_common.append(
                        (self.index_texts[i][0], self.res_texts[i][1: -1]))
            with open('res' + self.n_team + '.txt', 'r+', encoding="latin-1") as f:
                f.seek(3 + (common - 1) * 801 + self.offset)
                f.write(self.input_word)

                for i in range(len(with_common)):
                    to_write = with_common[i][1]
                    to_write = to_write.replace("\\n", "\\")
                    print(len(to_write))
                    f.seek(3 + (with_common[i][0] - 1) * 801 + self.offset)
                    print(to_write)
                    f.write(to_write)
            self.input_bis = ""


if __name__ == '__main__':
    Interface()
