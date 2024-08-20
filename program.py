class Language:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def message(self):
        print("My name es " + self.name)

languages = [Language("Python"), Language("Javascript")]

for language in languages:
    language.message()
    