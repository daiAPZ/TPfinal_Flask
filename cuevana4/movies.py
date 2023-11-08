from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from cuevana4.db import get_db

bp = Blueprint("movies", __name__)


@bp.route("/pelicula")
def index_films():
    db = get_db()
    films = db.execute(
        "SELECT title, description, rating, release_year, film_id"
        " FROM film"
        " ORDER BY title ASC"
    ).fetchall()
    return render_template("movies/pelicula.html", films=films)


@bp.route("/actor")
def index_actor():
    db = get_db()
    actors = db.execute(
        "SELECT first_name, last_name, actor_id"
        " FROM actor"
        " ORDER BY first_name ASC"
    ).fetchall()
    return render_template("movies/actor.html", actors=actors)


@bp.route("/categoria")
def index_category():
    db = get_db()
    categories = db.execute(
        "SELECT name" " FROM category" " ORDER BY name ASC"
    ).fetchall()
    return render_template("movies/categoria.html", categories=categories)


@bp.route("/lenguaje")
def index_languege():
    db = get_db()
    languages = db.execute(
        "SELECT name" " FROM language" " ORDER BY name ASC"
    ).fetchall()
    return render_template("movies/lenguaje.html", langueges=languages)
