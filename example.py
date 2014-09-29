#!/usr/bin/env python
import barcodegen

barcode = barcodegen.Ean13('1234567890128')
print(barcode.verifyChecksum())
barcode.drawImage()