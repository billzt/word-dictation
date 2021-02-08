# Word Dictation
A word or sentence dictation script based on MacOS.
It wroks in an interative shell. When you input `n` once, it will speak a line in file `dictation.txt` in ***random order***. 

# Run
1. Download and unpack this archive. 
2. Double-click `dictation.command`. 
3. An interative shell will appear. Then you can input your commands.

# Commands
```bash
n  # start dictation, or jump to the Next word/sentence.
r  # Repeat the previous word/sentence.
s  # Save answers manually. 
```
You can press key `↑`  to repeat the former command.
If you want to exit in the middle steps, press `Control+D`.

# Modify `dictation.txt`
The first line starting with `###LANG=` indicates the ***two-letter language code***. Supporting languages are:
（It might vary depending on your computer. Open your terminal and run `say -v '?'` to see the language list in your own system）
| Name | Gender | Lang | FullLang |
| --- | --- | --- | --- |
| Maged | Male | ar | ar_SA |
| Zuzana | Female | cs | cs_CZ |
| Sara | Female | da | da_DK |
| Anna | Female | de | de_DE |
| Melina | Female | el | el_GR |
| Alex | Male | en | en_US |
| Daniel | Male | en | en_GB |
| Fiona | Female | en | en-scotlan |
| Fred | Male | en | en_US |
| Karen | Female | en | en_AU |
| Moira | Female | en | en_IE |
| Rishi | Male | en | en_IN |
| Samantha | Female | en | en_US |
| Tessa | Female | en | en_ZA |
| Veena | Female | en | en_IN |
| Victoria | Female | en | en_US |
| Diego | Male | es | es_AR |
| Jorge | Male | es | es_ES |
| Juan | Male | es | es_MX |
| Monica | Female | es | es_ES |
| Paulina | Female | es | es_MX |
| Satu | Female | fi | fi_FI |
| Amelie | Female | fr | fr_CA |
| Thomas | Male | fr | fr_FR |
| Carmit | Female | he | he_IL |
| Lekha | Female | hi | hi_IN |
| Mariska | Female | hu | hu_HU |
| Damayanti | Female | id | id_ID |
| Alice | Female | it | it_IT |
| Luca | Male | it | it_IT |
| Kyoko | Female | ja | ja_JP |
| Otoya | Male | ja | ja_JP |
| Yuna | Female | ko | ko_KR |
| Nora | Female | nb | nb_NO |
| Ellen | Female | nl | nl_BE |
| Xander | Male | nl | nl_NL |
| Zosia | Female | pl | pl_PL |
| Joana | Female | pt | pt_PT |
| Luciana | Female | pt | pt_BR |
| Ioana | Female | ro | ro_RO |
| Milena | Female | ru | ru_RU |
| Yuri | Male | ru | ru_RU |
| Laura | Female | sk | sk_SK |
| Alva | Female | sv | sv_SE |
| Kanya | Female | th | th_TH |
| Yelda | Female | tr | tr_TR |
| Mei-Jia | Female | zh | zh_TW |
| Sin-ji | Female | zh | zh_HK |
| Ting-Ting | Female | zh | zh_CN |

The second line starting with `###RANDOM=` indicates whether you want to dictate in random order (1) or not (0).

Following lines are words or sentences to be dictated. One line by one line.

# Modify `dictation.py`
By default, only English (en) and Japanese (jp) has been included. See
https://github.com/billzt/word-dictation/blob/2daca547d8b9f1f9e19125e7bc53e39f39009ec2/dictation.py#L60

If you want to add other languages, add language to this line. For example, add French:
```python
lang2voice = {"en":'Alex Fiona Karen Daniel Samantha Tessa Fred Moira Veena Rishi Victoria', "jp":'Kyoko Otoya', "fr":'Amelie Thomas'}
```

# Check your answers!
After finishing dictation, you can find answers in `dictation_answer.txt`. During the dictation process, you can also type `s` to save current answers manually. However if you set `RANDOM=0`, the answers would be the same with `dictation.txt`.


