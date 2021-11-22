from fastapi import FastAPI
from fastapi.responses import Response, RedirectResponse
from jinja2 import Environment, FileSystemLoader
from urllib.request import urlopen, Request
from src.themes import THEMES
from json import loads
from src.template_data_assembly import assemble
from os import environ
app = FastAPI()
renderer = Environment(loader=FileSystemLoader('templates'))

templates = {
    "project_card": renderer.get_template('project_card.svg'),
}
default_theme = 'dark-blue'

GITHUB_TOKEN = environ.get('GITHUB_TOKEN')


@app.get('/')
async def index():
    """
    Redirects to documentation
    """
    return RedirectResponse('/docs')


@app.get('/themes')
async def themes():
    """
    Returns a list of themes
    """
    return list(THEMES.keys())


@app.get('/templates')
async def template_list():
    """
    Returns a list of templates
    """
    return list(templates.keys())


@app.get("/{template_name}/{user}/{repo}")
async def get_project_card(user: str, repo: str, template_name: str, theme: str = default_theme):
    """
    Get a project card for a given user and repo.
    """
    # Fetch the data from github
    try:
        print(GITHUB_TOKEN)
        req = Request(f"https://api.github.com/repos/{user}/{repo}")
        req.add_header("Authorization",
                       f"token {GITHUB_TOKEN}")
        req.add_header("Cache-Control", "no-cache")
        data = urlopen(req).read()

    except Exception as e:
        return {"error": str(e)}
    data = loads(data)

    # Loads the template
    template = templates.get(template_name, None)
    if not template:
        return {"error": "template not found"}

    # Loads the theme
    theme = THEMES.get(theme, None)
    if not theme:
        return {"error": "theme not found"}

    # Assembles the data for template
    template_data = assemble(template_name, data, theme)
    svg = template.render(template_data)
    return Response(svg, media_type="image/svg+xml")
