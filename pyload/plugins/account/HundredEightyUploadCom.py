# -*- coding: utf-8 -*-

from pyload.plugins.internal.XFSAccount import XFSAccount


class HundredEightyUploadCom(XFSAccount):
    __name__    = "HundredEightyUploadCom"
    __type__    = "account"
    __version__ = "0.02"

    __description__ = """180upload.com account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Walter Purcaro", "vuolter@gmail.com")]


    HOSTER_DOMAIN = "180upload.com"
