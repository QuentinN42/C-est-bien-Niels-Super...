import os

for i in range(100):
	os.system('mkdir '+str(i))
	os.system('> '+str(i)+'/prenom.txt')
	os.system('> '+str(i)+'/notes.txt')
	os.system('> '+str(i)+'/xps.txt')


