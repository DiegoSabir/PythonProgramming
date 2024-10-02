from flask import Blueprint

bp = Blueprint('post', __name__, url_prefix = '/post')

@bp.route('/posts')
def register():
    return ' Pagina de posts'

@bp.route('/create')
def create():
    return 'Pagina de create'

@bp.route('/update')
def update():
    return 'Pagina de update'

