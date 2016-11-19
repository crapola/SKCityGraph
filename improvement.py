class Improvement:
	def __init__(self,e):
		"""
		Construct from XML element e.
		"""
		self.internal_name=e.get('InternalName')
		self.icon=e.findtext('ArtDef')
		self.display_name=e.findtext('DisplayName')
		self.description=e.findtext('Description')
		# There's always only one requirement.
		self.required_improvement=e.findtext('RequiredImprovement')
		# Get race prereq, also assumes there's only one.
		prereqs=e.findall('Prereq')
		r=next((x for x in prereqs if x.findtext('Type')=='Race'),None)
		self.race=r.findtext('Attribute') if r else None
		self.cost=123


	def print(self):
		print(self.__dict__)