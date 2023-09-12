`c*ls`
======

Uses colour and pipes output to less, with a sensible prompt.

Each command is equivalent to:-

    cls      ls -FC
    clls     ls -lF --time-style=long-iso
    cllls    ls -lF --time-style=full-iso
    cals     ls -FCA
    calls    ls -lFA --time-style=long-iso
    callls   ls -lFA --time-style=full-iso
    csls     sudo ls -FC
    cslls    sudo ls -lF --time-style=long-iso
    csllls   sudo ls -lF --time-style=full-iso
    csals    sudo ls -FCA
    csalls   sudo ls -lFA --time-style=long-iso
    csallls  sudo ls -lFA --time-style=full-iso

Installation
------------

For this to work, you'll have to edit `.profile` and get it to put
`.local/bin` into your $PATH .

On older Debian/Ubuntu releases:

  1. Run **`pip3 -V`**
  1. If you get a *Command not found* error, run **`sudo apt install python3-pip`** and redo from start
  1. If your *pip* major version is less than 9, run **`pip3 install -U pip && hash -r`**
  1. Run **`pip3 install --user colorls`** 
  1. If this produces an error message, try again without `--user`

On Debian 12 ("Bookworm") and recent Ubuntu releases, pip3 will fail
with a "error: externally-managed-environment" message.  Therefore,
run these commands instead:

  1. **`sudo apt install python3-full pipx`**
  1. **`pipx install colorls`**

This will create symlinks in `~/.local/bin` similar to what **`pip3 install
--user`** does, however they point to a Python virtual environment
created by pipx in `~/.local/pipx/venvs/colorls` .

Upgrades
--------

To upgrade colorls when using pip, run **`pip3 install -U --user colorls`**

To upgrade colorls when using pipx, run **`pipx upgrade colorls`**

TO-DO
-----
  + `LINK_COL_WIDTH` (what does this mean??)
  + Fix inum handling
  + Check for numeric owner/group
  + Use `type -a python3` and `unset VIRTUAL_ENV` when in a venv to break out of it

Development
-----------

Package dependencies are handled by [pipenv](https://pipenv.kennethreitz.org/).
It is assumed that *pipenv* will manage the installation of all concrete
dependency versions.  setup.py reads the dependency info from Pipfile
via the `pipenv` pacakge.

Before you can build the package, you will have to have `make`
installed.  You can then run **`make setup`** to create a [Virtualenv][]
(the `.venv` subdirectory where packages and metadata will be installed)
and then **`. .venv/bin/activate`** to activate it.

Then you can run **`pip install pipenv wheel`** and then use a build
process such as:-

    make build
    make dist
    # ... test .whl file now ...
    make release

Credits
-------

This package was created with [Cookiecutter][] and the [`audreyr/cookiecutter-pypackage`][pp]
project template.

  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [pp]: https://github.com/audreyr/cookiecutter-pypackage
  [Virtualenv]: http://packaging.python.org/guides/installing-using-pip-and-virtual-environments
