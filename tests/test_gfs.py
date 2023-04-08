from datetime import datetime, timezone

import pytest

from open_wx_data.gfs import build_s3_prefix, calc_latest_possible_run


@pytest.mark.parametrize(
    "model_run,expected",
    [
        (
            datetime(year=2021, month=1, day=1, hour=0, tzinfo=timezone.utc),
            "gfs.20210101/00/atmos/gfs.t00z.pgrb2.0p25",
        ),
        (
            datetime(year=2021, month=1, day=1, hour=6, tzinfo=timezone.utc),
            "gfs.20210101/06/atmos/gfs.t06z.pgrb2.0p25",
        ),
    ],
)
def test_build_s3_prefix(model_run, expected):
    assert build_s3_prefix(model_run) == expected


@pytest.mark.parametrize(
    ("now", "expected"),
    [
        (
            datetime(2020, 3, 1, 12, tzinfo=timezone.utc),
            datetime(2020, 3, 1, 6, tzinfo=timezone.utc),
        ),
        (
            datetime(2020, 3, 1, 13, tzinfo=timezone.utc),
            datetime(2020, 3, 1, 6, tzinfo=timezone.utc),
        ),
        (
            datetime(2020, 3, 1, 14, tzinfo=timezone.utc),
            datetime(2020, 3, 1, 12, tzinfo=timezone.utc),
        ),
    ],
)
def test_calc_latest_possible_run(now: datetime, expected: datetime) -> None:
    """Test calc_latest_possible_run."""
    assert calc_latest_possible_run(now=now) == expected
