import random 
import csv
import logging
import math
import pprint

from Miser import Miser
from Geek import Geek
from Generous import Generous 
from Choosy import Choosy
from Desperate import Desperate
from Normal import Normal
from Essential import Essential
from Luxury import 	Luxury
from Utility import Utility

from logs import log_maker
from couples import Couple
from boy import Boy
from girl import girl
from gift_item import Gift
from util import testing_util


logging.basicConfig(filename='log_text.log',datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',level=logging.DEBUG,filemode='w')


def calc_happiness(H):
	'Function to calculate happiness'
	with open('./gifts_list.csv', 'r') as csvfile:
		ffp = csv.reader(csvfile, delimiter = ',')
		gifts=[]
		for row in ffp:
			if (row[3] =='Luxury') :
				gifts += [Luxury(row[0], int(row[1]), int(row[2]), row[3])]
			elif (row[3] =='Essential') :
				gifts += [Essential(row[0], int(row[1]), int(row[2]), row[3])]
			elif (row[3] =='Utility') :
				gifts += [Utility(row[0], int(row[1]), int(row[2]), row[3])]
		csvfile.close()

	gifts = sorted(gifts, key=lambda item: item.cost)
	logging.warning('\n\nDetails of Gifts:\n')
	for i in H:
		if (i.boy.type_ == 'Miser'):
			miser(gifts, i)

		if (i.boy.type_ == 'Generous'):
			generous(gifts, i)

		if (i.boy.type_ == 'Geek'):
			geek(gifts, i)

	k = random.randint(1, len(H))
	happy_couple(H, k)

def happy_couple(H, k):
	'Function for calculating k happy couples'
	A = sorted(H, key=lambda item: item.happiness, reverse=True)
	B = sorted(H, key=lambda item: item.compatibility_status, reverse=True)
	print ('\n\n'+str(k) + ' most happy couples are as follows:')
	for i in range(k):
		print (A[i].boy.name + ' & ' + A[i].girl.name)
	print('***Beware from Anti-romeo squad***\n')
	
def generous(gifts, p):
	'Function for generous boy'
	b1 = 0
	b2 = 0
	for k in gifts:
		if  (p.boy.boys_girlfriend_budget - k.cost > 0) and (p.boy.boys_girlfriend_budget >= 0) and ((p.boy.boys_girlfriend_budget-k.cost <= 300) or (k.cost == p.boy.boys_girlfriend_budget) )  :
			if (k.type_ == 'Luxury'):
				b2 = b2 + 2*k.cost
			else:
				b2 = b2 + k.cost
			b1 = b1 + k.cost
			p.gifts = p.gifts + [k]
			p.boy.boys_girlfriend_budget = p.boy.boys_girlfriend_budget - k.cost
			logging.info(p.boy.name + '  gave  ' + p.girl.name + ' a  Gift:| ' + k.name + '| of price =Rs. ' + str(k.cost) + '\-.')
	if (p.girl.type_ == 'Choosy' and b2>0):
		p.girl.happiness = math.log10(b2)
	elif (p.girl.type_ == 'Normal'):
		p.girl.happiness = b1
	else:
		p.girl.happiness = math.exp(b1)
	p.boy.happiness = p.girl.happiness
	p.set_happiness()
	p.set_compatibility()

def miser(gifts, x):
	'Function for miser boy'
	b1 = 0
	b2 = 0
	for k in gifts:
		if (x.boy.boys_girlfriend_budget >= 0) and ( (k.cost-x.girl.maintenance_budget <= 100) or k.cost == x.girl.maintenance_budget) and (x.boy.boys_girlfriend_budget - k.cost > 0):
			if (k.type_ == 'Luxury'):
				b2 = b2 + 2*k.cost
			else:
				b2 = b2 + k.cost
			b1 = b1 + k.cost
			x.gifts = x.gifts + [k]
			x.boy.boys_girlfriend_budget = x.boy.boys_girlfriend_budget - k.cost
			log_maker(x.boy.name + '  gave ' + x.girl.name + 'a  Gift:| ' + k.name + '| of price = Rs.' + str(k.cost) + '\-')

	if (x.girl.type_ == 'Choosy' and b2>0):
		x.girl.happiness = math.log10(b2)
	elif (x.girl.type_ == 'Normal'):
		x.girl.happiness = b1
	else:
		x.girl.happiness = math.exp(b1)
	x.boy.happiness = x.boy.boys_girlfriend_budget
	x.set_happiness()
	x.set_compatibility()


def geek(gifts, c):
	'Function for geek boy'
	b1 = 0
	b2 = 0
	for g in gifts:
		if  (c.boy.boys_girlfriend_budget >= 0)  and ((g.cost-c.girl.maintenance_budget <= 100) or (g.cost == c.girl.maintenance_budget))and (c.boy.boys_girlfriend_budget - g.cost > 0):
			if (g.type_ == 'Luxury'):
				b2 = b2 + 2*g.cost
			else:
				b2 = b2 + g.cost
			b1 = b1 + g.cost
			c.gifts = c.gifts + [g]
			c.boy.boys_girlfriend_budget = c.boy.boys_girlfriend_budget - g.cost
			log_maker(c.boy.name + '  gave ' + c.girl.name + ' a  Gift:| ' + g.name + '| of price =Rs. ' + str(g.cost) + '\-.')

	for i in gifts:
		if (i not in c.gifts) and (i.type_ == 'Luxury') and (i.cost <= c.boy.boys_girlfriend_budget):
			b2 = b2 + 2*i.cost
			b1 = b1 + i.cost
			c.gifts = c.gifts + [i]
			c.boy.boys_girlfriend_budget = c.boy.boys_girlfriend_budget - i.cost
			log_maker(c.boy.name + '  gave  ' + c.girl.name + ' a  Gift:| ' + i.name + '| of price =Rs. ' + str(i.cost) + '\-.')
			break


	if (c.girl.type_ == 'Choosy' and b2>0):
		c.girl.happiness = math.log10(b2)
	elif (c.girl.type_ == 'Normal'):
		c.girl.happiness = b1
	else:
		c.girl.happiness = math.exp(b1)
	c.boy.happiness = c.girl.intelligence
	c.set_happiness()
	c.set_compatibility()

def gifts_details(H):
	'Function for gift details'
	for h in H:
		print ('Gifts given from : ' + h.boy.name + ' to : ' + h.girl.name + ':\n')
		for l in h.gifts:
			print ( l.name + '\tType: ' + l.type_)
		print ('\n')
		k = random.randint(1, len(H))
		happy_couple(H, k)

def test():
	'Function to test all other functions.'
	with open('./boys_list.csv', 'r') as csvfile:
		fp1 = csv.reader(csvfile, delimiter = ',')
		boy_lists =[]
		for i in fp1:
			if(i[5] == 'Miser') :
				boy_lists += [Miser(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]
			elif (i[5] == 'Generous') :
				boy_lists += [Generous(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]
			elif (i[5] == 'Geek') :
				boy_lists += [Geek(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]

		csvfile.close()

	with open('./girls_list.csv', 'r') as csvfile:
		fp2 = csv.reader(csvfile, delimiter = ',')
		girl_lists=[]
		for j in fp2:
			if(j[4] == 'Choosy') :
				girl_lists += [Choosy(j[0], int(j[1]), int(j[2]), int(j[3]), j[4])]
			elif(j[4] == 'Normal') :
				girl_lists += [Normal(j[0], int(j[1]), int(j[2]), int(j[3]), j[4])]
			elif(j[4] == 'Desperate') :
				girl_lists += [Desperate(j[0], int(j[1]), int(j[2]), int(j[3]), j[4])]
		csvfile.close()

	print("Choose allotment algorithm :\n1.Algorithm1\n2.Algorithm2\n")
	ch=int(input())
	Couple_list = []
	girl_lists=sorted(girl_lists, key=lambda girl: girl.maintenance_budget, reverse=True)
	boy_lists=sorted(boy_lists, key=lambda boy: boy.attractiveness, reverse=True)
	countg=0
	countb=0
	count=0
	limitg=len(girl_lists)
	limitb=len(boy_lists)
	if(ch==1):
		while 1:
			if (count%2!=0 and countb != len(boy_lists)) :
				l=boy_lists[countb]
				logging.warning('Boy chooses girl')
				for f in girl_lists:
					if l.relationship_status == 'single' and f.relationship_status == 'single' :
						f.relationship_status = 'in_a_relationship'
						l.relationship_status = 'in_a_relationship'
						f.boyfriend = l.name
						l.girlfriend = k.name
						log_maker(l.name + ' is in relationship with ' + f.name)
						Couple_list = Couple_list+[(l, f)]
						break
				countb+=1

			if (count%2==0 and countg != len(girl_lists)):
				logging.warning('Girl chooses boy')
				k=girl_lists[countg]
				for l in boy_lists:
					if l.relationship_status == 'single' and k.relationship_status == 'single' and (k.is_eligible(l.boys_girlfriend_budget)) and (l.is_eligible(k.maintenance_budget, k.attractiveness)) :
						k.relationship_status = 'in_a_relationship'
						l.relationship_status = 'in_a_relationship'
						k.boyfriend = l.name
						l.girlfriend = k.name
						log_maker(k.name + ' is in relationship with ' + l.name)
						Couple_list = Couple_list+[(l, k)]
						break		
				countg+=1
			count+=1
			if(countb == limitb and countg == limitg ) :
				break


	elif(ch==2):
		logging.warning('\n\nGirls are searching boys for relationship.\n')
		for k in girl_lists:
			for l in boy_lists:
				log_maker(k.name + '  is searching ' + l.name)
				if l.relationship_status == 'single' and k.relationship_status == 'single' and (k.is_eligible(l.boys_girlfriend_budget)) and (l.is_eligible(k.maintenance_budget, k.attractiveness)) :
					k.relationship_status = 'in_a_relationship'
					l.relationship_status = 'in_a_relationship'
					k.boyfriend = l.name
					l.girlfriend = k.name
					log_maker(k.name + ' is in relationship with ' + l.name)
					logging.warning('Beware from Anti-romeo squad.')
					Couple_list = Couple_list+[(l, k)]
					break

	logging.warning('***Beware from Anti-romeo squad***\n')
	
	print ('\n\nCouples in Relationship are :\n')
	for m in girl_lists:
		if m.relationship_status == 'in_a_relationship':
			print (m.name + ' is in relationship with ' + m.boyfriend+'\n')
	print('***Beware from Anti-romeo squad***\n')
	H=[]
	for i in Couple_list:
		H += [Couple(i[0],i[1])]
	calc_happiness(H)

testing_util()
test()