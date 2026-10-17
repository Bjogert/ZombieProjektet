"""Translate original garden layout data into ground-level WorldEd layers."""
import re


def garden_layers(template, origin, size=300):
    """Return new layers; reject placements that obstruct the house or access."""
    if len(origin) != 2 or any(type(v) is not int for v in origin):
        raise ValueError('Garden origin must contain two integers')
    house = template['house_size']
    if len(house) != 2 or any(type(v) is not int or v < 1 for v in house):
        raise ValueError('Garden house_size must contain two positive integers')
    ox, oy = origin
    if not (0 <= ox < ox + house[0] <= size and 0 <= oy < oy + house[1] <= size):
        raise ValueError('House outside the authoring cell')

    def squares(rect):
        if len(rect) != 4 or any(type(v) is not int for v in rect):
            raise ValueError('Garden rectangle must contain four integers')
        x, y, w, h = rect
        if not (w > 0 and h > 0 and 0 <= ox + x < ox + x + w <= size
                and 0 <= oy + y < oy + y + h <= size):
            raise ValueError('Garden rectangle outside the authoring cell or empty')
        return [(x + dx, y + dy) for dy in range(h) for dx in range(w)]

    routes = {point for rect in template['clear_routes'] for point in squares(rect)}
    layers = {name: [None] * size ** 2 for name in ('0_Floor', '0_Furniture')}
    for patch in template['patches']:
        layer, tile = patch['layer'], patch['tile']
        if layer not in layers:
            raise ValueError(f'Unsupported garden layer: {layer}')
        if (len(tile) != 2 or not isinstance(tile[0], str)
                or not re.fullmatch(r'[A-Za-z0-9_]+', tile[0])
                or type(tile[1]) is not int or tile[1] < 0):
            raise ValueError(f'Invalid garden tile reference: {tile}')
        for x, y in squares(patch['rect']):
            if 0 <= x < house[0] and 0 <= y < house[1]:
                raise ValueError('Garden overlaps the house')
            if layer != '0_Floor' and (x, y) in routes:
                raise ValueError('Garden object obstructs a reserved route')
            index = (oy + y) * size + ox + x
            if layers[layer][index] is not None:
                raise ValueError('Overlapping garden patches on the same layer')
            layers[layer][index] = tuple(tile)
    return layers
