#!/usr/bin/python3

"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and,
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    opened_boxes = [False] * n  # Keep track of which boxes are opened
    opened_boxes[0] = True  # The first box is always opened
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        new_key = keys.pop()  # Get the next key to use
        if new_key < n and not opened_boxes[new_key]:  # If this key can open a box and the box is not opened
            opened_boxes[new_key] = True  # Mark the box as opened
            keys.extend(boxes[new_key])  # Add the new keys from the newly opened box

    return all(opened_boxes)  # Check if all boxes have been opened
