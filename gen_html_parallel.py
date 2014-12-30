from multiprocessing import Pool
import os
from subprocess import Popen, PIPE, call

'''
Script to parellelize the HTML doc generation.

Adjust the number of processes.

'''

def processLang(lang):
    cmd = "sphinx-build -a -b html -d build/doctrees/ -D language=%s source build/html-%s" %(lang, lang)
    print cmd
    p = Popen(cmd.split(" "), stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        print stderr
        print stdout

if __name__ == '__main__':


    cmd = "sphinx-intl -c source/conf.py build -d source/locale"
    print cmd
    p = Popen(cmd.split(" "), stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        print stderr
        print stdout

    pool = Pool(processes=8)

    languages=[
      'ar',
      'ca',
      'cs',
      'de',
      'es',
      'en',
      'fr',
      'he',
      'hu',
      'it',
      'jp',
      'kk',
      'pl',
      'pt_BR',
      'pt_PT',
      'ro',
      'ru',
      'sv',
      'tr',
      'uk']

    result = pool.map(processLang, languages)
    print 'Results are', result
