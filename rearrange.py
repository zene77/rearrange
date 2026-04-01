#!/usr/bin/env python3
def rearrange_name(name):
    if "," not in name:
        return name.strip()
    last, first = name.split(",", 1)
    return f"{first.strip()} {last.strip()}"

