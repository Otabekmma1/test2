from database import db
from colour import *
def add_category():
    category = input("Kategoriyani kiriting: ")
    db.insert_category(category)
    print(blue("Kategoriya qo'shildi."))
    yes_no = input("Yana kategoriya qo'shasizmi?: ha/yoq: ")
    if yes_no == 'ha':
        add_category()


def view_categories():
    categories = db.view_all_categories()
    for category in categories:
        category_id, category_name = category
        print('|', str(category_id).center(5, ' '), '|', category_name.center(50, ' '), '|')


def delete_category():
    view_categories()
    category_id = int(input("Kategoriya id sini kiriting: "))
    db.delete_category_by_id(category_id)
    yes_no = input("Yana kategoriya o'chirasizmi?: ha/yoq: ")
    if yes_no == 'ha':
        delete_category()


def update_category():
    view_categories()
    category_id = int(input("Kategoriya id sini kiriting: "))
    category_name = input("Kategoriyaning yangi nomini kiriting: ")
    db.update_category_by_id(category_name, category_id)
    yes_no = input("Yana kategoriyani o'zgartirasizmi?: ha/yoq: ")
    if yes_no == 'ha':
        update_category()

