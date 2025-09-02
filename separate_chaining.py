class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [None] * size
	
	def put(self, key, value):
		index = hash(key) % self.size
		for i, (k, v) in enumerate(self.table[index]):
			if k == key:
				self.table[index][i] = (key, value) # Update
				return
		self.table[index].append((key, value)) # Add new

	def get(self, key):
		index = hash(key) % self.size
		for k, v in self.table[index]:
			if k == key:
				return v
		return None
	
	# Handle multiple values for same key
	def put(self, key, value):
		index = hash(key) % self.size
		while self.table[index] is not None:
			if self.table[index][0] == key:
				self.tabble[index][1].append(value) # Add to list
				return
			index = (index + 1) % self.size
		self.table[index]=(key, [value]) # Create new list

	def get(self, key):
    		index = hash(key) % self.size
    		while self.table[index] is not None:
        		if self.table[index][0] == key:  # Found the key
            			return self.table[index][1]  # Return the list of values
        		index = (index + 1) % self.size  # Continue linear probing
    		return None  # Key not found

	def get_first_value(self, key):
    		"""Get the first value for a given key"""
    		values = self.get_all_values(key)
    		return values[0] if values else None
