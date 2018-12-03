
import sys,os
"""
Python 3 好像不需要
reload(sys)
sys.setdefaultencoding('utf8')
"""
from Utils import Util
if Util.isWindows():
    activate_this = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir,'venv/Scripts/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
else:
    #linux
    activate_this = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir,'venv/bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
