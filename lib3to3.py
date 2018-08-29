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

    # set this to True or False.  False to get the list of functions
    # that *need* conversion; True to actually *do* the conversion,
    # however a file camel_case_log.txt is required, which
    # can only be generated through the development_dynamic
    # JSBase.__getattr__ override
    config_info.action_camel_case = True

    if config_info.action_camel_case:
        fixname = 'camelcasecallers'
    else:
        fixname = 'camelcaseinkls'

    # set this (and action_camel_case=True) to actually change
    # called functions (NOT CALLERs)
    config_info.action_camel_case = True # action the list
    config_info.check_camel_case = False # overwrites the list (doh)
    fixname = 'camelcaseinkls'

    if main("js", ['--no-diffs', '-w',
                   '-f', fixname,
                   '-n', filename]):
        raise Exception('py3 conversion failed')

    #with open(outfile) as f:
    #    f = f.read()
    #    print (f)

    config_info.save()
