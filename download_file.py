from requests import get
import urllib.request
from urllib.request import urlretrieve
import sys
import os


class Downloader:

    def __init__(self, url, file_name="", path=os.path.curdir):
        self.url = url
        if file_name == "":
            self.file_name = self.url.split('/')[-1]
        else:
            self.file_name = file_name
        self.path = path

    def set_new_file(self, url, file_name="", path=os.path.curdir):
        self.url = url
        self.get_file_name(file_name)
        self.path = path

    def get_file_name(self, file_name):
        if file_name == "":
            self.file_name = self.url.split('/')[-1]
        else:
            self.file_name = file_name

    def download_this_file(self):
        urlretrieve(self.url, os.path.join(self.path, self.file_name), self.reporthook)

    def reporthook(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = "\r%5.1f%% %*.2fmb / %.2fmb %s" % (percent, len(str(totalsize)), readsofar / 1000000, totalsize / 1000000, self.file_name)
            sys.stderr.write(s)
            if readsofar >= totalsize: # near the end
                sys.stderr.write("\n")
        else: # total size is unknown
            sys.stderr.write("read %d\n" % (readsofar,))


file_dl = Downloader("https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe")
file_dl.download_this_file()

file_dl.set_new_file("https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi")
file_dl.download_this_file()
