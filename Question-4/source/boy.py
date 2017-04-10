class Boy:
	'Class for BOY'
	name = ''
	attractiveness = 0
	boys_girlfriend_budget = 0
	intelligence = 0
	minimum_attraction_requirement = 0
	type_= ''
	relationship_status = 'single'
	happiness=0
	girlfriend = ''
	def __init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_):
		'Constructor for initialising boy class'
		self.name = name
		self.attractiveness = attractiveness
		self.boys_girlfriend_budget = girlfriend_budget
		self.intelligence = intelligence
		self.minimum_attraction_requirement = minimum_attraction_requirement
		self.type_=type_
		self.relationship_status = 'single'
		self.happiness=0
		self.girlfriend = ''
	
	def set_happiness(self,happiness) :
		'Method for setting happiness'
		self.happiness=happiness

	def set_girlfriend(self,girlfriend):
		'Method for setting girlfriend'
		self.girlfriend=girlfriend
	
	def modify_boys_girlfriend_budget(self,budget):
		'Method for modifying the girlfriend budget'
		self.boys_girlfriend_budget=budget
		
	def is_eligible(self, maintenance_budget, attractiveness):
		'Method for checking the eligibility'
		if (self.boys_girlfriend_budget >= maintenance_budget) and (attractiveness >= self.minimum_attraction_requirement):
			return True
		else:
			return False