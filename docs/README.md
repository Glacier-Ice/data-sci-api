# Documentation

## Development

Install the dependencies with:

```
pip install -r requirements.txt
```

Start the docs server with 

```
mkdocs serve
```

and watch the results in your browser (by default at http://127.0.0.1:8000).

## Build and Deploy

From the current directory, use:

```
mkdocs gh-deploy --config-file ./docs/mkdocs.yml
```
to deploy the docs.
