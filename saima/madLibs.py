print ("Please provide the following words:")

name = input("Family name: ")
number = input("Number in word-form: ")
street = input("Street name only: ")
positiveAdj = input("Positive adjective: ")
noun = input("Noun: ")
adjective1 = input("Adjective: ")
adjective2 = input("Another adjective: ")

print ("""Harry Potter and the Sorcerer's Stone
The Boy Who Lived
Mr. and Mrs.%s, of %s, %s Drive, were proud to say that they were perfectly %s, thank you very much. They were the last %s you'd expect to be involved in anything %s or %s, because they just didn't hold with such nonsense.""" %(name, number, street, positiveAdj, noun, adjective1, adjective2))
