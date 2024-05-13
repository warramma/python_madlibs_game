#5/13/2024
#basic madlibs game

print('Let\'s play a game of madlibs!' )

##collecting the victims
noun = input("Enter a noun: ")
statement1 = 'Once upon a time there was a ' + noun

place = input('Enter the name of a city: ')
statement2 = 'They had just moved to ' + place

place = input('Enter a place you might visit in a town: ')
statement3 = 'On their first day there, they decided to go to the ' + place

purchase = input('Enter another noun: ')
verb = input('Enter a verb in past tense: ')
statement4 = 'They had just ' + verb + ' ' + purchase + '.'

adjective = input('Enter an adjective: ')
statement5 = 'They were so ' + adjective

adjective = input('Enter another adjective: ')
statement6 = 'Their new ' + purchase + ' would look so ' + adjective + ' in their new home.'


##result:
print('\n' + statement1)
print(statement2)
print(statement3)
print(statement4)
print(statement5)
print(statement6)