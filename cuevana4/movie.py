from flask import (
    Blueprint,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.exceptions import abort

from cuevana4.db import get_db

bp = Blueprint("movie", __name__)


@bp.route("/peliculas")
def index_films():
    db = get_db()
    films = db.execute(
        "SELECT title, description, rating, release_year, film_id"
        " FROM film"
        " ORDER BY title ASC"
    ).fetchall()
    return render_template("movie/peliculas.html", films=films)


@bp.route("/actores")
def index_actor():
    db = get_db()
    actors = db.execute(
        "SELECT first_name, last_name, actor_id"
        " FROM actor"
        " ORDER BY first_name ASC"
    ).fetchall()
    return render_template("movie/actores.html", actors=actors)


@bp.route("/categorias")
def index_category():
    db = get_db()
    categories = db.execute(
        "SELECT name" " FROM category" " ORDER BY name ASC"
    ).fetchall()
    return render_template("movie/categorias.html", categories=categories)


@bp.route("/lenguajes")
def index_languege():
    db = get_db()
    languages = db.execute(
        "SELECT name" " FROM language" " ORDER BY name ASC"
    ).fetchall()
    return render_template("detalles/lenguajes.html", langueges=languages)


@bp.route("/actor/<int:id>/")
def index_un_actor(id):
    db = get_db()
    actor = db.execute(
        """SELECT a.first_name, a.last_name FROM actor a
            WHERE a.actor_id = %s""",
        (id,),
    ).fetchone()

    peliculas = db.execute(
        """SELECT f.title, f.film_id
         FROM film f JOIN film_actor fa ON f.film_id = fa.film_id
         WHERE fa.actor_id = %s""",
        (id,),
    ).fetchall()
    return render_template("detalles/actor.html", actor=actor, peliculas=peliculas)


@bp.route("/pelicula/<int:id>/")
def index_una_pelicula(id):
    db = get_db()
    pelicula = db.execute(
        """SELECT title FROM film f
            WHERE f.film_id = %s """,
        (id,),
    ).fetchone()

    actores = db.execute(
        """SELECT a.first_name, a.last_name, a.actor_id FROM film_actor fa JOIN actor a ON a.actor_id = fa.actor_id  
    WHERE fa.film_id = %s """,
        (id,),
    ).fetchall()
    return render_template("detalles/pelicula.html", pelicula=pelicula, actores=actores)
