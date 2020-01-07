# base64 encoding/decoding example for PDF files 

## Notes:
- Use Python 3+ 

- the base64 package is a built-in package

```python

# encoded base64 string
base64_pdf = encode_pdf('./original.pdf') # expects the path of the original file

# decode and rewrite file
decode_pdf(base64_pdf, './decoded.pdf') # expects a base64 string and the path for the new file

```

#### change the file paths before running the script
```bash

python script.py

```
