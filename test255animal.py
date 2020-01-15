# Inheritance Example Using Super()
#Error -> ctrl + shift + p: indentation  -> convdert indentation to tab: 
class Animal:
	def make_sound(self, sound):
		print(f"this animal says {sound}")

	cool = True

class Cat(Animal):
	pass


gandalf = Cat()
gandalf.make_sound("Meow")
gandalf.cool

