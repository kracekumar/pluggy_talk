import pluggy
import json
from pygments import highlight, lexers, formatters
import click


hookimpl = pluggy.HookimplMarker("gutenberg")


@hookimpl
def get_click_group(group):
    # Add option to the existing command
    indent = click.Option(
        ["--indent", "-i", "indent"],
        show_default=True,
        type=int,
        help="Indent size",
        default=4,
    )
    colorize = click.Option(
        ["--colorize", "-c", "colorize"],
        show_default=True,
        type=bool,
        help="Colorize the output",
        default=True)
    command = group.get_command({}, "search")
    command.params.append(indent)
    command.params.append(colorize)


def colorize(formatted_json):
    return highlight(
        formatted_json.encode("UTF-8"),
        lexers.JsonLexer(),
        formatters.TerminalFormatter(),
    )


@hookimpl
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
    indent = kwargs.get("indent", 4)
    #print(f"Using the indent size as {indent}")
    if kwargs.get('format', '') == 'json':
        formatted_json = json.dumps(table, sort_keys=True, indent=indent)
        if kwargs.get('colorize'):
            print(colorize(formatted_json))
        else:
            print(formatted_json)
