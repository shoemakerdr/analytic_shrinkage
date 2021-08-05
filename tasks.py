"""
`invoke` tasks

List available tasks:
$ inv -l
"""

from pathlib import Path
import shutil

import invoke


@invoke.task
def clean(c):
    """
    Clean up builds

    $ inv clean
    """
    print("Cleaning `dist` directory...")
    if Path("dist").exists():
        shutil.rmtree("dist")

@invoke.task
def build(c):
    """
    Builds package distributions

    $ inv build
    """
    print("Running build...")
    c.run("python -m build")


@invoke.task
def conda_build(c):
    """
    Builds conda package

    $ inv conda-build
    """
    print("Running conda build...")
    c.run("conda build conda_recipe")


@invoke.task
def publish(c):
    """
    Builds package distributions

    $ inv publish
    """
    print("Running build...")
    c.run("python -m twine upload dist/*")


@invoke.task
def test(c):
    """
    Run tests

    $ inv test
    """
    print("Running tests...")
    c.run("pytest")

