# data-sci-api

![Python3.6](https://img.shields.io/badge/python-3.6-green.svg?style=flat-square&logo=python&colorB=blue)
[![Built with love](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square)](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square&logo=love)
[![Code style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square)](https://github.com/pre-commit/pre-commit)
<!-- ![Build Status](https://github.com/rexwangcc/data-sci-api/workflows/Tests%20on%20Pull%20Requests%20and%20Master/badge.svg?branch=master&event=push) -->

English

The API is designed to be thin and stateless. It relies on the data collected and validated by other sub-projects, transform and expose them through standard RESTful APIs. The service is written in Python and Flask.

This API primarily aims at feeding standardized data to data-science use cases.

<p align="center"> 
   <img src="https://www.lucidchart.com/publicSegments/view/6ab27659-257a-44ce-a478-46dad3328b9c/image.png" width="70%" height="70%">
</p>

## Get Started

Please first clone this repository and the sub-module-repo by:

```
git clone https://github.com/rexwangcc/data-sci-api
cd data-sci-api
git clone https://github.com/rexwangcc/data-sci-api
```

### Running locally with Docker (Recommended)

**Pre-requisite: You have to have [Docker client](https://www.docker.com/products/docker-desktop) installed on your machine.**

#### Build the Docker image

Run:
```
docker build -t data-sci-api:default .
```
from the root directory of the clone of this repo. Note this step could take a long time depends on where you are located in.

#### Run built Docker image

Run:
```
docker run --name data-sci-api --publish 8081:8081 data-sci-api:default 
```
and then open `http://localhost:8081` in your browser. _(Add `-d` to run the Docker container in detach/background mode)_

You should see a Swagger page documents the available endpoints now.

_If you ran into error `The container name "/data-sci-api" is already in use`, please run `docker rm data-sci-api` to delete previous container which has the same name._

#### Stop running Docker container

Run:
```
docker stop data-sci-api
```
to stop the running container.

### Running with your own Python environment

Please make sure you have **Python3.6** installed, (ideally you should be using a [VirtualEnv](https://docs.python.org/3.6/tutorial/venv.html)
or something like [PyEnv](https://github.com/pyenv/pyenv)). Then from the root directory of the cloned repo, run:

```
pip install -U -r requirements.txt
```

and then start the server by:

```
bash start_server
```
now if you open `http://localhost:8081` in your browser, you should see a Swagger page documents the available endpoints.

## Contributing Guide

As the above Tech Arch diagram shows (dot-line entities mean they are not there yet), this project is purely data-driven and the core layout looks like the following:

```
src
├── __init__.py
├── api/
├── core/
├── main.py
├── swagger/
├── tests/
└── utils/
```

`main.py` is the entry point of the services and it helps:
- glue all sub API YML files together to an aggregated YML
- send the YML to connection which renders the Swagger UI and applies the API resolvers.
- load required service-level connfigurations (such as debug, logging, path to the data sources, etc.).

### To add new or edit on existing API endpoint(s)

In general you need to edit the `src/swagger/api.yml` and probably its dependencies (such as `donation.yml`). **Be aware that any changes to the YML files can change the data model and breaks the system and the API consumers.**

If you are using a local Python3.6 environment, setting `debug=True` in `main.py` will help you see the changes you made in the Swagger UI in real time. 

Be aware that the `operationId` field in the YML files works as automatic routers that map your endpoint to your Python views functions. To make the endpoints functional, you also have to add/edit the functions in `src/api`. The results of the functions need to be consistent with the data model defined in the API YML file(s).

## Development

 <p align="center"> 
    <img src="https://www.lucidchart.com/publicSegments/view/b853bf49-31fa-46ba-b732-2eb9de8a2cf8/image.png" width="90%" height="85%">
 </p>

The above diagram shows how to work on this repo:

### Development Process

The development process of this project requires every contributor to fork the repo and only make PRs from the fork to `master` branch. 

#### Setup upstream

From within your fork, use:
```
git remote add upstream git@github.com:rexwangcc/data-sci-api.git
```
to setup this repo as the `upstream`.

#### Keep up-to-date with the upstream

Everytime before you want to make new changes to the repo, use:
```
git fetch upstream
git rebase upstream/master
```
to update your fork with latest changes that have merged to `upstream`'s `master` branch.

#### Code

You need to setup some git-hooks before the first time you push code to the repo. You could install the dependencies by `pip install -r requirements-dev.txt`. The required step here is running `pre-commit install` to install the pre-commit hooks.

You will see some outputs like the following:

```
[INFO] Initializing environment for https://github.com/psf/black.
[INFO] Initializing environment for https://gitlab.com/pycqa/flake8.
[INFO] Installing environment for https://github.com/psf/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
```

Once it's done, please start to code and contribute!

#### Address comments
Once you have finished committing and pushing your changes to your remote fork, please create a PR from your remote repo following the PR template. One of the maintainers of the repo will review and merge your PR. Please note PR that fails the tests cannot be reviewed or merged.

## Deployment

The current deployment is under construction and subjects to change. New documentation is coming soon...
