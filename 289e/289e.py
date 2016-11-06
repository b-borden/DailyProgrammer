# Including bonus 1

import re
import requests
import operator
from functools import reduce

from httpcache import CachingHTTPAdapter

# Let's be nice to pokeapi and cache our requests
s = requests.Session()
s.mount('http://', CachingHTTPAdapter())


def dmg_mult(attack):
	atk_types, def_types = (types.split() for types in re.split('\s*->\s*', attack))

	dmg = [1.0]
	for attack_type in atk_types:
		atk_info = s.get('http://pokeapi.co/api/v2/type/' + attack_type + '/').json()['damage_relations']
		atk_info = {effect_desc: [_type['name'] for _type in types] for effect_desc, types in atk_info.copy().items()}

		dmg.extend([0.0 for def_type in def_types if def_type in atk_info['no_damage_to']])
		dmg.extend([0.5 for def_type in def_types if def_type in atk_info['half_damage_to']])
		dmg.extend([2.0 for def_type in def_types if def_type in atk_info['double_damage_to']])

	return reduce(operator.mul, dmg)


atks = '''fire -> grass
 fighting -> ice rock
 psychic -> poison dark
 water -> normal
 fire -> rock'''

for atk in atks.splitlines():
	print('%.gx' % dmg_mult(atk))
