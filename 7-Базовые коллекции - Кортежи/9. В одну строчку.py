print([data
	   for i_key, data in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items()
	   if i_key % 2 == 0])