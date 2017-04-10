class girl:
	'Class for girl'
	name = ''
	attractiveness = 0
	maintenance_budget = 0
	intelligence = 0
	relationship_status = ''
	boyfriend = ''
	happiness=0
	type_= ''
	def __init__(self,name,attractiveness,maintenance_budget,intelligence,type_):
		'Constructor fot initialising girl'
		self.name = name
		self.attractiveness = attractiveness
		self.maintenance_budget = maintenance_budget
		self.intelligence = intelligence
		self.relationship_status = 'single'
		self.boyfriend = ''
		self.happiness=0
		self.type_=type_

	def set_happiness(self,happiness) :
		'Method for setting happiness'
		self.happiness=happiness

	def set_boyfriend(self,boyfriend):
		'Fucntion for setting boyfriend'
		self.boyfriend=boyfriend

	def modify_maintenance_budget(self,budget):
		'Function for modifying maintainence budget'
		self.maintenance_budget=budget
	
	def is_eligible(self, boys_girlfriend_budget):
		'Method for checking the eligibility'
		if (self.maintenance_budget <= boys_girlfriend_budget):
			return True
		else:
			return False
