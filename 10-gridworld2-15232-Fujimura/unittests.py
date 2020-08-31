# このセルは自動評価を行うための命令です。内容は無視して，実行(Shift-Enter)のみをしてください。
import re
from nose.tools import (
    eq_,
    ok_,
    assert_almost_equal,
    assert_count_equal,
    assert_equal,
    assert_in,
    assert_is,
    assert_not_equal,
    assert_regex,
)
import sys, io, contextlib
import numpy as np
import numpy.testing as nt


# check if src involves tgt
def _assert_array_involve(src, tgt, msg=""):
    try:
	    assert any( np.array_equal(tgt,i) for i in src )
    except:
        _alert(msg)
        raise ValueError(msg)

# check if src involves all items in tgt
def _assert_dict_equal(src, tgt, msg=""):
    try:
        assert all( (k,v) in src.items() for (k,v) in tgt.items() )
    except:
        _alert(msg)
        raise ValueError


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


class _bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    WHITE = "\033[37m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BG_FAIL = "\033[41m"

from IPython.display import HTML


def _err(msg):
    return _bcolors.FAIL + msg + _bcolors.ENDC

def _alert(msg):
    display(HTML('<div class="alert alert-danger">{msg}</div>'.format(msg=msg)))

from plotchecker import LinePlotChecker, PlotChecker, BarPlotChecker


def _check_axes_title(axes,title=["xtitle","ytitle"]):
    try:
        pc = PlotChecker(axes)
    except:
        _alert("座標コンテナが正常に定義されていないようです")
        raise

    try:
        pc.assert_xlabel_equal(title[0])
    except:
        _alert("横軸のタイトルが不適切です")
        raise

    try:
        pc.assert_ylabel_equal(title[1])
    except:
        _alert("縦軸のタイトル不適切です")
        raise

def _check_labels(axes,labels,msg="凡例が適切に定義されていないようです"):
    try:
        pc = LinePlotChecker(axes)
    except:
        _alert("座標コンテナが正常に定義されていないようです")
        raise

    try:
	    pc.assert_labels_equal(labels)
    except:
        _alert(msg)
        raise		

def ut_msg(func,arg,msg=""):
    try:
        ret=func(arg)
    except:
        _alert(msg)
        raise ValueError(msg)
    return ret