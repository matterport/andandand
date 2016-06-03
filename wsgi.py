"""
andandand: Health checker

Does not support (local) endpoints with dot separators for hypothetical
security reasons.

. is where the configuration comes from. So use uwsgi's --chdir2 or
--chroot to set . appropriately.
"""

from urllib2 import urlopen
import os

TIMEOUT = 2


def application(env, start_response):
    """
    This is where uwsgi calls us.
    """
    config_path = '.'

    def awesome():
        start_response('200', [])

    def notawesome():
        start_response('500', [])
    # Strip beginning /healthcheck/ and sketchy .'s.
    path = env['REQUEST_URI'][len('/healthcheck/'):].strip('.')

    # These are the "endpoints" (/healthcheck/thing) that we respond on.
    local_endpoints = os.listdir(config_path)

    if path in local_endpoints:
        # These are the endpoints that we check to determine if we return
        # a 200 or a 500.
        for url_file in os.listdir(path):
            url_filepath = os.path.join(path, url_file)
            for url in open(url_filepath).readlines():
                try:
                    status = (urlopen(url, timeout=TIMEOUT).getcode())
                except:
                    status = 'Not great'
            if status != 200:
                notawesome()
                return ''
        awesome()
    else:
        notawesome()
    return ''
