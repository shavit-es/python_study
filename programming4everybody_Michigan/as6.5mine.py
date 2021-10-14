text = "X-DSPAM-Confidence:    0.8475";
start=text.find(':')
value=text[start+1:].strip()
value=float(value)
print(value)
