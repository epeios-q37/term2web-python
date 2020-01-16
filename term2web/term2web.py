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

import os, sys, threading, time, html

# Detecting 'Repl.it' environment.
if ('HOME' in os.environ) and (os.environ['HOME'] == '/home/runner'):
  os.environ["ATK"] = "REPLit"

sys.path.append("./Atlas.zip")
sys.path.append("../Atlas.zip")

import atlastk as Atlas

head = """
<title>'term2web' for Python</title>
<link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAMFBMVEUEAvyEhsxERuS8urQsKuycnsRkYtzc2qwUFvRUVtysrrx0ctTs6qTMyrSUksQ0NuyciPBdAAABHklEQVR42mNgwAa8zlxjDd2A4POfOXPmzZkFCAH2M8fNzyALzDlzg2ENssCbMwkMOsgCa858YOjBKxBzRoHhD7LAHiBH5swCT9HQ6A9ggZ4zp7YCrV0DdM6pBpAAG5Blc2aBDZA68wCsZPuZU0BDH07xvHOmAGKKvgMP2NA/Zw7ADIYJXGDgLQeBBSCBFu0aoAPYQUadMQAJAE29zwAVWMCWpgB08ZnDQGsbGhpsgCqBQHNfzRkDEIPlzFmo0T5nzoMovjPHoAK8Zw5BnA5yDosDSAVYQOYMKIDZzkoDzagAsjhqzjRAfXTmzAQgi/vMQZA6pjtAvhEk0E+ATWRRm6YBZuScCUCNN5szH1D4TGdOoSrggtiNAH3vBBjwAQCglIrSZkf1MQAAAABJRU5ErkJggg==" />
<style type="text/css">
 html, body {height: 100%; padding: 0; margin: 0; width: 100%;}
 .vcenter-out, .hcenter { display: table; height: 100%; margin: auto;}
 .vcenter-in {display: table-cell; vertical-align: middle;}
 .hidden {display: none;}
 input[type="text"] {border: none;}
 input[type="text"]:disabled {background-color: transparent; color: inherit;}
</style>
<style id="console">
	fieldset {
		font-family: monospace;
		font-size: larger;
	}
</style>
"""

body = """
<div class="vcenter-out">
	<div class="vcenter-in">
		<fieldset id="Output" data-xdh-onevent="Focus"/>
	</div>
</div>
"""

_print = ""
_printBuffer = "<span>"
_printRead = threading.Lock()
_printRead.acquire()
_printWrite = threading.Lock()
_printWrite.acquire()

_flush = threading.Lock()
_autoFlush = False

_input = ""
_inputRead = threading.Lock()
_inputRead.acquire()
_inputWrite = threading.Lock()
_inputWrite.acquire()

_properties = {}

def getStyle_():
	style = ""

	for name in _properties: 
		style += name + ": " + _properties[name] + "; "

	return style


def openingTag_():
	return "<span style='" + getStyle_() + "'>"


def closingTag_():
	return "</span>"


def reset_properties():
	global _properties, _printBuffer

	_properties = {}

	_printBuffer += closingTag_()
	_printBuffer += openingTag_()


def set_property(name, value):
	global _properties, _printBuffer

	_properties[name] = value

	_printBuffer += closingTag_()
	_printBuffer += openingTag_()
	

def set_properties(properties):
	global _properties, _printBuffer

	for name in properties:
		_properties[name] = properties[name]

	_printBuffer += closingTag_()
	_printBuffer += openingTag_()
	


def handleSpecialChars_(text):
	return text.replace('\n', "<br/>").replace(" ","&nbsp;")


def flush_():
	global _print, _printBuffer, _printRead, _printWrite, _autoFlush
	if _printBuffer:
		_flush.acquire()
		_printWrite.acquire()
		_print = _printBuffer + closingTag_()
		_printBuffer = openingTag_()
		_printRead.release()
		_flush.release()

	_autoFlush = False


def addToBuffer_(text):
	global _printBuffer

	text= str(text)

	_printBuffer += handleSpecialChars_(html.escape(text))



def print(*args, sep=" ", end="\n"):
	global _printBuffer, _printRead, _printWrite, _autoFlush

	first = True

	for arg in args:
		if first:
			first = False
		else:
			addToBuffer_(sep)

		addToBuffer_(arg)

	addToBuffer_(end)

	_autoFlush = True


def input(prompt=""):
	global _print, _printRead,_printWrite, _input, _inputRead,_inputWrite, _autoFlush

	_autoFlush = False

	if prompt:
		print(prompt,end="")
		flush_()

	result = ""
	_printWrite.acquire()
	_printRead.release()
	_inputRead.acquire()
	result = _input
	_input = ""
	_inputWrite.release()

	return result


def scrollToBottom_(dom):
	dom.execute("window.scrollTo(0,document.getElementById('Output').scrollHeight);")


def loop_(dom):
	global _print, _printRead,_printWrite, _input, _inputRead,_inputWrite,_autoFlush
	cont = True
	
	_autoFlush = True

	while cont:
		_printRead.acquire()

		if _print:
			dom.appendLayout("Output", "<span>" + _print + "</span>")
			scrollToBottom_(dom)
			_print = ""
		else:
			cont = False
		_printWrite.release()

	dom.appendLayout("Output","<span><input type='text' id='Input' data-xdh-onevent='Submit'/><br/></span>")
	scrollToBottom_(dom)
	dom.focus("Input")


def acConnect(dom):
	global _printWrite, _inputWrite
	dom.setLayout("", body)
	_printWrite.release()
	_inputWrite.release()
	loop_(dom)


def acSubmit(dom, id):
	global _print, _printRead,_printWrite, _input, _inputRead,_inputWrite

	_inputWrite.acquire()
	_input = dom.getContent("Input")
	dom.disableElement("Input")
	dom.removeAttribute("Input","data-xdh-onevent")
	dom.removeAttribute("Input","id")
	_inputRead.release()
	loop_(dom)


def acFocus(dom):
	dom.focus("Input")


callbacks = {
	"": acConnect,
	"Submit": acSubmit,
	"Focus": acFocus,
}


class Atlas_(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		Atlas.launch(callbacks, None, head, "Blank")


_atlasThread = Atlas_()
# _atlasThread.daemon = True
_atlasThread.start()


class Flush_(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True:
			time.sleep(.1)
			if _autoFlush:
				flush_()


_flushThread = Flush_()
# _flushThread.daemon = True
_flushThread.start()
