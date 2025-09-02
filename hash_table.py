class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [None] * size

	def put(self, key, value):
		index = hash(key) % self.size
		while self.table[index] is not None:
			if self.table[index][0] == key: # Update existing key
				self.table[index] = (key, value)
				return
			index = (index + 1) % self.size # Linear probing
		self.table[index] = (key, value)

	def get(self, key):
		index = hash(key) % self.size
		while self.table[index] is not None:
			if self.table[index][0] == key:
				return self.table[index][1]
			index = (index + 1) % self.size
		return None # Key not found
