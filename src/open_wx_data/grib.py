from collections import defaultdict


def parse_idx(idx: str) -> dict:
    # idx format: 1:0:d=2023040812:PRMSL:mean sea level:anl:

    idx_dict = defaultdict(lambda: defaultdict(dict))
    prev_start_byte = None
    for line in reversed(idx.splitlines()):
        _, start_byte, _, param, level, _ = line.rstrip(":").split(":")
        start_byte = int(start_byte)
        idx_dict[param][level]["byte_range"] = (start_byte, prev_start_byte)
        prev_start_byte = start_byte
    return idx_dict


