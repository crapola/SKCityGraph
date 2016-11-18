"""
Functions used to access Sorcerer King data.
"""

from config import GAME_PATH
import os
import xml.etree.ElementTree

def check_path():
	"""
	Will quit if config.GAME_PATH is not set to a correct path.
	"""
	if not os.path.isdir(GAME_PATH):
		print("GAME_PATH «",GAME_PATH,"» is invalid.\n\
Open config.py and make it point to Sorcerer King's game root folder.")
		quit()

def load_improvements():
	"""
	Load CoreImprovements.xml.

	Returns
	-------
	xml.etree.ElementTree.Element
		Root of the XML hierarchy.
	"""
	tree=xml.etree.ElementTree.parse(GAME_PATH
		+"\data\English\Core Improvements\CoreImprovements.xml")
	root=tree.getroot()
	# Remove DataChecksum element.
	root.remove(root[0])
	return root

def extract_improvements(root_element):
	"""
	Convert XML to a list of Improvements.

	Parameters
	----------
	root_element : xml.etree.ElementTree.Element
		Base of the XML tree.

	Returns
	-------
	list of Improvement
		The list of improvements.
	"""
	return ()