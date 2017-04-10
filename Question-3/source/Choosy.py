from girl import girl
class Choosy(girl):
	'Class for choosy girl'
	def __init__(self,name,attractiveness,maintenance_budget,intelligence,type_):
		'Constructor for initialising choosy girl'
		girl.__init__(self,name,attractiveness,maintenance_budget,intelligence,type_)

	