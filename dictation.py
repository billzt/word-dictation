#!/usr/bin/env python3

import argparse
import re
import sys
import cmd
import random
import os

current_num = 1
previous_line = ''
now_dictation_items = []
def save_answer():
    with open('dictation_answer.txt', mode='w') as f_answer:
        for i in range(len(now_dictation_items)):
            print(f'({i+1}) {now_dictation_items[i]}', file=f_answer)
        f_answer.close()
        print(f'Answers saved to dictation_answer.txt', file=sys.stderr)

class SayItem(cmd.Cmd):
    intro = 'Welcome to the dictation shell.  Type n to listen the next item, or r to repeat the previous item, or s to save current answers.\n'
    prompt = '(dictation) '
    def do_n(self, line):
        """n (means next)
        n (means next)"""
        global current_num
        global previous_line
        if len(items)>0:
            #print("hi,", items[0])
            print(f"Say {current_num}/{all_num} by voice: {voices[current_num%len(voices)]}")
            os.system(f'say -v {voices[current_num%len(voices)]} {items[0]}')
            previous_line = items[0]
            now_dictation_items.append(items[0])
            del(items[0])
            current_num += 1
        else:
            print('All finished')
            save_answer()
            return True

    def do_r(self, line):
        """r (means repeat)
        r (means repeat)"""
        if current_num == 1:
            print(f'Dictation has not begun yet. Please type n', file=sys.stderr)
        else:
            print(f"Say {current_num-1}/{all_num} [again] by voice:  {voices[(current_num-1)%len(voices)]}")
            os.system(f'say -v {voices[(current_num-1)%len(voices)]} {previous_line}')

    def do_s(self, line):
        """s (means save)
        s (means save)"""
        save_answer()

    def do_EOF(self, line):
        save_answer()
        return True

    def emptyline(self):
        1

    def postloop(self):
        print()

if __name__ == '__main__':
    items = []
    lang = 'na'
    with open('dictation.txt') as f:
        for line in f:
            words = line.strip()
            if words != '':
                if words.startswith('###LANG='):
                    lang = words.replace('###LANG=', '').strip()
                elif words.startswith('###RANDOM='):
                    rand_order = words.replace('###RANDOM=', '').strip()
                else:
                    items.append(line.strip())
    if rand_order == '1':
        random.shuffle(items)
    all_num = len(items)
    lang2voice = {"en":'Alex Fiona Karen Daniel Samantha Tessa Fred Moira Veena Rishi Victoria', "jp":'Kyoko Otoya'}
    if lang in lang2voice:
        voices = lang2voice[lang].split()
    else:
        print(f'Error language {lang}', file=sys.stderr)
        exit(0)

    SayItem().cmdloop()

