import json
dump_file=input("Enter path of dump file: ")
json_file=dump_file
with open(dump_file) as json.file:
	data = json.load(json_file)
	print("Type:", type(data))
	print("\nBlock: ", data['blocks'])
		
		
	
	

	
