"""
    I create this script to crerate utils for this part of the projects.
    Including two functions that runs the logic behind part 2.
"""

import platform
import ctypes

def validate_student_id(student_id):
    """
        Args:
            student_id: this value is tajen from the Form
        Returns boolean:
            if entered value is in valid_id's returns True else False
    """
    valid_ids = ["1190652", "1234567", "0101010", "2211221"]
    return student_id in valid_ids

def lock_screen():
    """
    Locks the screen based on the operating system.
    """
    system_platform = platform.system()

    if system_platform == 'Windows':
        # Implement locking for Windows using ctypes
        ctypes.windll.user32.LockWorkStation()