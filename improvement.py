class Improvement:
	def __init__(self):
		self.internal_name="InvalidImprovement"
		self.display_name="Invalid Improvement"
		self.description="Description"
		self.required_improvement=None

	def print(self):
		print(self.__dict__)
