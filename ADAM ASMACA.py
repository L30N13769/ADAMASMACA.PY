# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|  |
  /   |
       |
--------"""]
kelimeler = ["zümrüt", "yakut", "elmas", "safir", "kehribar", "pırlanta"]
kelime = random.choice(kelimeler)
tahminler = []

kelimeler = ["zümrüt", "yakut", "elmas", "safir", "kehribar", "pırlanta"]
kelime = random.choice(kelimeler)
tahminler = set()

print("Adam Asmaca oyununa hoş geldiniz!")
print("Bulmanız gereken kelime {} harfli.".format(len(kelime)))

while True:
    bosluklu_kelime = ""
    for harf in kelime:
        if harf in tahminler:
            bosluklu_kelime += harf + " "
        else:
            bosluklu_kelime += "_ "
    print(bosluklu_kelime)

    tahmin = input("Bir harf girin: ").lower()

    if tahmin in tahminler:
        print("Bu harfi daha önce tahmin ettiniz. Lütfen başka bir harf girin.")
        continue

    tahminler.add(tahmin)

    if tahmin not in kelime:
        print("Yanlış!")
        print(resim[len(tahminler)])
        if len(tahminler) == len(resim) - 1:
            print("Kaybettiniz! Doğru kelime '{}' idi.".format(kelime))
            break

    if all(harf in tahminler for harf in kelime):
        print("Tebrikler! Kelimeyi doğru bildiniz. Kelime '{}'. ".format(kelime))
        break









