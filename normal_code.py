import click
import requests
import json
from pygments import highlight, lexers, formatters


def colorize(formatted_json):
    return highlight(
        formatted_json.encode("UTF-8"),
        lexers.JsonLexer(),
        formatters.TerminalFormatter(),
    )


def print_output(resp, kwargs):
    data = resp.json()
    table = [
        {
            "name": result["authors"][0]["name"],
            "bookshelves": result["bookshelves"],
            "copyright": result["copyright"],
            "download_count": result["download_count"],
            "title": result["title"],
            "media_type": result["media_type"],
            "xml": result["formats"]["application/rdf+xml"],
        }
        for result in data["results"]
    ]
    if kwargs.get('format', '') == 'json':
        indent = kwargs.get("indent", 4)
        formatted_json = json.dumps(table, sort_keys=True, indent=indent)
        if kwargs.get('colorize'):
            print(colorize(formatted_json))
        else:
            print(formatted_json)
    # TODO: Add YAML Format
    # TODO: Add Tabular Format


class Search:
    def __init__(self, term, kwargs):
        self.term = term
        self.kwargs = kwargs

    def make_request(self):
        resp = requests.get(f"http://gutendex.com/books/?search={self.term}")
        return resp

    def run(self):
        resp = self.make_request()
        print_output(resp, self.kwargs)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--title", "-t", type=str, help="Title to search")
@click.option("--author", "-a", type=str, help="Author to search")
@click.option("--format", "-f", type=str, help="Output format", default='json')
def search(title, author, **kwargs):
    if not (title or author):
        print("Pass either --title or --author")
        exit(-1)
    else:
        search = Search(title or author, kwargs)
        search.run()


if __name__ == '__main__':
    cli()
