"""
Functions used to access Sorcerer King data.
"""

from config import GAME_PATH
import improvement
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
	Load CoreImprovements.xml into an usable list.

	Returns
	-------
	list of improvement.Improvement
		The list of improvements.
	"""
	tree=xml.etree.ElementTree.parse(GAME_PATH
		+"\data\English\Core Improvements\CoreImprovements.xml")
	root=tree.getroot()
	# Remove DataChecksum element.
	root.remove(root[0])
	# Build and return the list of Improvement.
	r=[]
	for e in root:
		# Filter out things that aren't buildings.
		if e.find('RequiresResource')==None and e.find('HideInBuildList')==None\
		and e.findtext('LaborToBuild')!='0' and e.find('IsOutpostUpgrade')==None:
			req_level=e.findtext('ReqCityLevel')
			req_level=int(req_level) if req_level!=None else 0
			if req_level<9:
				r.append(improvement.Improvement(e))
	return r

def fix_icons(improvements):
	"""
	Replace ArtDefs by full path to PNG.
	"""
	art_xml=xml.etree.ElementTree.parse(GAME_PATH
		+"\data\English\Core Improvements\ArtImprovements.xml").getroot()

	icons_path=GAME_PATH+"\Gfx\Medallions\Improvements\\"

	for i in improvements:
		artdef=i.icon
		e=art_xml.find("ImprovementTypeArtDef[@InternalName='"+artdef+"']")
		if e:
			f=e.findtext('ImprovementTypeArtSubPack/Medallions/All')
			i.icon=icons_path+f