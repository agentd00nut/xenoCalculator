import pprint
from copy import deepcopy
import json
## Element list
#	f = fire
#	w = water
#	g = earth ( ground )
#	e = electric
#	a = wind ( air )
#	i = ice
# 	l = light
# 	d = dark

# Driver blade element list
# Doubling the number of elements for a driver ( f,f,i,i  instead of just f,i )
#		Is used for the players driver to indicate that they can build combos faster than NPC's on average.
team={
	0:["f","f","i","i"], 
	1:["w","a"],
	2:["g"]
}


pp=pprint.PrettyPrinter(indent=4);
def pretty(d, indent=-1):
	if(indent==0):
		print()
	try:
		for key, value in d.items():
			print(' ' * indent + str(key))
			if isinstance(value, dict) or isinstance(value, list):
				pretty(value, indent+1)
			else:
				print(' ' * (indent+1) + str(value))
			#print()
	except AttributeError:
		for value in d:
			#print(d.__class__.__name__)
			if isinstance(value, dict):
				pretty(value, indent+1)
			else:
				print(' ' * (indent+1) + str(value) )
combos={
	"f":{
		"f":["f","l"],
		"w":["f","i"]
	},
	"w":{
		"w":["f","d"],
		"g":["a"]
	},
	"g":{
		"f":["a","g"],
		"g":["e"]
	},
	"e":{
		"f":["a","i"],
		"e":["w"]
	},
	"a":{
		"a":["g","e"],
		"i":["i"]
	},
	"i":{
		"w":["a"],
		"i":["g","d"]
	},
	"l":{
		"e":["f"],
		"l":["w","l"]
	},
	"d":{
		"l":["e"],
		"d":["g","d"]
	}
}


def getElementCount(d):
	c={}
	for k in d:
		
		if not isinstance(k, int): # Add element to count if its not numeric
			if k in c:
				c[k]+=1
			else:
				c[k]=1


		if isinstance(d[k], dict): # Recurse over dictionaries.
			x=getElementCount(d[k])

			for i in x.keys():
				if not isinstance(i, int):
					if i in c:
						c[i]+=x[i]
					else:
						c[i]=x[i]
		
		elif isinstance(d[k], list): # Add a lists elements to counts
			for i in d[k]:
				if not isinstance(i, int):
					if i in c:
						c[i]+=1
					else:
						c[i]=1
	return c

def findCombos(combos, team):
	viableCombos=[]
	teamBAK=deepcopy(team);
	
	for e in combos.keys():
		team=deepcopy(teamBAK)
		
		if e in team: # First art

			combo={e:[]}
			combo2=[]
			team[e]-=1;

			for i in combos[e]:
				if i in team: # Second art
					if team[i] >0:

						team_2BAK=deepcopy(team[i]);
						team[i]-=1;
						combo2={i:[]}
						j=combos[e][i]

						for x in j:
							if x in team:
								team_3BAK=deepcopy(team[x])
								if team[x] > 0: # Third art
									team[x]-=1;
									combo2[i].append(x)
								team[x]=deepcopy(team_3BAK)

						team[i]=deepcopy(team_2BAK)

						combo[e].append(combo2)
			viableCombos.append(combo)

	return viableCombos

def getComboCount(combos):
	count={"one":{}, "two":{}, "three":{}}
	total={"one":0, "two":0,"three":0}
	for combo in combos:
		for c1 in combo:
			if c1 in count["one"]:
				count["one"][c1]+=1
				total["one"]+=1
			else:
				count["one"][c1]=1
				total["one"]+=1

			for c2 in combo[c1]:


				if list(c2)[0] in count["two"]:
					count["two"][list(c2)[0]]+=1
					total["two"]+=1
				else:
					count["two"][list(c2)[0]]=1
					total["two"]+=1

				for c3 in c2[list(c2)[0]]:
					if c3 in count["three"]:
						count["three"][c3]+=1
						total["three"]+=1
					else:
						count["three"][c3]=1
						total["three"]+=1

	return {"counts":count, "totals":total}

x=getElementCount(team)
y=findCombos(combos, x)
#pp.pprint(y)
print("Possible Combos: ")
pretty(y)
print()
#pp.pprint(getComboCount(y))
#json.dumps(getComboCount(y),indent=4)

counts = getComboCount(y);

print("Team:")
print("	0:	", team[0])
print("	1:	", team[1])
print("	2:	", team[2])
print()
print("Combo counts:")
print("	One 	", counts["counts"]["one"])
print("	Two 	", counts["counts"]["two"])
print("	Three 	", counts["counts"]["three"])
print()
print("Combo Totals:")
print("	One:	", counts["totals"]["one"])
print("	Two:	", counts["totals"]["two"])
print("	Three:	", counts["totals"]["three"])