class student_types(object):
	"""docstring for student"""
	first_day = []
	def __init__(self, genius, slow, dull):
		self.genius = genius # indicates group of genuis people in class
		self.slow = slow # indicates group of slow learners in class
		self.dull = dull # indicates group of dull and below average students in class

	def newly_joined(self):
		whole_class = []
		import itertools
		self.first_day = [self.genius, self.slow, self.dull] # all students get to sit together in the first day of school and colleges.
		self.whole_class = list(itertools.chain(*self.first_day))
		print
		return self.whole_class

	def after_tests(self):
		import random
		avg_list = []
		self.random_dull = [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57] # results of the dull people after normal tests
		self.random_slow = [58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76] # results of the slow learners after normal tests
		self.random_genius = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98] # results of the genius people after normal tests
		self.genius = sum([random.choice(self.random_genius) for x in self.random_genius]) / len(self.random_genius) # average of the marks of the genius people
		self.slow = sum([random.choice(self.random_slow) for x in self.random_slow]) / len(self.random_slow)# average of the marks of the slow learners
		self.dull = sum([random.choice(self.random_dull) for x in self.random_dull]) / len(self.random_dull) # average of the marks of the dull people
		self.avg_list = [self.genius, self.slow, self.dull] # list of the average marks of the dull people
		self.average_percentage = sum(self.avg_list) / len(self.avg_list) # average of the whole class in terms of marks
		return 'The average performance of the students as per the whole class is ' + str(self.average_percentage) + '. After it is narrowed down, the result is divided as per the overall percentage of the students. \n\tThe average percentage of the students who scored well is ' + str(self.genius) + '. \n\tThe average percentage of the students who scored normal is ' + str(self.slow) + '. \n\tThe average percentage of the students who scored very badly is ' + str(self.dull) + '.'

	def serious_concern(self):
		# after serius concern, the class is grouped, having one genius, one slow and one dull student in each group
		import random
		groups = []
		self.groups = zip([random.choice(self.random_genius) for x in self.random_genius],[random.choice(self.random_slow) for x in self.random_slow],[random.choice(self.random_dull) for x in self.random_dull]) # usage of zip func to group the students based on their performance
		return 'After serious planning and discussions, the class has been grouped as per the grades having one genius, one slow and one dull in each group --->', self.groups

	def final_test(self):
		return 'Serius studies is going on. Students are literally working very effectively in the groups which they are assigned to. I (Head Master) hope this time they will nail the examinations :)'

	def final_result(self):
		import random
		self.rg = [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97] # percentge of the marks of the genius people, the result of the genius people always remains constant in every class
		self.rs = [66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84] # percentge of the marks of the slow learners, the result of the slow learners always remains constant in every class
		self.rd = [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63] # percentge of the marks of the dull people, the result of the dull people always remains constant in every class
		self.result_genius = sum([random.choice(self.rg) for x in self.rg]) / len(self.rg) # takes the random percentages and get the average of the result of the genius people
		self.result_slow = sum([random.choice(self.rs) for x in self.rs]) / len(self.rs) # takes the random percentages and get the average of the result of the slow learners
		self.result_dull = sum([random.choice(self.rg) for x in self.rd]) / len(self.rd) # takes the random percentages and get the average of the result of the dull people
		self.result_final = [self.result_slow,self.result_genius,self.result_dull]
		self.result_avg = sum(self.result_final) / len(self.result_final) # gets the overall average percentage of the class after serious practise and studies
		return 'The average result of the overall class for the final exam is ' + str(self.result_avg)

	def conclusion(self):
		return 'Finally the Head Master of the Institution feels happy seeing the result and dedication of students in studies aspect.'

'''pupil = student_types(['genius'],['slow'],['dull'])
print(pupil.newly_joined())
print(pupil.after_tests())
print(pupil.serious_concern())
print(pupil.final_test())
print(pupil.final_result())
print(pupil.conclusion())
print'''

class g_s_d(student_types):
	def student_development(self): # takes all the functions in a list and prints the outcomes
		for result in [student_types.newly_joined(self), student_types.after_tests(self), student_types.serious_concern(self), student_types.final_test(self), student_types.final_result(self), student_types.conclusion(self)]:
			print
			print result


# different class groups

cms = g_s_d(['dull'],['genius'],['slow'])
print(cms.student_development())
print(cms)

cme = g_s_d(['genius'],['slow'],['dull'])
print(cme.student_development())
print(cme)

hep = g_s_d(['slow'],['dull'],['genius'])
print(hep.student_development())
print(hep)

pme = g_s_d(['slow'],['genius'],['dull'])
print(pme.student_development())
print(pme)

pcm = g_s_d(['genius'],['dull'],['slow'])
print(pcm.student_development())
print(pcm)

ems = g_s_d(['genius'],['slow'],['dull'])
print(ems.student_development())
print(ems)

ecm = g_s_d(['dull'],['slow'],['genius'])
print(ecm.student_development())
print(ecm)
