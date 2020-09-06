# *term2web*: terminal in a web page (*Python* version)

[![Run on Repl.it](https://q37.info/s/kpm7xhfm.png)](https://q37.info/s/kjjcfcp3)

[![license: MIT](https://img.shields.io/github/license/epeios-q37/term2web-python?color=yellow&style=for-the-badge)](https://github.com/epeios-q37/term2web-python/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/epeios-q37/term2web-python.svg?style=for-the-badge)](https://github.com/epeios-q37/term2web-python/stargazers)
[![Forks](https://img.shields.io/github/forks/epeios-q37/term2web-python.svg?style=for-the-badge)](https://github.com/epeios-q37/term2web-python/network/members)
[![Downloads](https://img.shields.io/pypi/dm/term2web.svg?label=&style=for-the-badge)![Version](https://img.shields.io/pypi/v/term2web?style=for-the-badge&color=90b4ed&label=PyPi)](http://q37.info/s/c7pnhdm7)

***Notice française*** : https://q37.info/s/rhj9qmb9.

---

***Note for Repl.it users (online demonstrations)***: **after the first demonstration, you may have to click the refresh button (red arrow on picture below) to display the QR code for the other demonstrations.**

[![The refresh button](https://q37.info/s/vsc3c7gc.png "The button to click to display the QR code")](http://q37.info/s/zbgfjtp9)

---

This library is like [*termcolor*](https://pypi.org/project/termcolor/), but with all the text formatting possibility of [*CSS*](https://en.wikipedia.org/wiki/Cascading_Style_Sheets).

Install (`pip install term2web`), import (`from term2web import *`) on the top of your program, and all `print(…)` and `input(…)` will be redirected to a web page.

You can also launch:
- `git clone http://github.com/epeios-q37/term2web-python`,
- `cd term2web-python`,
- `python3 main.py` (or directly `python3 Basic.py` or `python3 WithCSS.py`).

Online demonstration: https://q37.info/s/kjjcfcp3.

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

`Basic.py` is an example with calls to `print(…)` and `input(…)`, but without CSS formatting. Comment out the `import * from term2web` for the program to run in the usual way in a terminal.

`WithCSS.py` shows how CSS rules can be used to format the displayed text.

<!-- There is also a stub to for this library at address <https://q37.info/s/qh99qtjt>.-->

You can still use the default `print(…)` and `input(…)` after an `import builtins` with `builtins.print(…)` and `builtins.input(…)`.

Unlike other programs based on the [*Atlas* toolkit](https://atlastk.org), on which this library is based, it is not possible to simultaneously launch two or more instances of a program based on the *term2web* library. This is intentional, in order to keep this library simple to use. 

---

This project is based on the [*Atlas* toolkit](https://atlastk.org). Other projects using this toolkit can be found here: <https://q37.info/s/sssznrb4>.
