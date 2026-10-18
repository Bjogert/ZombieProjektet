"""Resize the original west-entry cottage's authored layout, never its artwork."""
import argparse
import copy
from pathlib import Path
import xml.etree.ElementTree as ET


def grid(width, height, value):
    return '\n' + ',\n'.join(','.join(str(value(x, y)) for x in range(width))
                             for y in range(height)) + '\n'


def resize_roof(root, upper, width, height):
    roof = upper.find("object[@type='roof']")
    roof.set('width', str(width))
    roof.set('height', str(height))
    if width == 6:
        return
    # The old steep peak flattens beyond six squares. Stock 30-degree slopes
    # cover up to six squares per side; odd widths use a one-square ridge.
    caps = root.find("tile_entry[@category='roof_caps']")
    slopes = root.find("tile_entry[@category='roof_slopes']")
    for i in range(1, 7):
        for direction, base, step in (('RiseE', 0, 1), ('FallE', 13, -1),
                                      ('RiseS', 16, 1), ('FallS', 29, -1)):
            ET.SubElement(caps, 'tile', enum=f'CapSlope30{direction}{i}',
                          tile=f'walls_exterior_roofs_30_17_{base + (i - 1) * step:03}')
        for direction, base in (('E', 32), ('S', 40)):
            ET.SubElement(caps, 'tile', enum=f'CapPeak30{direction}{i}',
                          tile=f'walls_exterior_roofs_30_17_{base + i - 1:03}')
        for direction, base, step in (('W', 16, 1), ('E', 13, -1)):
            ET.SubElement(slopes, 'tile', enum=f'Slope30{direction}{i}',
                          tile=f'roofs_30_01_{base + (i - 1) * step:03}')
        ET.SubElement(slopes, 'tile', enum=f'Peak30WE{i}',
                      tile=f'roofs_30_01_{110 - i:03}')
    roof.set('Depth', 'Zero')
    if width % 2:
        roof.set('RoofType', 'Peak30NS')
    else:
        roof.set('RoofType', 'Slope30W')
        roof.set('width', str(width // 2))
        roof.set('cappedE', 'false')
        other = copy.deepcopy(roof)
        other.set('RoofType', 'Slope30E')
        other.set('x', str(width // 2))
        other.set('cappedW', 'false')
        other.set('cappedE', 'true')
        upper.insert(list(upper).index(roof) + 1, other)


def generate(source, width, height):
    if type(width) is not int or type(height) is not int or not (6 <= width <= 12 and 9 <= height <= 18):
        raise ValueError('Supported cottage width 6-12, length 9-18 whole squares')
    root = ET.fromstring(source)
    if (root.tag != 'building' or root.get('width') != '6' or root.get('height') != '10'
        or len(root.findall('room')) != 3 or len(root.findall('floor')) != 2):
        raise ValueError('Expected the original three-room 6 by 10 cottage')
    root.set('width', str(width))
    root.set('height', str(height))
    front = height - max(3, round(height * .4))
    split = width - max(2, round(width / 3))
    ground, upper = root.findall('floor')
    objects = ground.findall('object')
    # Keep the original object types/tile references; only dimensions/positions change.
    positions = [
        (0, 3), (1, front), (width - 2, front),
        (0, 1), (0, front + 1), (width // 2, 0), (width, 2), (width, front + 1),
        (2, height), (width - 1, height),
        (0, 4), (2, front), (width - 1, front),
        (width // 2, 2), (width // 2, 4), (2, height - 2),
        (width - 3, 0), (width - 2, 0), (width - 1, 0),
        (width - 1, front), (width - 1, height - 2),
    ]
    expected_types = ['door'] * 3 + ['window'] * 7 + ['furniture'] * 11
    expected_furniture = ['0', '0', '0', '1', '2', '3', '4', '5', '6', '6', '7']
    if ([obj.get('type') for obj in objects] != expected_types
        or [obj.get('FurnitureTiles') for obj in objects[10:]] != expected_furniture
        or upper.find("object[@type='roof']") is None):
        raise ValueError('Unsupported cottage object layout')
    for obj, (x, y) in zip(objects, positions):
        obj.set('x', str(x))
        obj.set('y', str(y))
    ground.find('rooms').text = grid(
        width, height, lambda x, y: 1 if y < front else (2 if x < split else 3))
    corners = {(0, 0): 1, (width, 0): 3, (0, height): 3, (width, height): 2}
    ground.find("tiles[@layer='WallTrim']").text = grid(
        width + 1, height + 1, lambda x, y: corners.get((x, y), 0))
    upper.find('rooms').text = grid(width, height, lambda x, y: 0)
    upper.find("tiles[@layer='Floor']").text = grid(
        width + 1, height + 1, lambda x, y: 4 if x < width and y < height else 0)
    resize_roof(root, upper, width, height)
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=(
        Path(__file__).resolve().parents[1] / 'assets/buildings/swedish_cottage_01.tbx'))
    parser.add_argument('--width', type=int, required=True)
    parser.add_argument('--height', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        data = generate(args.source.read_bytes(), args.width, args.height)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('xb') as file:
            file.write(data)
        print('Cottage variant written; official export and game verification required.')
    except (OSError, ValueError) as error:
        parser.error(str(error))
