from flask import Flask, render_template

# Создаём приложение Flask
app = Flask(__name__)

# Определяем главную страницу сайта (/)
@app.route('/')
def index():
    # Эта функция берёт файл index.html и показывает его
    return render_template('index.html')

# Если этот файл запущен напрямую, запускаем сервер
if __name__ == '__main__':
    # Включаем режим отладки, чтобы видеть ошибки
    app.run(debug=True)