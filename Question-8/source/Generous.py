from boy import Boy 
class Generous(Boy):
	'Class for generous boy'
	def __init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_):
		'Constructor for initialising generous boy'
		Boy.__init__(self, name, attractiveness, girlfriend_budget, intelligence, minimum_attraction_requirement,type_)