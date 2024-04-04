from flask import Blueprint, render_template, url_for

pages = Blueprint('pages', __name__)

@pages.route('/<http_code>')
def root(http_code):
    return render_template('base.html', 
                            title='test', 
                            level = '4',
                            code = '2',
                            header_two='test header', 
                            paragraph='test paragraph')