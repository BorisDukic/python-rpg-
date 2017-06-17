import random

#character
player = {"name":"Elfonja","xp": 0,"lvl":1,"dmg": 2,"hp":20,"pxp":5}

#monsters
imp = {"name":"Ruzni","lvl": 3,"dmg": 1,"hp": 10}
goblin = {"name":"Zeleni","lvl": 4,"dmg": 3,"hp": 25}
zmija = {"name":"Garmo","lvl": 1,"dmg":3,"hp": 5}


def imp_reduceHp(player, imp):
	if player.get('lvl') != imp.get('lvl'):
		imp['hp'] = imp['hp'] - random.choice(range(0, 15))
	if player.get('lvl') < imp.get('lvl'):
		player['hp'] =  player['hp'] - random.choice(range(3, 8))
def goblin_reduceHp(player, goblin):
	if player.get("lvl") != goblin.get("lvl"):
		goblin["hp"] = goblin["hp"] - random.choice(range(0, 6))
	if player.get("lvl") < goblin.get("lvl"):
		player["hp"] = player["hp"] - random.choice(range(0, 3))
def zmija_reduceHp(player, zmija):
	if player.get("lvl") != zmija.get("lvl"):
		zmija["hp"] = zmija["hp"] - random.choice(range(0, 15))
	if player.get("lvl") < zmija.get("lvl"):
		player["hp"] = player["hp"] - random.choice(range(0, 4))
"""
def random_att(player,imp,goblin,zmija):
	if player.get("lvl") < 2:
		if player.get('lvl') != imp.get('lvl'):
			imp['hp'] = imp['hp'] - random.choice(range(0, 15))
		if player.get('lvl') <imp.get('lvl'):
			player['hp'] =  player['hp'] - random.choice(range(3, 8))
	if player.get("lvl") > 1:
		if player.get("lvl") != goblin.get("lvl"):
			goblin["hp"] = goblin["hp"] - random.choice(range(0, 14))
		if player.get("lvl") < goblin.get("lvl"):
			player["hp"] = player["hp"] - random.choice(range(3,8))
	if player.get("lvl") = 1:
		if player.get("lvl") != zmija.get("lvl"):
			zmija["hp"] = zmija["hp"] - random.choice(range(0, 14))
		if player.get("lvl") < zmija.get("lvl"):
			player["hp"] = player["hp"] - random.choice(range(3,8))

 """      

def player_lvl_up(player):
	if imp.get("hp") < 0:
		player["xp"] = player["xp"] + random.choice(range(0, 12))
	if player["xp"] > player["pxp"]:
		player["lvl"] = player["lvl"] + 1
		player["pxp"] = player["pxp"] * 2
		player["dmg"] = player["dmg"] + random.choice(range(1, 4))
		player["hp"] = player["hp"] + 20 + random.choice(range(5, 15))
		##player[""] = player[""]
	

"""
def monster_gen(player,imp,snake,goblin):
	if random.choice(range(1,3)) < 3:
		player.get('lvl') != goblin.get('lvl')
		goblin.get['hp'] = goblin.get['hp'] - random.choice(range(0, 15))
		player.get('lvl') < goblin.get('lvl')
		player['hp'] =  player['hp'] - random.choice(range(3, 8))
	pass
"""
while player['hp'] > 0:
	if player["lvl"] < 2:
		imp_reduceHp(player, imp)
   ##reduceHp(player, imp, goblin, zmija)
   ##random_attm(player,imp,zmija,goblin)
   player_lvl_up(player)
   ##print("{}".format(player["hp"]))    potrebno objasnjenje 
   print("player HP",player['hp'])
   print("Player XP",player["xp"])
   print("Player LVL",player["lvl"])
   print("To next lvl xp",player["pxp"])
   print("Enemy HP",imp['hp'])
   print("Player DMG",player["dmg"])
   print("HP after lvl_up",player["hp"])
   ##print("",player)
   ##print("",player)
   ##print("",player)
   break