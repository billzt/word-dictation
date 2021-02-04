# word-dictation
A word or sentence dictation script based on MacOS.
It wroks in an interative shell. When you press Enter once, it will speak a line in file `dictation.txt` in ***random order***. 

# Run
1. Download and unpack this archive. 
2. Double-click 'dictation.command'. 
3. An interative shell will appear. Then you can input your commands.

# Commands
```bash
n  # Start dictation, or jump to the Next word/sentence.
r  # Repeat the previous word/sentence.
```
You can use "Enter" directly to repeat the former command.
If you want to exit in the middle steps, press Control+D.

# Modify `dictation.txt`
The first line starting with `###` indicates the language code. Supporting languages are:
｜   Name   ｜   Gender   ｜   Lang   ｜   FullLang   ｜
｜   ---   ｜   ---   ｜   ---   ｜   ---   ｜
｜   Maged   ｜   Male   ｜   ar   ｜   ar_SA   ｜
｜   Zuzana   ｜   Female   ｜   cs   ｜   cs_CZ   ｜
｜   Sara   ｜   Female   ｜   da   ｜   da_DK   ｜
｜   Anna   ｜   Female   ｜   de   ｜   de_DE   ｜
｜   Melina   ｜   Female   ｜   el   ｜   el_GR   ｜
｜   Alex   ｜   Male   ｜   en   ｜   en_US   ｜
｜   Daniel   ｜   Male   ｜   en   ｜   en_GB   ｜
｜   Fiona   ｜   Female   ｜   en   ｜   en-scotlan   ｜
｜   Fred   ｜   Male   ｜   en   ｜   en_US   ｜
｜   Karen   ｜   Female   ｜   en   ｜   en_AU   ｜
｜   Moira   ｜   Female   ｜   en   ｜   en_IE   ｜
｜   Rishi   ｜   Male   ｜   en   ｜   en_IN   ｜
｜   Samantha   ｜   Female   ｜   en   ｜   en_US   ｜
｜   Tessa   ｜   Female   ｜   en   ｜   en_ZA   ｜
｜   Veena   ｜   Female   ｜   en   ｜   en_IN   ｜
｜   Victoria   ｜   Female   ｜   en   ｜   en_US   ｜
｜   Diego   ｜   Male   ｜   es   ｜   es_AR   ｜
｜   Jorge   ｜   Male   ｜   es   ｜   es_ES   ｜
｜   Juan   ｜   Male   ｜   es   ｜   es_MX   ｜
｜   Monica   ｜   Female   ｜   es   ｜   es_ES   ｜
｜   Paulina   ｜   Female   ｜   es   ｜   es_MX   ｜
｜   Satu   ｜   Female   ｜   fi   ｜   fi_FI   ｜
｜   Amelie   ｜   Female   ｜   fr   ｜   fr_CA   ｜
｜   Thomas   ｜   Male   ｜   fr   ｜   fr_FR   ｜
｜   Carmit   ｜   Female   ｜   he   ｜   he_IL   ｜
｜   Lekha   ｜   Female   ｜   hi   ｜   hi_IN   ｜
｜   Mariska   ｜   Female   ｜   hu   ｜   hu_HU   ｜
｜   Damayanti   ｜   Female   ｜   id   ｜   id_ID   ｜
｜   Alice   ｜   Female   ｜   it   ｜   it_IT   ｜
｜   Luca   ｜   Male   ｜   it   ｜   it_IT   ｜
｜   Kyoko   ｜   Female   ｜   ja   ｜   ja_JP   ｜
｜   Otoya   ｜   Male   ｜   ja   ｜   ja_JP   ｜
｜   Yuna   ｜   Female   ｜   ko   ｜   ko_KR   ｜
｜   Nora   ｜   Female   ｜   nb   ｜   nb_NO   ｜
｜   Ellen   ｜   Female   ｜   nl   ｜   nl_BE   ｜
｜   Xander   ｜   Male   ｜   nl   ｜   nl_NL   ｜
｜   Zosia   ｜   Female   ｜   pl   ｜   pl_PL   ｜
｜   Joana   ｜   Female   ｜   pt   ｜   pt_PT   ｜
｜   Luciana   ｜   Female   ｜   pt   ｜   pt_BR   ｜
｜   Ioana   ｜   Female   ｜   ro   ｜   ro_RO   ｜
｜   Milena   ｜   Female   ｜   ru   ｜   ru_RU   ｜
｜   Yuri   ｜   Male   ｜   ru   ｜   ru_RU   ｜
｜   Laura   ｜   Female   ｜   sk   ｜   sk_SK   ｜
｜   Alva   ｜   Female   ｜   sv   ｜   sv_SE   ｜
｜   Kanya   ｜   Female   ｜   th   ｜   th_TH   ｜
｜   Yelda   ｜   Female   ｜   tr   ｜   tr_TR   ｜
｜   Mei-Jia   ｜   Female   ｜   zh   ｜   zh_TW   ｜
｜   Sin-ji   ｜   Female   ｜   zh   ｜   zh_HK   ｜
｜   Ting-Ting   ｜   Female   ｜   zh   ｜   zh_CN   ｜
