#!/usr/bin/env python
"""select a broweser to use for each URL by rules
"""
__author__ = """halloleo"""
__version__ = """0.1"""

import sys
import logging as log
log.basicConfig(level=log.DEBUG)
import webbrowser


def select_and_open (url):
    # set default browser
    log.debug("set default browser (fixed as chrome)")
    selected_browser = webbrowser.get('open -a Google\ Chrome.app %s')
    # browser for files
    if url.startswith('file'):
        log.debug("'file' browser")
        selected_browser = webbrowser.get('safari')
    # browser comming from emacs
    elif url.startswith('emacs-'):
        log.debug("emacs browser")
        url = url[len('emacs-'):]
        selected_browser = webbrowser.get('open -a Firefox.app %s')

    selected_browser.open_new_tab(url)

args = sys.argv[1:]
for arg in args:
    log.debug("open urls '%s'" % arg)
    select_and_open(arg)
