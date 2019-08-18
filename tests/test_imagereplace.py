import unittest
import tempfile
from os import path
from lxml import etree

from mailmerge import MailMerge
from tests.utils import EtreeMixin, get_document_body_part


class ReplaceImageTests(EtreeMixin, unittest.TestCase):
    def test_with_path(self):
        with MailMerge(path.join(path.dirname(__file__), 'test.docx')) as document:

            document.replace_image(1, 'gmei_screenshot.png')
            with open('out.docx', 'wb') as outfile:
                document.write(outfile)

    def test_with_stream(self):
        with MailMerge(path.join(path.dirname(__file__), 'test.docx')) as document:
            with open('gmei_screenshot.png', 'rb') as img:
                document.replace_image(1, img)

                with open('out2.docx', 'wb') as outfile:
                    document.write(outfile)