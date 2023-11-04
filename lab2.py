from flask import Blueprint, render_template
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/example')
def example():
    name, nl, gr, nk = 'Бодрых Александр', '2', 'ФБИ-14', '3' 
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 140},
        {'name': 'апельсины', 'price': 170},
        {'name': 'мандарины', 'price': 195},
        {'name': 'манго', 'price': 235}
    ]

    book = [
        {'Author': 'Роберт Грин', 'name': '48 законов власти', 'style': 'Деловая литература', 'str': '637 страниц'},
        {'Author': 'Джордж Оруэлл', 'name': '1984', 'style': 'Фантастика', 'str': '352 страницы'},
        {'Author': 'Джоан Роулинг', 'name': 'Гарри Поттер и философский камень', 'style': 'Фэнтези', 'str': '320 страниц'},
        {'Author': 'Габриэль Гарсиа Маркес', 'name': 'Сто лет одиночества', 'style': 'Магический реализм', 'str': '432 страницы'},
        {'Author': 'Филип К. Дик', 'name': 'Мечтают ли андроиды об электроовцах?', 'style': 'Научная фантастика', 'str': '256 страниц'},
        {'Author': 'Джейн Остин', 'name': 'Гордость и предубеждение', 'style': 'Классическая литература', 'str': '416 страниц'},
        {'Author': 'Артур Конан Дойл', 'name': 'Приключения Шерлока Холмса', 'style': 'Детектив', 'str': '576 страниц'},
        {'Author': 'Агата Кристи', 'name': 'Десять негритят', 'style': 'Детектив', 'str': '256 страниц'},
        {'Author': 'Эрнест Хемингуэй', 'name': 'Старик и море', 'style': 'Современная классика', 'str': '128 страниц'},
        {'Author': 'Маргарет Этвуд', 'name': 'Рассказ служанки', 'style': 'Научная фантастика', 'str': '320 страниц'}
    ]
    return render_template('example.html', nl=nl, name=name, gr=gr, nk=nk, fruits=fruits, book=book)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/weapon')
def weapon():
    return render_template ('weapon.html')