from gift_item import Gift
class Essential(Gift):
	'Class for Essential gift'
	def __init__(self,name,cost,value,type_) :
		'Constructor for initialising essential gifts.'
		Gift.__init__(self,name,cost,value,type_)