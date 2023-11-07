from textwrap import wrap


def get_ipv4_as_hex_little_endian(ipv4_str: str) -> str:
    result = ''
    decimal_list = ipv4_str.split(".")
    if len(decimal_list) != 4:
        raise Exception("Incorrect IP format: an ipv4 address should contain 4 decimal numbers seperated by a '.'")
    for d in decimal_list:
        decimal = int(d)
        if decimal >= 0 and decimal <= 255:
            hex_str = hex(decimal).replace('0x', '')
            if (len(hex_str) == 1):
                hex_str = '0' + hex_str
            result = hex_str + result
    return '0x' + result


def get_port_as_hex_little_endian(port_str: str) -> str:
    result = ''
    hex_str = hex(int(port_str)).replace('0x', '')
    hex_list = wrap(hex_str, 2)
    for h in hex_list:
        hex_number = h
        if len(hex_number) == 1:
            hex_number = '0' + hex_number
        result = hex_number + result
    return '0x' + result
