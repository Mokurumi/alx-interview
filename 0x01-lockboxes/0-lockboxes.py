#!/usr/bin/python3
'''
Lockboxes
'''


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened
    '''
    if not boxes:
        return False
    keys = [0]

    # Check if all boxes can be opened
    for key in keys:
        # Check if box is not empty
        for new_key in boxes[key]:
            # Check if key is not already in keys
            if new_key not in keys and new_key < len(boxes):
                # Add key to keys
                keys.append(new_key)
    # Check if all boxes can be opened
    return len(keys) == len(boxes)
