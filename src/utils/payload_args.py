def parse_payload_args(args: str) -> dict:
    result = {}
    splitted = args.split(",")
    for a in splitted:
        s = a.split("=")
        key = s[0]
        value = s[1]
        result[key] = value
    return result
