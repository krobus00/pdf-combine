import os
from PIL import Image
from PyPDF2 import PdfFileMerger
from datetime import datetime
class pdf:
    """
    class converter gambar ke pdf dan mengabungkan beberapa pdf
    """
    def __init__(self, dir):
        self.dir = dir
    def savetopdf(self):
        """
        method simpan dalam bentuk pdf
        """
        imageList = []
        for idx,val in enumerate(os.listdir(self.dir)):
            if val.endswith('.pdf'):
                continue
            if idx != 0:
                img = Image.open('{}/{}'.format(self.dir,val).format(self.dir,val),"r")
                img.convert('RGB')
                imageList.append(img)
            else:
                img1 =  Image.open('{}/{}'.format(self.dir,val).format(self.dir,val),"r")
                img1.convert('RGB')
        img1.save(r"./output/{}.pdf".format(datetime.now().strftime("%d%m%Y %H%M%S")),save_all=True, append_images=imageList)
    def pdfmerger(self):
        """
        method mengabungkan pdf
        """
        merge_list = []
        for x in os.listdir(self.dir):
            if not x.endswith('.pdf'):
                continue
            merge_list.append(self.dir + x)

        merger = PdfFileMerger()

        for pdf in merge_list:
            merger.append(pdf)

        merger.write("./output/{}.pdf".format(datetime.now().strftime("%d%m%Y %H%M%S")))#your output directory
        merger.close()