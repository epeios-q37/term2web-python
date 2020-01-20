# *term2web*: terminal in a web page (*Python* version)

[![Run on Repl.it](https://repl.it/badge/github/epeios-q37/tortoise-python)](https://q37.info/s/kjjcfcp3) [![Version](https://img.shields.io/pypi/v/term2web?color=90b4ed&label=PyPi)](https://q37.info/s/c7pnhdm7) [![license: MIT](https://img.shields.io/github/license/epeios-q37/term2web-python)](https://github.com/epeios-q37/term2web-python/blob/master/LICENSE)

***Notice française*** : https://q37.info/s/rhj9qmb9.

**About *Repl.it***: it seems that *Repl.it* sometimes crashes with the content of this repository. This can be avoided by hiding (putting back) the corresponding navigator tab until all files are loaded (~45 s).

This library is like [*termcolor*](https://pypi.org/project/termcolor/), but with all the formatting possibility of [*CSS*](https://en.wikipedia.org/wiki/Cascading_Style_Sheets).

Install (`pip install term2web`), import (`from term2web import *`) and all `print(…)` and `input(…)` will be redirected to a web page.

You can also launch:
- `git clone http://github.com/epeios-q37/term2web-python`,
- `cd term2web-python`,
- `python3 main.py` (or directly `python3 Basic.py` or `python3 WithCSS.py`).

Live demonstration: https://q37.info/s/kjjcfcp3.

There are three other functions available.

`set_property(name,value)` applies the CSS property of name `name` and value `value`.

Example:

```python
set_property("font-style", "italic")
```

`set_properties(properties)` applies the CSS properties stored in `properties` which is a dictionary whose keys are property names, and values the corresponding property values.

Example:

```python
set_properties({
    "text-decoration-line": "line-through",
    "text-decoration-style": "wavy",
    "text-decoration-color": "red"
})
```

`reset_properties()` removes all the CSS properties set by above functions.

`Basic.py` is an example with calls to `print(…)` and `input(…)`, but without CSS formatting.

`WithCSS.py` shows how CSS is used to format the displayed text.

There is also a stub to for this library at address <https://q37.info/s/qh99qtjt>.

Unlike other programs based on the *Atlas* toolkit, on which this library is based, it is not possible to simultaneously launch two or more instances of a program based on the *term2web* library. This is intentional, in order to keep this library simple to use, as it is mainly intended for beginners.

---

This project is based on the [*Atlas* toolkit](https://atlastk.org). Other projects using this toolkit can be found here: <https://q37.info/s/sssznrb4>.
