# `fixstb`

Fixstb is a tool for fixing the HTML imported from Sakai to Brightspace.

The main problem is that LaTeX code between dollar signs was not originally
converted to any math mode. Fixstb takes care of that.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* A command line.  Fixstb is developed on a Mac.
* Python 3.9

## Installing `fixstb`

To install `fixstb`, follow these steps:

Linux and macOS:

* clone the repository
* install a virtualenv

```shell
git clone https://github.com/leingang/python-fixstb.git
cd python-fixstb
virtualenv-3.9 ~/.local/share/virtualenvs/fixstb
. ~/.local/share/virtualenvs/fixstb/bin/activate
python -m pip install click
python -m pip install latex2mathml
```

Windows:

Not attempted.  If you have and can contribute here, please do.

## Using `fixstb`

`fixstb` provides one script, which has a command line interface

```
./fixstb.py in.html
```

You can leave off the file argument, in which case `fixstb.py` will read
`STDIN`.

Here is a recommended workflow.

1. Open a Brightspace page in the browser and a terminal window alongside it.
2. In the browswer, edit any RTE element and choose the `</>` option to view the source.
3. Copy the source to the clipboard.
4. In the terminal window, type `pbpaste | ./fixstb.py | pbcopy`.  This will replace the contents of the clipboard with the fixed version.
5. Back in the browser, paste.
6. Go to the next element that needs to be converted and repeat.  Since the terminal command doesn't change, it can be repeated with an up-arrow and return.

Options:

* `--verbose`: be verbose
* `--debug`: print debugging statements

## Contributing to `fixstb`
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to fixstb, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

This package is built on:

* click: A great Python library for creating command line applications
* latex2mathml: A small package for converting LaTeX to MathML

## Contact

Matthew Leingang (leingang@nyu.edu) is the principal developer of this project.

## License

This project uses the MIT license.
