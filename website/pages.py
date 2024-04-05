from flask import Blueprint, render_template, url_for
import yaml

pages = Blueprint('pages', __name__)

DATA_FILE = 'website/data.yaml'

with open(DATA_FILE, 'r') as f:
    datas = yaml.safe_load(f)


@pages.route('/<http_code>')
def root(http_code):
    
    error_page = next((item for item in datas if item['code'] == http_code), None)
    
    if error_page is None:
        return render_template('base.html', 
                                title='test', 
                                level='4',
                                code='4',
                                header_two='test', 
                                paragraph='test')
        
    return render_template('base.html', 
                            title=error_page['title'], 
                            level=error_page['code'][0],
                            code=error_page['code'][-1],
                            header_two=error_page['h2'], 
                            paragraph=error_page['paragraph'])