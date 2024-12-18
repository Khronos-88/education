import sqlite3
from flask import Flask, render_template_string

app = Flask(__name__)

DB_PATH = 'gifts.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS gifts')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gift_title TEXT NOT NULL,
            cost REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM gifts')
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany('''

            INSERT INTO gifts (name, gift_title, cost, status)
            VALUES (?, ?, ?, ?)
        ''', [
            ("Иванов Иван", "Книга", 500, "куплен"),
            ("Петров Петр", "Носки", 200, "некуплен"),
            ("Сидоров Сидор", "Чайный набор", 1500, "куплен"),
            ("Смирнова Анна", "Парфюм", 3000, "некуплен"),
            ("Кузнецова Ольга", "Флешка", 800, "куплен"),
            ("Попов Алексей", "Блокнот", 450, "некуплен"),
            ("Князева Мария", "Ручка", 150, "куплен"),
            ("Иванова Дарья", "Часы", 2500, "некуплен"),
            ("Смирнов Олег", "Подарочная карта", 1000, "куплен"),
            ("Сухов Роман", "Календарь", 500, "некуплен"),
            ("Колпаков Александр", "Кружка", 300, "куплен"),
            ("Романцова Анна", "Книга", 500, "некуплен"),
            ("Петрова Светлана", "Кружка", 300, "некуплен"),
            ("Зайцева Анна", "Плед", 1200, "куплен"),
            ("Попов Сергей", "Набор инструментов", 3000, "некуплен"),
        ])

    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('../gifts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM gifts')
    rows = cursor.fetchall()
    conn.close()


    html = '''
    <h1>Список подарков</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>ФИО</th>
            <th>Название подарка</th>
            <th>Стоимость</th>
            <th>Статус</th>
        </tr>
    '''
    for row in rows:
        html += f'''
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
            <td>{row[4]}</td>
        </tr>
        '''
    html += '</table>'
    return render_template_string(html)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
