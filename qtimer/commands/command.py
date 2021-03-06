class Command:

	'''
	Required. A unique string key which allows the program to determine which
	command it should run. Two commands with the same identifier is unsupported.
	'''
	# COMMAND_IDENTIFIER = 'foo'

	''' Set an optional help message for this command. '''
	# COMMAND_HELP = 'some help string'

	def runCommand(self, args, program):
		'''
		Required. Perform the business logic associated with this command. You are
		given the args you added to the parser in addArguments as well as the
		program to run database commands, and access global data
		'''
		raise RuntimeError('You must implement this method')

	def addArguments(self, parser):
		'''
		Optional. Add all required args for this command.
		'''
		pass
