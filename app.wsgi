# _*_ coding:utf-8 _*_

import sys
import logging
from traceback import format_exc

#Expand Python classes path with your app's path
#将项目根目录加入环境变量
sys.path.insert(0, "C:\Users\sunzhiming\Desktop\\blueprint")
 

##引入你的app
from run import app


 
#Put logging code (and imports) here ...
##日志，如果需要可以引入
 
#Initialize WSGI app object

application = app
