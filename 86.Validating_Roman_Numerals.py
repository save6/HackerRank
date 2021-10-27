#regex_pattern = r"^(I|II|III|IV|V|VI|VII|VIII|IX|X|L|C|D|M)+$"	# Do not delete 'r'.
regex_pattern = r"M{0,3}(C{0,3}|CD|DC{0,3}|CM)(X{0,3}|XL|LX{0,3}|XC)(I{0,3}|IV|VI{0,3}|IX)$"

import re
print(str(bool(re.match(regex_pattern, input()))))