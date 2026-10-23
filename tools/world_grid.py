"""Creator-approved 45-degree Getaboda grid, one square per metric metre.

Source coordinates stay unchanged. Translation is recorded by the caller;
rounding belongs to a separate footprint/road adaptation step.
"""
import math


def pair(value):
    if (not isinstance(value, (list, tuple)) or len(value) != 2
        or any(type(v) not in (int, float) or not math.isfinite(v) for v in value)):
        raise ValueError('Expected a pair of finite coordinates')
    return value


def to_grid(point, origin, *, offset=(0, 0)):
    east, north = pair(point)
    origin_east, origin_north = pair(origin)
    offset_x, offset_y = pair(offset)
    east, north = east - origin_east, north - origin_north
    return ((east - north) / math.sqrt(2) + offset_x,
            -(east + north) / math.sqrt(2) + offset_y)


def from_grid(point, origin, *, offset=(0, 0)):
    x, y = pair(point)
    origin_east, origin_north = pair(origin)
    offset_x, offset_y = pair(offset)
    x, y = x - offset_x, y - offset_y
    return ((x - y) / math.sqrt(2) + origin_east,
            -(x + y) / math.sqrt(2) + origin_north)
