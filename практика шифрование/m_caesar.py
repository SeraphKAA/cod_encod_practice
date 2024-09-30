def Encode_caesar(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('а') if char.islower() else ord('А')
            shifted_char = chr((ord(char) - start + shift) % 32 + start)
        else:
            shifted_char = char
        result += shifted_char

    return result



def Decode_caesar(orig_text, shift):
    res = ''
    for symbol in orig_text:
        if symbol.isalpha():
            start_of_alphabet = ord('а') if symbol.islower() else ord('А')
            enc_text = ord(symbol) - shift
            if enc_text < start_of_alphabet:
                enc_text += 32
            res += chr(enc_text)
        else:
            res += symbol

    return res




print("caesar is active")
