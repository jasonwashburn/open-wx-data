import pytest

from open_wx_data.grib import parse_idx


@pytest.fixture
def idx_file():
    idx_file = """1:0:d=2023040812:PRMSL:mean sea level:anl:
2:1005022:d=2023040812:CLMR:1 hybrid level:anl:
3:1115513:d=2023040812:ICMR:1 hybrid level:anl:
4:1378411:d=2023040812:RWMR:1 hybrid level:anl:
5:1605522:d=2023040812:SNMR:1 hybrid level:anl:
"""
    return idx_file


def test_parse_idx_file(idx_file):
    assert parse_idx(idx=idx_file) == {
        "PRMSL": {"mean sea level": {"byte_range": (0, 1005022)}},
        "CLMR": {"1 hybrid level": {"byte_range": (1005022, 1115513)}},
        "ICMR": {"1 hybrid level": {"byte_range": (1115513, 1378411)}},
        "RWMR": {"1 hybrid level": {"byte_range": (1378411, 1605522)}},
        "SNMR": {"1 hybrid level": {"byte_range": (1605522, None)}},
    }
