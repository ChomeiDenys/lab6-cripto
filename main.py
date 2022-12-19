import functools

LENGTH = 8
UNREDUCED = "00011011"

def _prepare(byte):
    int_represent = int(byte, 16)
    binary_reprecent = format(int_represent, 'b').zfill(LENGTH)
    return binary_reprecent

def xor(binary_represent_1, binary_represent_2):
    return [str(int(bit_1, 2) ^ int(bit_2, 2)) for bit_1, bit_2 in zip(binary_represent_1, binary_represent_2)]

def convert_binary_array(binary_arr):
    return hex(int("".join(binary_arr), 2))

def mul02(byte):
    binary_reprary_init = _prepare(byte)
    binary_reprary = binary_reprary_init[1:] + '0'
    if binary_reprary_init[0] == '1':
        binary_reprary = xor(binary_reprary, UNREDUCED)

    mul_result = convert_binary_array(binary_reprary)
    return mul_result

def mul03(byte):
    mul_2 = _prepare(mul02(byte))
    byte_binary = _prepare(byte)
    return convert_binary_array(xor(mul_2, byte_binary))

def mul_any_bytes(p1, p2):
    p1_binary = _prepare(p1)
    p2_binary = _prepare(p2)

    iterations = 7 - [int(i) for i, bit in enumerate(p1_binary) if bit == "1"][0]
    powers_inds = [int(i) - 1 for i, bit in enumerate(reversed(p1_binary)) if bit == "1"]
    powers = [p2_binary] if -1 in powers_inds else []

    for i in range(iterations):
        p2_hex = mul02(p2)
        p2 = p2_hex
        if i in powers_inds:
            powers.append(_prepare(p2))

    return convert_binary_array(functools.reduce(lambda x, y: xor(x, y), powers))

if __name__ == "__main__":
    print("=================")
    print(f"02 * 0xd4 = {mul02('0xd4')}")
    print("=================")
    print(f"03 * 0xbf = {mul03('0xbf')}")
    print("=================")
