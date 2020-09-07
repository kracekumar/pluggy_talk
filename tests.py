import json
import requests
from host import setup, search
from output import print_output
from click.testing import CliRunner


def test_search():
    setup()
    runner = CliRunner()
    result = runner.invoke(
        search,
        ["-t", "My freedom and My bondage", "--indent", 8, "--colorize", "false"],
    )

    expected_output = """
[
        {
                "bookshelves": [
                        "African American Writers",
                        "Slavery"
                ],
                "copyright": false,
                "download_count": 1201,
                "media_type": "Text",
                "name": "Douglass, Frederick",
                "title": "My Bondage and My Freedom",
                "xml": "http://www.gutenberg.org/ebooks/202.rdf"
        }
]
    """
    assert result
    assert result.output.strip() == expected_output.strip()


def test_print_output(capsys):
    resp = requests.get("http://gutendex.com/books/?search=Kafka")
    print_output(resp, {})

    captured = capsys.readouterr()
    assert len(json.loads(captured.out)) >= 1
