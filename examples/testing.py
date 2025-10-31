#!/usr/bin/env python3
"""
Simple Inspire Hand test menu:
- Open all
- Close all
- Point middle finger
- Pinch golf ball

Assumes each actuator accepts 0..1000. If your hand is inverted, flip OPEN_VAL and CLOSE_VAL.
"""

import time
import sys
import os
import argparse

# Add parent to path so `from inspire_hand import InspireHand` works when running from examples/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inspire_hand import InspireHand  # noqa: E402

# Tunables
OPEN_VAL = 0          # fully open
CLOSE_VAL = 1000      # fully closed
THUMB_ROT_NEUTRAL = 500  # neutral thumb rotation
MOVE_DELAY = 0.6      # seconds to allow motion to complete

def set_fingers(hand, thumb_bend, thumb_rot, index, middle, ring, little):
    hand.thumb_bend.move(thumb_bend)
    hand.thumb_rotate.move(thumb_rot)
    hand.index_finger.move(index)
    hand.middle_finger.move(middle)
    hand.ring_finger.move(ring)
    hand.little_finger.move(little)
    time.sleep(MOVE_DELAY)

def pose_open_all(hand):
    set_fingers(hand, OPEN_VAL, THUMB_ROT_NEUTRAL, OPEN_VAL, OPEN_VAL, OPEN_VAL, OPEN_VAL)

def pose_close_all(hand):
    set_fingers(hand, CLOSE_VAL, THUMB_ROT_NEUTRAL, CLOSE_VAL, CLOSE_VAL, CLOSE_VAL, CLOSE_VAL)

def pose_point_middle(hand):
    """
    Middle finger extended, others closed.
    Adjust OPEN_VAL and CLOSE_VAL if your hardware direction differs.
    """
    set_fingers(hand, CLOSE_VAL, THUMB_ROT_NEUTRAL, CLOSE_VAL, OPEN_VAL, CLOSE_VAL, CLOSE_VAL)

def pose_pinch_golf_ball(hand):
    """
    Simple pinch meant to approximate holding a golf ball between thumb and index.
    Tune the values as needed for your hand geometry.
    """
    thumb_bend = 650
    thumb_rot = 600          # slight pronation toward index
    index = 700
    middle = 300             # relaxed support
    ring = 300               # relaxed support
    little = 300             # relaxed support
    set_fingers(hand, thumb_bend, thumb_rot, index, middle, ring, little)

def relax(hand):
    """
    Lightly flexed, natural pose.
    """
    set_fingers(hand, 300, THUMB_ROT_NEUTRAL, 300, 300, 300, 300)

def menu():
    print("\n--- Inspire Hand Test ---")
    print("1) Open all")
    print("2) Close all")
    print("3) Point middle finger")
    print("4) Pinch golf ball")
    print("5) Relax")
    print("6) Exit")
    return input("Select an option: ").strip()

def main():
    parser = argparse.ArgumentParser(description="Simple Inspire Hand test menu")
    parser.add_argument("--port", default="/dev/tty.usbserial-210", help="Serial port")
    parser.add_argument("--baud", type=int, default=115200, help="Baud rate")
    args = parser.parse_args()

    hand = InspireHand(port=args.port, baudrate=args.baud)
    hand.open()
    print(f"Connected to Inspire Hand on {args.port}")

    try:
        relax(hand)
        while True:
            choice = menu()
            if choice == "1":
                pose_open_all(hand)
            elif choice == "2":
                pose_close_all(hand)
            elif choice == "3":
                pose_point_middle(hand)
            elif choice == "4":
                pose_pinch_golf_ball(hand)
            elif choice == "5":
                relax(hand)
            elif choice == "6":
                break
            else:
                print("Invalid selection")
    except KeyboardInterrupt:
        print("\nInterrupted")
    finally:
        relax(hand)
        hand.close()
        print("Disconnected")

if __name__ == "__main__":
    main()