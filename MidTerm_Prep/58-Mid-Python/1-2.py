encoded = input()
if len(encoded) == 64: # str64
    print(encoded[8]+encoded[22]+encoded[34]+encoded[49])
elif len(encoded) == 128:
    a = int(encoded[3]+encoded[101]+encoded[24]+encoded[32])
    b = int(encoded[56]+encoded[89]+encoded[92]+encoded[12])
    print((a+b)//2)
