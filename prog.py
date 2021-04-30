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
			main[row][col]["bg"] = "#ff7d00" if entries[row][col] else "#ffffff"

	root.after(1, tick, n, m)

# Размер поля n x m
n = 30
m = 60

# Массив булевых
entries = [[False if random.randint(0, 1) == 0 else True for col in range(m)] for row in range(n)]

# Создаем окно
root = Tk()
root.resizable(width=False, height=False)
root.title("Жизнь")

# Создаем массив для вывода на экран
main = [[None for col in range(m)] for row in range(n)]
for row in range(n):
	for col in range(m):
		e = Button(width = 2, height = 1)
		e.grid(row = row, column = col)
		main[row][col] = e

# Запускаем
# Для обновления экрана
root.after(1, peacture, n, m)
# Общий цикл
root.mainloop()