from tkinter import *
import random
import time

# Функция для подсчета соседей с окольцовкой
def neighboard(x, y):
	global entries
	res = 0

	# Сама окольцовка
	if y == len(entries[x]) - 1: y = -1
	if x == len(entries) - 1: x = -1

	if entries[x + 1][y] == True:
		res += 1
	if entries[x + 1][y + 1] == True:
		res += 1
	if entries[x + 1][y - 1] == True:
		res += 1
	if entries[x - 1][y] == True:
		res += 1
	if entries[x - 1][y + 1] == True:
		res += 1
	if entries[x - 1][y - 1] == True:
		res += 1
	if entries[x][y + 1] == True:
		res += 1
	if entries[x][y - 1] == True:
		res += 1
	return res

# Функция для выполнения алгоритма
def tick(n, m):
	global entries
	temp = [[False for col in range(m)] for row in range(n)]

	for row in range(n):
		for col in range(m):
			if neighboard(row, col) == 3:
				temp[row][col] = True
			elif entries[row][col] == True and neighboard(row, col) == 2:
				temp[row][col] = True
			else:
				temp[row][col] = False

	entries = temp.copy()
	peacture(n, m)


# Функция отрисовки на окне
def peacture(n, m):
	global entries
	global main
	for row in range(n):
		for col in range(m):
			main[row][col]["bg"] = "#00ff00" if entries[row][col] else "#000000"

	root.after(1, tick, n, m)
#ff7d00
# Размер поля n x m
n = 30
m = 41

# Рандомный массив булевых
#entries = [[False if random.randint(0, 1) == 0 else True for col in range(m)] for row in range(n)]

# Паттерн
entries = [[False for col in range(m)] for row in range(n)]
a = 0
entries[5 + a][1 + a] = True
entries[6 + a][1 + a] = True
entries[5 + a][2 + a] = True
entries[6 + a][2 + a] = True

entries[3 + a][14 + a] = True
entries[3 + a][13 + a] = True
entries[4 + a][12 + a] = True
entries[5 + a][11 + a] = True
entries[6 + a][11 + a] = True
entries[7 + a][11 + a] = True
entries[8 + a][12 + a] = True
entries[9 + a][13 + a] = True
entries[9 + a][14 + a] = True

entries[6 + a][15 + a] = True

entries[4 + a][16 + a] = True
entries[5 + a][17 + a] = True
entries[6 + a][17 + a] = True
entries[7 + a][17 + a] = True
entries[6 + a][18 + a] = True
entries[8 + a][16 + a] = True

entries[3 + a][21 + a] = True
entries[3 + a][22 + a] = True
entries[4 + a][21 + a] = True
entries[4 + a][22 + a] = True
entries[5 + a][21 + a] = True
entries[5 + a][22 + a] = True
entries[2 + a][23 + a] = True
entries[6 + a][23 + a] = True

entries[1 + a][25 + a] = True
entries[2 + a][25 + a] = True


entries[6 + a][25 + a] = True
entries[7 + a][25 + a] = True


entries[3 + a][35 + a] = True
entries[4 + a][35 + a] = True
entries[3 + a][36 + a] = True
entries[4 + a][36 + a] = True

# Создаем окно
root = Tk()
root.resizable(width=False, height=False)
root.title("Жизнь")

# Создаем массив для вывода на экран
main = [[None for col in range(m)] for row in range(n)]
for row in range(n):
	for col in range(m):
		e = Button(width = 2, height = 1, font='Verdana 6')
		e.grid(row = row, column = col)
		main[row][col] = e

# Запускаем
# Для обновления экрана
root.after(1, peacture, n, m)
# Общий цикл
root.mainloop()