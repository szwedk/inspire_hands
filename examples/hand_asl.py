#!/usr/bin/env python3

import sys
import time
import argparse
import os

# parent directory to import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inspire_hand import InspireHand

# Define ASL gestures for letters
def sign_A(hand):
    hand.thumb_bend.move(300)
    hand.index_finger.close()
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_B(hand):
    hand.thumb_bend.move(600)
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.move(1000)
    hand.little_finger.move(1000)
def sign_C(hand):
    hand.thumb_bend.move(500)
    hand.index_finger.move(500)
    hand.middle_finger.move(500)
    hand.ring_finger.move(500)
    hand.little_finger.move(500)
def sign_D(hand):
    hand.thumb_bend.move(200)
    hand.index_finger.move(1000)
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_F(hand):
    hand.thumb_bend.move(1000)
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_G(hand):
    hand.thumb_bend.move(100)
    hand.index_finger.move(1000)
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_H(hand):
    hand.thumb_bend.move(100)
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_I(hand):
    hand.thumb_bend.close()
    hand.index_finger.close()
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.move(1000)
def sign_J(hand):
    sign_I(hand)
    time.sleep(0.5)
    hand.little_finger.move(800)
    time.sleep(0.2)
    hand.little_finger.move(600)
def sign_K(hand):
    hand.thumb_bend.move(600)
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_E(hand):
    hand.thumb_bend.move(400)
    hand.index_finger.move(300)
    hand.middle_finger.move(300)
    hand.ring_finger.move(300)
    hand.little_finger.move(300)
def sign_L(hand):
    hand.thumb_bend.move(100)
    hand.index_finger.move(1000)
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_M(hand):
    hand.index_finger.move(300)
    hand.middle_finger.move(300)
    hand.ring_finger.move(300)
    hand.thumb_bend.move(800)
    hand.little_finger.move(1000)
def sign_N(hand):
    hand.index_finger.move(300)
    hand.middle_finger.move(300)
    hand.thumb_bend.move(700)
    hand.ring_finger.close()
    hand.little_finger.move(1000)
def sign_O(hand):
    hand.thumb_bend.move(500)
    hand.index_finger.move(500)
    hand.middle_finger.move(500)
    hand.ring_finger.move(500)
    hand.little_finger.move(500)
def sign_P(hand):
    hand.thumb_bend.move(1000)
    hand.index_finger.move(1000)
    hand.middle_finger.move(800)
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_Q(hand):
    hand.thumb_bend.move(200)
    hand.index_finger.move(800)
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_R(hand):
    hand.thumb_bend.move(300)
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_S(hand):
    hand.thumb_bend.move(200)
    hand.index_finger.close()
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_T(hand):
    hand.thumb_bend.move(300)
    hand.index_finger.close()
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.move(1000)
def sign_U(hand):
    hand.thumb_bend.close()
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_V(hand):
    hand.thumb_bend.close()
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_W(hand):
    hand.thumb_bend.close()
    hand.index_finger.move(1000)
    hand.middle_finger.move(1000)
    hand.ring_finger.move(1000)
    hand.little_finger.close()
def sign_X(hand):
    hand.thumb_bend.move(200)
    hand.index_finger.move(200)
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.close()
def sign_Y(hand):
    hand.thumb_bend.move(1000)
    hand.index_finger.close()
    hand.middle_finger.close()
    hand.ring_finger.close()
    hand.little_finger.move(1000)
def sign_Z(hand):
    sign_index = hand.index_finger
    sign_index.move(1000)
    time.sleep(0.3)
    sign_index.move(800)
    time.sleep(0.3)
    sign_index.move(600)

ASL_SIGNS = {
    "A": sign_A,
    "B": sign_B,
    "C": sign_C,
    "D": sign_D,
    "E": sign_E,
    "F": sign_F,
    "G": sign_G,
    "H": sign_H,
    "I": sign_I,
    "J": sign_J,
    "K": sign_K,
    "L": sign_L,
    "M": sign_M,
    "N": sign_N,
    "O": sign_O,
    "P": sign_P,
    "Q": sign_Q,
    "R": sign_R,
    "S": sign_S,
    "T": sign_T,
    "U": sign_U,
    "V": sign_V,
    "W": sign_W,
    "X": sign_X,
    "Y": sign_Y,
    "Z": sign_Z,
}

def play_sign_sequence(hand, sequence, delay=1.5):
    for char in sequence:
        if char in ASL_SIGNS:
            print(f"Showing: {char}")
            ASL_SIGNS[char](hand)
            time.sleep(delay)
        else:
            print(f"Unknown character: {char}")

def main_menu():
    hand = InspireHand(port='/dev/tty.usbserial-210')
    hand.open()  # Manual connection

    try:
        while True:
            print("\n--- ASL Playback Menu ---")
            print("1. Show Letter A")
            print("2. Show Letter B")
            print("3. Show Letter C")
            print("4. Show Word: HELLO")
            print("5. Show Word: COOL")
            print("6. Exit")
            print("7. Spell Custom Word")

            choice = input("Select an option: ").strip()

            if choice == "1":
                sign_A(hand)
            elif choice == "2":
                sign_B(hand)
            elif choice == "3":
                sign_C(hand)
            elif choice == "4":
                play_sign_sequence(hand, "HELLO")
            elif choice == "5":
                play_sign_sequence(hand, "COOL")
            elif choice == "6":
                print("Exiting.")
                break
            elif choice == "7":
                word = input("Enter a word or phrase (letters A–Z only): ").upper()
                play_sign_sequence(hand, word)
            else:
                print("Invalid option. Please choose 1–7.")
    finally:
        hand.close()  # Ensure connection is closed

if __name__ == "__main__":
    main_menu()