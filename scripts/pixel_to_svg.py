#!/usr/bin/env python3
"""
Convert pixel art PNG to optimized SVG using floodfill region detection.
Groups connected same-color pixels into single path elements.
"""

import sys
from PIL import Image
from pathlib import Path


def pixel_art_to_svg(img_path: str) -> str:
    img = Image.open(img_path).convert('RGBA')
    w, h = img.size
    pixels = img.load()
    visited = set()
    paths = []

    for y in range(h):
        for x in range(w):
            if (x, y) in visited:
                continue

            color = pixels[x, y]
            # Skip fully transparent pixels
            if color[3] == 0:
                visited.add((x, y))
                continue

            # Floodfill to find all connected pixels of this color
            region = []
            stack = [(x, y)]
            while stack:
                px, py = stack.pop()
                if (px, py) in visited:
                    continue
                if not (0 <= px < w and 0 <= py < h):
                    continue
                if pixels[px, py] != color:
                    continue

                visited.add((px, py))
                region.append((px, py))
                stack.extend([(px+1, py), (px-1, py), (px, py+1), (px, py-1)])

            if not region:
                continue

            # Convert region to path data (1x1 rect per pixel)
            rects = ''.join(f'M{px},{py}h1v1h-1z' for px, py in region)

            r, g, b, a = color
            if a == 255:
                fill = f'#{r:02x}{g:02x}{b:02x}'
            else:
                fill = f'rgba({r},{g},{b},{a/255:.2f})'

            paths.append(f'<path fill="{fill}" d="{rects}"/>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" shape-rendering="crispEdges">
{"".join(paths)}
</svg>'''
    return svg


def main():
    if len(sys.argv) < 2:
        print("Usage: pixel_to_svg.py <input.png> [output.svg]")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix('.svg')

    svg_content = pixel_art_to_svg(str(input_path))
    output_path.write_text(svg_content)
    print(f"Created {output_path}")


if __name__ == '__main__':
    main()
