import os

# hash for abcd

for i in range(100):
	os.system('> eleve' + str(i) + '.txt')
	f = open('eleve'+str(i)+'.txt','w')
	f.write("88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589")
	f.close()
