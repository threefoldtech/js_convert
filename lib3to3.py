from lib2to3.main import main
import sys
import os
import shutil
import config_info

if __name__ == '__main__':

    # 2to3 is way too chatty
    #import logging
    #logging.basicConfig(filename=os.devnull)

    config_info.load()

    filename = sys.argv[1]
    #outfile = os.path.join('out', os.path.basename(filename))

    shutil.rmtree('./out', ignore_errors=True)
    os.mkdir('out')
    #shutil.copy(filename, outfile)

    config_info.action_camel_case = True

    if config_info.action_camel_case:
        fixname = 'camelcasecallers'
    else:
        fixname = 'camelcaseinkls'

    fixname = 'camelcase'

    if main("js", ['--no-diffs', '-w',
                   '-f', fixname,
                   '-o', 'out', '-n', filename]):
        raise Exception('py3 conversion failed')

    #with open(outfile) as f:
    #    f = f.read()
    #    print (f)

    config_info.save()
