import base64


# more info here https://www.tutorialsteacher.com/python/python-read-write-file

def encode_pdf(path):
    # very imortant to read the file in binary format
    f = open(path, 'rb')
    data = base64.b64encode(f.read())
    f.close()
    return data


def decode_pdf(base64_data, path):
    # very imortant to write the file in binary format
    f = open(path, 'wb')
    f.write(base64.b64decode(base64_data))
    f.close()


# encoded base64 string
base64_pdf = encode_pdf('./original.pdf')

# decode and rewrite file
decode_pdf(base64_pdf, './decoded.pdf')
