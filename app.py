from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>

    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>   

        <main>
            <ol>
                <li>
                    <a href="/lab1">Лабораторнгая работа 1</a>
                </li>
            </ol?
        </main>

    <footer>
            &copy; Бодрых Александр Юрьевич, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>

"""

@app.route("/lab1")
def lab1():
    return """

<!doctype html>
<html>
    <head>
        <title>Бодрых Александр Юрьевич, лабораторная 1</title>
    </head>

    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>   

        <h1> web-сервер на flask</h1>

        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов

            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </div>

       

        <footer>
            &copy; Бодрых Александр, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""