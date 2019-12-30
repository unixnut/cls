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

Credits
-------

This package was created with [Cookiecutter][] and the [`audreyr/cookiecutter-pypackage`][pp]
project template.

  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [pp]: https://github.com/audreyr/cookiecutter-pypackage

