from database import db
from categories import *
from articles import *



def run():
    while True:
        command = input("Buyruqni kiriting: ")
        if command == 'stop':
            break
        elif command == 'add category':
            add_category()
        elif command == 'del category':
            delete_category()
        elif command == 'view categories':
            view_categories()
        elif command == 'update category':
            update_category()
        elif command == 'add article':
            add_articles()
        elif command == 'del article':
            delete_articles()
        elif command == 'view articles':
            view_articles()
        elif command == 'update article':
            update_article()





if __name__ == '__main__':
    db.create_table_categories()
    db.create_table_articles()
    db.create_table_comments()
    run()