
import sys
import time
import argparse
import os

# Add parent directory to import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inspire_hand import InspireHand


# Update with correct serial port from your setup
SERIAL_PORT = "/dev/tty.usbserial-210"

hand = InspireHand(SERIAL_PORT, baudrate=115200)
hand.open()

# Move to initial neutral pose
hand.move_all([500] * 6)
time.sleep(1)

# Define crawl steps
crawl_steps = [
    [700, 700, 500, 500, 500, 500],  # lift front fingers
    [500, 500, 700, 700, 500, 500],  # lift rear fingers
]

print("🟢 Starting crawl loop...")
for _ in range(10):  # Repeat 10 times
    for pose in crawl_steps:
        hand.move_all(pose)
        time.sleep(0.5)

# Return to neutral
hand.move_all([500] * 6)
hand.close()
print("✅ Crawl finished.")