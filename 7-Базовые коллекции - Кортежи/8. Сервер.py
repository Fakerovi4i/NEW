server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for item, data in server_data.items():
	print("{0}:".format(item))
	for j_item, j_data in data.items():
		print("  {0}: {1}".format(j_item, j_data))