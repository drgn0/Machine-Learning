import random 


class TextFinder:
	def initialise(self, TARGET_TEXT, POPULATION, MUTATION):
		def random_element():
			# array of intergers (which represents characters) 
			return [self.random_char() for i in range(len(TARGET_TEXT))]

		self.POPULATION = POPULATION
		self.MUTATION_CHANCES = MUTATION

		self.TARGET_TEXT = tuple(map(ord, TARGET_TEXT)) 
	
		self.generation_no = 0 
		self.elements = [random_element() for i in range(POPULATION)]
		self.scores = self.find_scores() 
	
	def random_char(self):
		if random.randrange(0, 53) == 0:
			return ord(' ') 
		n = ord('a') if random.randrange(0, 2) else ord('A') 
		return n + random.randrange(0, 26)
	
	def score(self, element):
		return sum(x == y for x, y in zip(element, self.TARGET_TEXT)) 
	
	def find_scores(self):
		return tuple(map(self.score, self.elements)) 

	def convert_string(self, elem):
		return ''.join(map(chr, elem)) 
	
	def best_element(self):
		# element with largest value of score.
		# assuming self.scores is updated
		return self.elements[max(range(len(self.elements)), key = self.scores.__getitem__)]
		return max(zip(self.elements, self.scores), key = lambda item: item[1])[0] 

	def mutate(self, elem):
		elem[random.randrange(0, len(elem))] = self.random_char() 
	
	def reproduce(self, elem1, elem2):
		new_elem = [x if random.randrange(0, 2) else y for x, y in zip(elem1, elem2)] 

		if random.random() < self.MUTATION_CHANCES:
			self.mutate(new_elem)  
		
		return new_elem		

	def find_next_generation(self): 
		# assuming self.scores is updated 
		return [
			self.reproduce(*random.choices(self.elements, weights=self.scores, k=2))
			for i in range(self.POPULATION) 
		]
	
	def update_generation(self):
		self.scores = self.find_scores() 
		self.elements = self.find_next_generation() 
		self.generation_no += 1 

	def start(self):
		while any(x != y for x, y in zip(self.best_element(), self.TARGET_TEXT)):
			self.update_generation() 

			if self.generation_no % 50 == 0:
				print(self.convert_string(self.best_element()))
		
if __name__ == '__main__':
	text_finder = TextFinder() 

	target_text = "Lets see if it can be found" 

	text_finder.initialise(target_text, 250, 0.2) 
	text_finder.start() 
	print(f"Sucess in {text_finder.generation_no} generations")  
