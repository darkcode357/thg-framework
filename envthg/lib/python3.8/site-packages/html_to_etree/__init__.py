# -*- coding: utf-8 -*-

"""
parse a html document into an lxml etree

Notes:
- https://github.com/buriy/python-readability/issues/42
- https://github.com/scrapy/scrapy/blob/c68140e68a7aee894e304122e2532c2fc7edfdc5/scrapy/http/response/text.py#L69
"""

__author__ = 'Johannes Ahlmann'
__email__ = 'johannes@fluquid.com'
__version__ = '0.2.0'

import lxml
import lxml.etree
from lxml.html.clean import Cleaner
from w3lib.encoding import html_to_unicode, resolve_encoding
import cchardet as chardet


# 'cleaner' settings used by teamhg-memex/html-text
clean_html = Cleaner(
    scripts=True,
    javascript=False,  # onclick attributes are fine
    comments=True,
    style=True,
    links=True,
    meta=True,
    page_structure=False,  # <title> may be nice to have
    processing_instructions=True,
    embedded=True,
    frames=True,
    forms=False,  # keep forms
    annoying_tags=False,
    remove_unknown_tags=False,
    safe_attrs_only=False,
).clean_html


def _detect_encoding(bytestring, default_encoding='utf-8'):
    # NOTE: alternatively `UnicodeDammit(x).originalEncoding`
    # NOTE: alternatively use scrapy.http.TextResponse().text
    encoding = chardet.detect(bytestring).get('encoding')
    if encoding:
        # TODO: `resolve_encoding`?
        return resolve_encoding(encoding)
    else:
        return default_encoding


def _decode_bytes(body, content_type='', default_encoding='utf-8'):
    encoding, uni_string = html_to_unicode(
        content_type_header=content_type,
        html_body_str=body,
        default_encoding=default_encoding,
        auto_detect_fun=_detect_encoding)
    return (encoding, uni_string)


def parse_html_bytes(body, content_type='', default_encoding='utf-8'):
    encoding, uni_string = _decode_bytes(body, content_type, default_encoding)
    return parse_html_unicode(uni_string)


def parse_html_unicode(uni_string):
    parser = lxml.html.HTMLParser(encoding='utf8')
    return lxml.html.fromstring(uni_string.encode('utf8'), parser=parser)
