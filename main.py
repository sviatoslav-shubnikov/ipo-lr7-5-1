books = [
	{'title': "Мастер и Маргарита", 'author': "Михаил Булгаков", 'year': 1940},
	{'title': "Мёртвые души", 'author': "Николай Гоголь", 'year': 1842},
	{'title': "Отцы и дети", 'author': "Иван Тургенев", 'year': 1861},
	{'title': "Воскресение", 'author': "Лев Толстой", 'year': 1899},
	{'title': "Тихий Дон", 'author': "Михаил Шолохов", 'year': 1940},
]


while True:

	title = input("Введите название книги: ")
	author = input("Введите автора книги: ")
	year = int(input("Введите год издания книги: "))

	new_book = {
        "title": title,
        "author": author,
        "year": year
    }
	books.append(new_book)

	continues = input("Хотите ли вы продолжить добавлять книги? (+/-): ")

	if continues != '+':
		break


for i in range(len(books)):
    print(f"---------------------- Книга {i + 1} -----------------------")
    print(f"Название: {books[i]['title']}, Автор: {books[i]['author']},")
    print(f"-------------------------{books[i]['year']}-------------------------")