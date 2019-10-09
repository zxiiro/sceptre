# LEGACY DOCS

Follow these steps to build legacy docs compatible with GH pages deployment (sceptre v2+):

1. Cherry pick this commit into the legacy version of your choice
2. Create python venv
3. install sceptre `pip install .` or `python setup.py install`
4. `cd docs`
5. `make build-gh-pages`
6. Take the `_site/docs` directory and commit it to `sceptre.github.io` as `<version_number>/<content of docs/ directory>`

# Docs

This directory contains the code for Sceptre's [docs](https://sceptre.cloudreach.com).

The docs is written using the [Jekyll](https://jekyllrb.com) framework.

## Ruby

Jekyll depends on Ruby. Documentation on installing Ruby can be found [here](https://www.ruby-lang.org/en/documentation/installation/).

## Usage Summary

For more details see `make help`,

Note: The below assumes you are in the docs directory, if not prefix make commands with `docs-` e.g `make docs-install`

### Install Jekyll

Jekyll and its dependencies can be installed with:

```shell
make install
```

### Build and serve docs locally

The docs can be built with:

```shell
make build-latest
```

To make and serve the docs and watch for changes, run:

```shell
make serve-latest
```

View them at `http://localhost:4000/latest/`
