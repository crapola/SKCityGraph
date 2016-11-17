"""
Functions used to access Sorcerer King data.
"""

from config import GAME_PATH
import os

def check_path():
	"""
	Will quit if config.GAME_PATH is not set to a correct path.
	"""
	if not os.path.isdir(GAME_PATH):
		print("GAME_PATH «",GAME_PATH,"» is invalid.\n\
Open config.py and make it point to Sorcerer King's game root folder.")
		quit()