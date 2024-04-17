'''
Volem fer un petit programa per guardar la informació dels diferents llibres que té una biblioteca.

A un fitxer s'ha de dir  books.out

Per introduir els llibres, primer es llegirà els llibres per teclat (en concret: títol, autor, nombre de pàgines).  El primer nombre indica la quantitat de llibres que es vol introduir. En versions futures la lectura dels llibres  es farà d'un fitxer.

Quan acabi volem que mostri la llista de llibres i el número total, el llibre més curt i el llibre més llarg (en cas d'empat el primer que s'hagi llegit del fitxer).

3

Lorem

Ot Pi

56

Ipsum

Mar Om

77

Dolor

Lin Om

42

'''

def books():
    try:
        # crear un fitxer amb els llibres
        with open('books.out', mode='wt', encoding='utf-8') as file:
            # demanar la quantitat de llibres que es vol introduir
            num_books = int(input("Introdueix la quantitat de llibres que vols introduir: "))
            # introduir els llibres
            for _ in range(num_books):
                title = input("Introdueix el títol del llibre: ")
                author = input("Introdueix l'autor del llibre: ")
                pages = input("Introdueix el nombre de pàgines del llibre: ")
                file.write(f"{title} {author} {pages}\n")
        # llegir el fitxer
        with open('books.out', mode='rt', encoding='utf-8') as file:
            books = file.readlines()
            books = [book.split() for book in books]
            print("--------------------")
            print("Llista de llibres:")
            for book in books:
                print(f"{book[0]} - {book[1]} - {book[2]} pàgines")
            print("--------------------")
            print(f"Total de llibres: {len(books)}")

            # llibre més curt
            min_pages = min([int(book[2]) for book in books])
            min_book = [book for book in books if int(book[2]) == min_pages][0]
            print(f"Llibre més curt: {min_book[0]} - {min_book[1]} - {min_book[2]} pàgines")
            # llibre més llarg
            max_pages = max([int(book[2]) for book in books])
            max_book = [book for book in books if int(book[2]) == max_pages][0]
            print(f"Llibre més llarg: {max_book[0]} - {max_book[1]} - {max_book[2]} pàgines")
            print("--------------------")

            # lo que sale en la consola ponerlo en un fichero
            with open('books.out', mode='wt', encoding='utf-8') as file:
                file.write("--------------------\n")
                file.write("Llista de llibres:\n")
                for book in books:
                    file.write(f"{book[0]} - {book[1]} - {book[2]} pàgines\n")
                file.write("--------------------\n")
                file.write(f"Total de llibres: {len(books)}\n")
                file.write(f"Llibre més curt: {min_book[0]} - {min_book[1]} - {min_book[2]} pàgines\n")
                file.write(f"Llibre més llarg: {max_book[0]} - {max_book[1]} - {max_book[2]} pàgines\n")
                file.write("--------------------\n")

    except FileNotFoundError:
        print("El fitxer no existeix.")

    except ValueError:
        print("El nombre de pàgines ha de ser un número enter.")
books()
