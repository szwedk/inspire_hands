#!/usr/bin/env python3
"""
Real-time finger tracking with MediaPipe to control Inspire Hand. 
<<<<<<< HEAD:inspire-test.py
=======
Written by Kamil Szwed, started Project on 07.15.25
>>>>>>> 6cf2fb8 (Initial commit: Inspire 5-finger hand control code):examples/inspire-test.py
Using inspire_hand Library + Mediapipe Library
"""

import cv2
import time
import math
import sys
import os
0
#  parent directory to import path for InspireHand
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inspire_hand import InspireHand

import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def calc_flexion(lm_tip, lm_base):
    dx = lm_tip.x - lm_base.x
    dy = lm_tip.y - lm_base.y
    dz = lm_tip.z - lm_base.z
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


def map_flexion_to_motor(flex_val, min_flex=0.05, max_flex=0.15):
    flex_val = max(min_flex, min(max_flex, flex_val))  # Clamp
    return int(((flex_val - min_flex) / (max_flex - min_flex)) * 1000)


def main():
    port = "/dev/tty.usbserial-210"
    baud = 115200
    hand = InspireHand(port=port, baudrate=baud)
    hand.open()
    print(f"Connected to Inspire Hand on {port}")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6) as hands:
        try:
            frame_count = 0
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    continue
                frame_count += 1
                if frame_count % 2 != 0:
                    continue  #skip every other frame  

                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        lm = hand_landmarks.landmark

                        thumb_val = calc_flexion(lm[4], lm[2])
                        index_val = calc_flexion(lm[8], lm[5])
                        middle_val = calc_flexion(lm[12], lm[9])
                        ring_val = calc_flexion(lm[16], lm[13])
                        little_val = calc_flexion(lm[20], lm[17])

                        thumb_motor = map_flexion_to_motor(thumb_val)
                        index_motor = map_flexion_to_motor(index_val)
                        middle_motor = map_flexion_to_motor(middle_val)
                        ring_motor = map_flexion_to_motor(ring_val)
                        little_motor = map_flexion_to_motor(little_val)

                        motor_vals = [
                            thumb_motor,  #Thumb bend
                            thumb_motor,  #Thumb rotate reuse
                            index_motor,
                            middle_motor,
                            ring_motor,
                            little_motor
                        ]

                        hand.thumb_bend.move(motor_vals[0])
                        hand.thumb_rotate.move(motor_vals[1])
                        hand.index_finger.move(motor_vals[2])
                        hand.middle_finger.move(motor_vals[3])
                        hand.ring_finger.move(motor_vals[4])
                        hand.little_finger.move(motor_vals[5])
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                cv2.imshow('MediaPipe Hand Tracking', image)
                if cv2.waitKey(5) & 0xFF == 27:
                    break
        except KeyboardInterrupt:
            print("keyboard Exit")
        finally:
            cap.release()
            cv2.destroyAllWindows()
            hand.close()
            print("Disconnected")


if __name__ == "__main__":
    main()