#!/usr/bin/python
# coding: utf-8

import unittest

import faces


class FacesTest(unittest.TestCase):
    def setUp(self):
        with open('tests/Roosevelt.jpg', 'rb') as valid_image:
            self.image_by_file = faces.FaceAppImage(file=valid_image)

        valid_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/President_Roosevelt_-_Pach_Bros.tif/lossy-page1-220px-President_Roosevelt_-_Pach_Bros.tif.jpg'
        self.image_by_url = faces.FaceAppImage(url=valid_url)

if __name__ == "__main__":
    unittest.main()
