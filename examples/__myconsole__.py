import inttable

inttable.core.activate("dev")

class MyConsole:
	def run():
		inttable.console.run("hello")
console = MyConsole
console.run()