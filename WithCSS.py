# coding: utf-8
"""
MIT License

Copyright (c) 2020 Claude SIMON (https://q37.info/s/rmnmqd49)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys,os

sys.path.append("./term2web")

if ('Q37_XPP' in os.environ):
  sys.path.append(os.path.join(os.environ["HOME"],"epeios/other/libs/term2web/PYH/term2web"))


from term2web import *

import builtins

p = builtins.print

properties = {}

def print_and_set_properties(nameOrProperties,value = None):
    global properties

    reset_properties()

    print()

    if value:
        print( nameOrProperties + ": " + value)
        properties[nameOrProperties] = value
    else:
        for name in nameOrProperties:
            print( name + ": " + nameOrProperties[name])
            properties[name] = nameOrProperties[name]

    set_properties(properties)


def show(*args):
    print_and_set_properties(*args)

    print("Lorem ipsum dolor sit amet…")


show({
    "text-decoration-line": "line-through"
})

show({
    "text-decoration-style": "wavy",
    "text-decoration-color": "red"
})

show({
    "color": "white",
    "background-color": "blue",
})

show({
    "text-decoration-line": "none",
    "text-shadow": "0 0 3px #FF0000, 0 0 5px #0000FF",
    "color": "initial",
    "background-color": "lightblue",
})

show({
    "font-style": "italic",
    "font-size": "larger"
})


show({
    "font-weight": "bold",
    "word-spacing": "15px",
    "text-transform": "capitalize"
})

show("letter-spacing", "-2px")

show({
    "outline-style": "dashed",
    "outline-color": "green"
})

sys.exit(0)
