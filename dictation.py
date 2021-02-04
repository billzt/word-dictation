#!/usr/bin/env python3

'''Here is the title
Here is the document
'''

__author__ = 'Tao Zhu'
__copyright__ = 'Copyright 2019'
__license__ = 'GPL'
__version__ = '0.1'
__email__ = 'taozhu@mail.bnu.edu.cn'
__status__ = 'Development'

import argparse
import re
import sys
import cmd
import random
import os

current_num = 1
previous_line = ''

class SayItem(cmd.Cmd):
    intro = 'Welcome to the dictation shell.  Type n to listen the next item, or r to repeat the previous item.\n'
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
            del(items[0])
            current_num += 1
        else:
            print('All finished')
            return True

    def do_r(self, line):
        """r (means repeat)
        r (means repeat)"""
        if current_num == 1:
            print(f'Dictation has not begun yet. Please type n', file=sys.stderr)
        else:
            print(f"Say {current_num-1}/{all_num} in {voices[(current_num-1)%len(voices)]}")
            os.system(f'say -v {voices[(current_num-1)%len(voices)]} {previous_line}')

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()

if __name__ == '__main__':
    items = []
    lang = 'na'
    with open('dictation.txt') as f:
        for line in f:
            words = line.strip()
            if words != '':
                if words.startswith('###'):
                    lang = words.replace('###', '')
                else:
                    items.append(line.strip())
    random.shuffle(items)
    all_num = len(items)
    lang2voice = {"en":'Alex Fiona Karen Daniel Samantha Tessa Fred Moira Veena Rishi Victoria', "jp":'Kyoko Otoya'}
    if lang in lang2voice:
        voices = lang2voice[lang].split()
    else:
        print(f'Error language {lang}', file=sys.stderr)
        exit(0)

    SayItem().cmdloop()

#查看所有声音列表 say --voice='?'
#如使用婷婷语音 say -v Ting-Ting 北京欢迎您

