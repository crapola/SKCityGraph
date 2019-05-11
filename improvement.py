import config
import textwrap

class Improvement:
	def __init__(self,e):
		"""
		Construct from XML element e.
		"""
		self.internal_name=e.get('InternalName')
		self.display_name=e.findtext('DisplayName')
		self.description=e.findtext('Description')
		self.wrap_description()
		self.cost=e.findtext('LaborToBuild')

		self.required_improvements=[r.text for r in e.findall('RequiredImprovement')]

		# Get the race prereq if any.
		prereqs=e.findall('Prereq')
		r=next((x for x in prereqs if x.findtext('Type')=='Race'),None)
		self.race=r.findtext('Attribute') if r else None

		# Get the ability prereq if any.
		r=next((x for x in prereqs if x.findtext('Type')=='AbilityBonusOption'),None)
		self.required_ability=r.findtext('Attribute') if r else None
		
		# Set icon full path if present in CoreImprovement.
		# If not, set it to the ArtDef and it'll be fixed later.
		x=e.findtext("ImprovementTypeArtDef/ImprovementTypeArtSubPack/Medallions/All")
		if x is not None:
			self.icon=config.GAME_PATH+"\Gfx\Medallions\Improvements\\"+x
		else:
			self.icon=e.findtext('ArtDef')

	def __str__(self):
		return str(self.__dict__)

	def wrap_description(self):
		"""
		Graphviz doesn't support word wrapping.
		We have to add line breaks ourselves.
		"""
		lines=textwrap.wrap(self.description,50)
		self.description="<br/>".join(lines)