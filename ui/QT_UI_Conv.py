#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os           
import platform

# 找出正確的 OS
#print (platform.system())

if ('Linux' == platform.system()):
    uicProg = 'pyuic5'
    rccProg = 'pyrcc5'
else:
    uicProg = @'"D:\Python\Python27\python.exe" "D:\Python\Python27\Lib\site-packages\PyQt4\uic\pyuic.py"'
    rccProg = @'"D:\Python\Python27\Lib\site-packages\PyQt4\pyrcc4.exe"' 



for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.ui'):
            os.system(f'{uicProg} -o build/ui_%s.py %s' %
                      (file.rsplit('.', 1)[0], file))
            # print "D:\Python\Python27\python.exe" ' "D:\Python\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -o ui_%s.py %s' % (
            #    file.rsplit('.', 1)[0], file)
        elif file.endswith('.qrc'):
            os.system(f'{rccProg} -o build/%s_rc.py %s' %
                      (file.rsplit('.', 1)[0], file))
