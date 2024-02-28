import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='kun_uz',
            user='postgres',
            password='Instagram',
            host='localhost'
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                fetchmany: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result

    def create_table_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER GENERATED ALWAYS AS IDENTITY PRiMARY KEY,
            category_name VARCHAR(50) UNIQUE NOT NULL
        )'''
        self.manager(sql, commit=True)

    def drop_table_categories(self):
        sql = '''DROP table categories'''
        self.manager(sql, commit=True)

    def insert_category(self, category):
        sql = '''INSERT INTO categories(category_name) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, (category,), commit=True)

    def delete_category_by_id(self, category_id):
        sql = '''DELETE FROM categories WHERE category_id = %s'''
        self.manager(sql, (category_id,), commit=True)

    def update_category_by_id(self,category_name, category_id):
        sql = '''UPDATE categories SET category_name = %s WHERE category_id = %s'''
        self.manager(sql, category_name, category_id, commit=True)

    def view_all_categories(self):
        sql = '''SELECT * FROM categories'''
        return self.manager(sql, fetchall=True)

    def create_table_articles(self):
        sql = '''CREATE TABLE IF NOT EXISTS articles(
            article_id INTEGER GENERATED ALWAYS AS IDENTITY PRiMARY KEY,
            title VARCHAR(250),
            content TEXT,
            created TIMESTAMP DEFAULT NOW(),
            category_id INTEGER,
            foreign key (category_id) references categories(category_id)

        )'''
        self.manager(sql, commit=True)

    def drop_table_articles(self):
        sql = '''DROP TABLE IF EXISTS articles'''
        self.manager(sql, commit=True)

    def insert_articles(self, title, content, category_id):
        sql = '''INSERT INTO articles(title, content, category_id) VALUES(%s, %s, %s) ON CONFLICT DO NOTHING'''
        self.manager(sql, title, content, category_id, commit=True)

    def delete_articles(self, article_id):
        sql = '''DELETE FROM articles WHERE article_id = %s'''
        self.manager(sql, (article_id,), commit=True)

    def update_articles_title(self, title, article_id):
        sql = '''UPDATE articles SET title = %s WHERE article_id = %s'''
        self.manager(sql, title, article_id, commit=True)

    def update_articles_content(self, content, article_id):
        sql = '''UPDATE articles SET content = %s WHERE article_id = %s'''
        self.manager(sql, content, article_id, commit=True)

    def update_articles_category(self, category_id, article_id):
        sql = '''UPDATE articles SET category_id = %s WHERE article_id = %s'''
        self.manager(sql, category_id, article_id, commit=True)

    def select_article(self, article_id):
        sql = '''SELECT title, content FROM articles WHERE article_id = %s'''
        return self.manager(sql, article_id, fetchall=True)

    def view_articles_by_id(self):
        sql = '''SELECT article_id, title, content, created, category_name FROM articles
        JOIN categories ON categories.category_id = articles.category_id
        ORDER BY article_id'''
        return self.manager(sql, fetchall=True)

    def create_table_comments(self):
        sql ='''CREATE TABLE IF NOT EXISTS comments(
            comment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            comment VARCHAR(200),
            article_id INTEGER,
            FOREIGN KEY (article_id) REFERENCES articles(article_id)
        )'''
        self.manager(sql, commit=True)

    def insert_comment(self):
        sql = '''INSERT INTO comments(comment, article_id) VALUES (%s, %s)'''
        self.manager(sql, comment, article_id, commit=True)

    def delete_comment_by_id(self, comment_id):
        sql = '''DELETE FROM comments WHERE comment_id = %s'''
        self.manager(sql, (comment_id,), commit=True)

    def view_comments(self):
        sql = '''SELECT comment_id, comment FROM comments'''
        return self.manager(sql, fetchall=True)


db = DataBase()