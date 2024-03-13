# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна
# (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
from flask import Flask
from flask import render_template

app = Flask(__name__)
context = {
    'data': {'Одежда': ['Куртка', 'Брюки'], "Обувь": ['Ботинки']},
}


@app.route('/')
def index():
    context_b = {
        'title': 'Интернет Магазин: Интербот',
        'content_main': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eligendi maiores at quisquam asperiores, cum deleniti assumenda consequuntur excepturi aut laudantium amet consequatur? Neque atque dignissimos, nobis quam consequuntur enim saepe.',
        
    }
    return render_template('index.html', **context_b)


@app.route('/Catalog')
def catalog():
    context['title'] = 'Каталог'
    return render_template('catalog.html', **context)


@app.route('/Catalog/<category>')
def cat(category):
    if category in context['data'].keys():
        context['title'] = category
        return render_template('category.html', **context)
    else:
        context['title'] = 'Ошибка'
        return render_template('error.html', **context)


@app.route('/Catalog/<category>/<product>')
def prod(category, product):
    if category in context['data'].keys() and product in context['data'][category]:
        context['title'] = product
        context['category'] = category
        context['product'] = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea iure deleniti quibusdam aut itaque velit."
        return render_template('product.html', **context)
    return cat(category)


@app.route('/Contact')
def contact():
    context_c = {
        'title': 'Контакты',
        'data': {'email': 'sendme@email.ru', 'tel': '+123-456-789'},
    }
    return render_template('contact.html', **context_c)


if __name__ == '__main__':
    app.run(debug=True)