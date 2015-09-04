import periodictable.core

# Delayed loading of the element melting point information

def _load():
	"""
	Melting point data (Celsius)
	"""
	from . import core
	core.init(periodictable.core.default_table())

periodictable.core.delayed_load(['melting_point'], _load)