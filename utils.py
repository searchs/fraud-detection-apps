import re

class Utils():
	"""Helper class for mostly used functionalities """
	
	COMMA_DELIMITER = re.compile(''', (?=(?:[^"]*"[^"]*")*[^"]*$)''')
