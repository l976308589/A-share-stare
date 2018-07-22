import sys
import traceback


def Except():
    s = sys.exc_info()
    traceback.print_exc()
    return "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
