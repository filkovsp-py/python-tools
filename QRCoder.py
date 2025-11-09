import io
import qrcode
import qrcode.image.svg as svg
import numpy as np
import math
import io

class QRCoder():
    def __init__(self):
        # default value for number of code lines per each SVG file.
        self.line_max = 50
    
    # @classmethod --> what's the heck is this in bloody Python???
    def encode(self, fileName):
        f = io.open(fileName, mode="r", encoding="utf-8")
        fileText = f.readlines()
        line_count = len(fileText)
        
        # number of code chunks (SVG files)
        chunks = np.array_split(fileText, math.ceil(line_count/self.line_max))

        i=0
        for chunk in chunks:
            if len(chunks) > 1:
                img = qrcode.make("".join(chunk), image_factory=svg.SvgImage)
                img.save("{0}.{1}.svg".format(fileName,i))
                i+=1
            else:
                img = qrcode.make("".join(chunk), image_factory=svg.SvgImage)
                img.save("{0}.svg".format(fileName))

    def decode(self, filname):
        raise Exception("This method hasn't been implemented yet")

qr = QRCoder()
qr.encode("readme.md")
# qr.decode("readme.svg")

print("All done")
