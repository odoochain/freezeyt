from flask import Flask, url_for, abort, render_template
from mistune import markdown
from pathlib import Path

app = Flask(__name__)

base_path = Path(__file__).parent
content_path = base_path / 'content/'

ARTICLES_PATH = content_path / 'articles/'
STATIC_PATH = content_path / 'images/'

@app.route('/')
def index():
    """Start page with list of articles."""
    post_names = [art_file.stem for art_file in ARTICLES_PATH.iterdir()]

    return render_template(
        'index.html',
        post_names=post_names,
    )


@app.route('/<slug>')
def post(slug):
    article = ARTICLES_PATH / f'{slug}.md'
    try:
        file = open(article, mode='r', encoding='UTF-8')
    except FileNotFoundError:
        return abort(404)

    with file:
        md_content = file.read()

    html_content = markdown(md_content)

    return html_content





