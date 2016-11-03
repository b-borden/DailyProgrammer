import re
import requests
from httpcache import CachingHTTPAdapter

# Let's be nice to pokeapi and cache our requests
s = requests.Session()
s.mount('http://', CachingHTTPAdapter())

def dmg_mult(attack):
	move_type, def_type = re.split('\s*->\s*', attack)

	attack_dmg_info = s.get('http://pokeapi.co/api/v2/type/' + move_type + '/').json()['damage_relations']
	def_dmg_info = s.get('http://pokeapi.co/api/v2/type/' + def_type + '/').json()['damage_relations']
	return attack_dmg_info, def_dmg_info


print(dmg_mult('grass -> grass'))
