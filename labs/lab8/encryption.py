def encode(sent, key_val):
    acc = ''

    for ch in sent:
        enc_ch = ord(ch) + key_val
        uncoded_ch = chr(enc_ch)
        acc = acc + uncoded_ch
    return acc

def encode_better(sent, key):
    acc = ''

    for i in range(len(sent)):
        encod_ch = ord(sent[i])
        encod_key = ord(key[i % len(key)])
        x = encod_ch + encod_key - 97
        acc = acc + chr(x)
    return acc
