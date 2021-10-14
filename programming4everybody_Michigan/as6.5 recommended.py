text = "X-DSPAM-Confidence:    0.8475   ";
ipos=text.find(':')
piece = text[ipos+1:]
value = float(piece)
print(value)
