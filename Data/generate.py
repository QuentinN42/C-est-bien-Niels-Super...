import os

for i in range(100):
	os.system('mkdir '+str(i))
	os.system('> '+str(i)+'/prenom.txt')


