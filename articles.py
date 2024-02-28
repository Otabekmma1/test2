from database import db
from categories import *
from colour import *

def add_articles():
    title = input("Sarlavhani kiriting: ")
    content = input('Matnni kiriting: ')
    view_categories()
    category_id = input('Kategoriya id ni kiriting: ')
    db.insert_articles(title, content, category_id)
    print(blue("Maqola qo'shildi."))
    yes_no = input("Yana maqola qo'shasizmi?: ha/yoq: ")
    if yes_no == 'ha':
        add_articles()

def view_articles():
    art = db.view_articles_by_id()
    print(blue('=')*125)
    print('|', "ID".center(5, ' '), '|', "KATEGORIYA".center(20, ' '), '|', "SARLAVHA".center(90, ' '), '|')
    print(blue('=')*125)
    for i in art:
        print('|', str(i[0]).center(5, ' '), '|', i[4].center(20, ' '), '|', i[1].center(90, ' '), '|')
    print('-'*125)
    article_id = input(yellow("Maqola id sini kiriting: "))
    maqola = db.select_article(article_id)
    for a in maqola:
        print(black(a[0], shrift=True).center(15, ' '))
        print(a[1])
        # print('|', i[2].center(100, ' '), '|')
        # print('|', str(i[3]).center(50, ' '), '|')


def delete_articles():
    view_articles()
    article_id = int(input('Maqola id sini kiriting: '))
    db.delete_articles(article_id)
    yes_no = input("Yana maqola o'chirasizmi?: ha/yoq: ")
    if yes_no == 'ha':
        delete_articles()

def update_article():
    view_articles()
    title_or_content = input(f"Nimani o'zgartirmoqchisiz?\ntitle/content/category_id: ")
    if title_or_content == 'title':
        article_id = int(input('Maqola id sini kiriting: '))
        title = input('Yangi sarlavhani kiriting: ')
        db.update_articles_title(title, article_id)
        yes_no = input("Yana maqola o'zgartirasizmi?: ha/yoq: ")
        if yes_no == 'ha':
            update_article()

    if title_or_content == 'content':
        article_id = int(input('Maqola id sini kiriting: '))
        content = input('Yangi matnni kiriting: ')
        db.update_articles_content(content, article_id)
        yes_no = input("Yana maqola o'zgartirasizmi?: ha/yoq: ")
        if yes_no == 'ha':
            update_article()

    if title_or_content == 'category_id':
        article_id = int(input('Maqola id sini kiriting: '))
        category_id = int(input('Yangi kategoriya id sini kiriting: '))
        db.update_articles_category(category_id, article_id)
        yes_no = input("Yana maqola o'zgartirasizmi?: ha/yoq: ")
        if yes_no == 'ha':
            update_article()
