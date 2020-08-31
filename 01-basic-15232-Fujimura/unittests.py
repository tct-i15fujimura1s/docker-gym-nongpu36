#%load unittests.py
from IPython.display import HTML

import re
from nose.tools import eq_,ok_,assert_equal,assert_in,assert_equal,assert_not_equal,assert_regex
import sys, io, contextlib

class Data(object):
    pass

@contextlib.contextmanager
def capture_stdout():
    old = sys.stdout
    capturer = io.StringIO()
    data = Data()
    try:
        sys.stdout = capturer
        yield data
    finally:
        sys.stdout = old
        data.result = capturer.getvalue()

def _alert(msg):
	display(HTML("""
    <div class="alert alert-danger" style="animation: alert 2s ease-in infinite alternate">{msg}</div>
    <style>
    @keyframes alert {{
        0% {{background-color: #f2dede}}
        100% {{background-color: #ff0000}}
    }}
    </style>
    """.format(msg=msg)))