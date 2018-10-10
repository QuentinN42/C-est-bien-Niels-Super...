import csv
data = list(csv.reader(open('./donnee.txt', 'r')))

entete = data.pop(0)
entete = [int(float(entete[i])) for i in range(len(entete)-1)] + [entete[len(entete)-1]]

data = [list(map(lambda x: int(float(x)),d)) for d in data]
xp = [[i] + data[i][:-1] for i in range(len(data))]


if __name__ == "__main__":
    print(entete)
    print(xp)
