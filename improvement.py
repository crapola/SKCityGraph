class Improvement:
	def __init__(self,e):
		"""
		Construct from XML element e.
		"""
		self.internal_name=e.get('InternalName')
		self.icon=e.findtext('ArtDef')
		self.display_name=e.findtext('DisplayName')
		self.description=e.findtext('Description')
		# There's always only one requirement, at least so far.
		self.required_improvement=e.findtext('RequiredImprovement')

	def print(self):
		print(self.__dict__)