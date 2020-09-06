from host import setup, search
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
