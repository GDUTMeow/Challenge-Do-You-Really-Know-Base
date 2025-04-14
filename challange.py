import base2048


with open("output.txt", "wt", encoding="utf8") as f:
    f.write(base2048.encode("B4ptbxqMn4EcOHMAeOijraxLbldJMLsQiefbUhbgSTCzeGsYaUnvCTusPTfwStCmUn4u6wBpphJAy80HsLaryAbEkZ3aBreMcvNYfuI3J29v2jIT1kg1P6BHTI46C3sYYdX2vl8mvSfUzlyZVqzq8sBSuf7PSQlQdr9t3rlF9ZEAredQROSfxrnKNRocpqsCncOZJCOLz2Y0SJZTEBFeEdk0VHJzMjMWEqsmGb0xVRhlEGRzRX".encode()))
    
with open("output.txt", "rt", encoding="utf8") as f:
    data = f.read()
    decoded_data = base2048.decode(data)
    print(decoded_data.decode())