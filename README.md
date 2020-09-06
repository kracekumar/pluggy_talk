# pluggy_talk
Sample code for Pluggy Talk

### Setup the repo

- Create a virtual environment using conda or virtualenv.
Here is a conda example `conda create -n pluggy_talk python=3.7`
- Activate the environment. `conda activate pluggy_talk`.
- Install requirements using Pip. `pip install -r requirements.txt`.

### Run the code

``` bash
$python host.py search -t "My freedom and My bondage" --indent 8
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
```

### Run tests

- Run tests using pytest.

``` bash
$pytest -vv tests.py
...
collected 1 item

tests.py::test_search PASSED
```

Slides: https://slides.com/kracekumarramaraju/pluggy
