'''
# The  class is a utility for encapsulating and manipulating the path component of a URL, including adding nodes, parsing path strings, and building path strings with optional encoding.

import urllib.parse

class UrlPath:
    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments and a flag indicating the presence of an end tag.
        """

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        """


    def parse(self, path, charset):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        """


    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :return: str, the fixed path string.
        """

'''

import urllib.parse


class UrlPath:
    def __init__(self):
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        self.segments.append(self.fix_path(segment))

    def parse(self, path, charset):
        if path:
            if path.endswith('/'):
                self.with_end_tag = True

            path = self.fix_path(path)
            if path:
                split = path.split('/')
                for seg in split:
                    decoded_seg = urllib.parse.unquote(seg, encoding=charset)
                    self.segments.append(decoded_seg)

    @staticmethod
    def fix_path(path):
        if not path:
            return ''

        segment_str = path.strip('/')
        return segment_str


