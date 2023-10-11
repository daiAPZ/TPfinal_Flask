from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("movies", __name__)


@bp.route("/movies")
def index():
    db = get_db()
    movies = db.execute(
        "SELECT title, description, release_year FROM film ORDER BY title ASC;"
    ).fetchall()
    return render_template("blog/index.html", movies=movies)

    # def get_post(id, check_author=True):
    #    post = (
    #        get_db()
    #        .execute(
    #            "SELECT p.id, title, body, created, author_id, username"
    #            " FROM post p JOIN user u ON p.author_id = u.id"
    #            " WHERE p.id = ?",
    #            (id,),
    #        )
    #        .fetchone()
    #    )


#    if post is None:
#       abort(404, f"Post id {id} doesn't exist.")

#  return post
