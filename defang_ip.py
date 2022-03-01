def defang_ip(ip):
    new_address=""
    split_address=ip.split(".")
    separator="[.]"
    new_address=separator.join(split_address)
    return new_address