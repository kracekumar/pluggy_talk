import pluggy
import click
import requests
import hookspecs
import output


class Search:
    def __init__(self, term, hook, kwargs):
        self.term = term
        self.hook = hook
        self.kwargs = kwargs

    def make_request(self):
        resp = requests.get(f"http://gutendex.com/books/?search={self.term}")
        return resp

    def run(self):
        resp = self.make_request()
        self.hook.print_output(resp=resp, kwargs=self.kwargs)


def get_plugin_manager():
    pm = pluggy.PluginManager("gutenberg")
    pm.add_hookspecs(hookspecs)
    # pm.load_setuptools_entrypoints("gutenberg")
    pm.register(output)
    return pm


@click.group()
def cli():
    pass


@cli.command()
@click.option("--title", "-t", type=str, help="Title to search")
@click.option("--author", "-a", type=str, help="Author to search")
def search(title, author, **kwargs):
    if not (title or author):
        print("Pass either --title or --author")
        exit(-1)
    else:
        pm = get_plugin_manager()
        search = Search(title or author, pm.hook, kwargs)
        search.run()


def setup():
    pm = get_plugin_manager()
    pm.hook.get_click_group(group=cli)


if __name__ == "__main__":
    setup()
    cli()
