#!/usr/bin/env python
import barcodegen

barcode = barcodegen.Ean13('1234567890128')
print(barcode.verifyChecksum())
barcode.drawImage()

barcode2 = barcodegen.Ean14('30012345678906')
print(barcode2.verifyChecksum())
barcode2.drawImage()