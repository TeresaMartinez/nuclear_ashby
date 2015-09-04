import periodictable.core

# Delayed loading of the element xs information

def _load():
	"""
	Cross section data calculated from isotope data
	"""
	from . import core
	core.init(periodictable.core.default_table())

periodictable.core.delayed_load(['xs'], _load, isotope=True, element=True)