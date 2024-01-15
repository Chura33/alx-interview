#!/usr/bin/python3


"""
Module: lockboxes

This module provides a function to determine if all boxes can be opened
based on a set of rules.

Functions:
    canUnlockAll(boxes): Determine if all boxes can be opened.

Usage:
    # Example usage of canUnlockAll function
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()
    # Add the first box to the set since it's already open
    opened_boxes.add(0)

    # List to keep track of keys found in each step
    keys_to_check = boxes[0]

    # Iterate until there are keys to check
    while keys_to_check:
        # Get the first key from the list
        key = keys_to_check.pop(0)

        # Check if the key can open a new box
        if key < len(boxes) and key not in opened_boxes:
            # Add the new box to the set of opened boxes
            opened_boxes.add(key)
            # Add the keys from the new box to the list of keys to check
            keys_to_check.extend(boxes[key])

    return len(opened_boxes) == len(boxes)
