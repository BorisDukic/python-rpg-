import random

#character
player = {"name":"Elfonja","xp": 0,"lvl":1,"dmg": 2,"hp":20,"pxp":5}

#monsters
imp = {"name":"Ruzni","lvl": 3,"dmg": 1,"hp": 5}
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

def player_lvl_up(player):
    if player.get("pxp") < player.get("xp"):
        player["xp"] = player["xp"] + random.choice(range(0, 12))
    if player["xp"] > player["pxp"]:
        player["lvl"] = player["lvl"] + 1
        player["pxp"] = player["pxp"] * 2
        player["dmg"] = player["dmg"] + random.choice(range(1, 4))
        player["hp"] = player["hp"] + 20 + random.choice(range(5, 15))



while player['hp'] > 0:
    if player["hp"] < 0:
        break
    if player["lvl"] < 2:
        while imp["hp"] > 0:
            print("Player VS Imp")
            imp_reduceHp(player, imp)
            player_lvl_up(player)
    if player["lvl"] == 2:
        while goblin["hp"] > 0:
            print("Player VS Goblin")
            goblin_reduceHp(player, goblin)
            player_lvl_up(player)
    if player["lvl"] > 2:
        while zmija["hp"] > 0:
            print("Player VS Zmija")
            zmija_reduceHp(player, zmija)
            player_lvl_up(player)

    print("player HP",player['hp'])
    print("Player XP",player["xp"])
    print("Player LVL",player["lvl"])
    print("To next lvl xp",player["pxp"])
    print("Enemy HP",imp['hp'])
    print("Player DMG",player["dmg"])
    print("HP after lvl_up",player["hp"])
    