# Property Pricing Model

## Getting Started

### Prerequisites

Ensure you have on your system:

* `pip` v3
* `python` v3.6

#### Poetry

Poetry is a Python dependency management tool. Use `poetry` to manage your Python virtualenv.

Install [Poetry](https://python-poetry.org/docs/#installation). Add to your .rc file (e.g. `.zshrc` ):

``` bash
source $HOME/.poetry/env
```

#### Docker

#### Environment variables

Add to your `.bashrc` (or your relevant `.*rc` file):

``` bash
# Insurami
export EPC_KEY=<EPC API KEY>
```

### Install

Install `poetry` :

``` bash
# Install dependencies via poetry
poetry install

# Spawn new shell within virtualenv.
poetry shell
```

### Update

Add a dependency:

``` bash
poetry add <PyPI package>
```

Update dependencies:

``` bash
poetry update
```

Make sure to commit your `poetry.lock` file when you update dependencies.

### Migrate db

FOR LOCAL DATABASE. After making model changes, run:

``` bash
flask db migrate -m <details of migration>
flask db upgrade
```

## Linting

We use [Black formatting](https://github.com/psf/black). Make sure to your code
follows their strict formatting guidelines. Check like so:

``` bash
poetry run black --check --line-length 79 insurami/path/to/my/file.py
```

Auto-correct without the `--check` argument.

## Testing

### Unit tests

``` bash
poetry run pytest
```

### External APIs

Just EPC at the moment
