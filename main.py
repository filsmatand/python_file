from flask import Flask

from flask import Flask, request, render_template


app = Flask(__name__)

app.config.update(

    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Seigneur1@localhost/catalog',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


# using jinja template in html
@app.route('/films')
def films():
    films_dict = {
        'BLACK PANTHER': 2.5,
        'Avengers: Infinity War': 3.2,
        'Ready Player One': 2.14,
        'Les Indestructibles 2': 1.48,
        'Woman at War': 2.52,
        'The Guilty': 1.5,
        'Deadpool 2': 3.5,
        'Mission Impossible - Fallout': 1.7
    }
    return render_template('table_movies.html', films=films_dict, name='Sorelle')


@app.route('/macros')
def films_macros():
    films_dict = {
        'BLACK PANTHER': 2.5,
        'Avengers: Infinity War': 3.2,
        'Ready Player One': 2.14,
        'Les Indestructibles 2': 1.48,
        'Woman at War': 2.52,
        'The Guilty': 1.5,
        'Deadpool 2': 3.5,
        'Mission Impossible - Fallout': 1.7
    }
    return render_template('using_macros.html', films=films_dict)



    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ' Publisher  is {}'.format(self.name)



    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return 'title of book is {} by {}'.format(self.title, self.author)


if __name__ == '__main__':
    app.run(debug=True)






