import io
import qrcode
import numpy as np
import math

from qrcode.image.svg import SvgImage

class QRCoder():
    
    line_max = 50
    
    @classmethod
    def encode(cls, file_name:str) -> None:
        f = io.open(file_name, mode="r", encoding="utf-8")
        file_text:list[str] = f.readlines()
        line_count:int = len(file_text)
        
        chunks:list = np.array_split(file_text, math.ceil(line_count / cls.line_max))

        if len(chunks) == 0:
            raise Exception("Nothing to encode!")

        elif len(chunks) == 1:
            img:SvgImage = qrcode.make("".join(chunks[0]), image_factory=SvgImage)
            img.save(f"{file_name}.svg")

        else:
            for i in range(len(chunks)):
                img:SvgImage = qrcode.make("".join(chunks[i]), image_factory=SvgImage)
                img.save(f"{file_name}.{i}.svg")

    @classmethod
    def decode(cls, file_name:str) -> None:
        raise Exception("This method hasn't been implemented yet")

QRCoder.encode("readme.md")
# QRCoder.decode("readme.svg")

print("All done")
