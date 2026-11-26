"""Entry for make.fun news-image-20261126.

Sums up the world news of Thursday 26 November 2026 in one image:
a front-page style illustration with six panels (US tariffs on 14
nations, Ukraine's strike on a Russian air base, Kim Jong Un's call
for wider tactical nuclear deployment, the Cairo fuel-tanker fire,
doubt over Netanyahu's bribery charge, and the postponed Macy's
Thanksgiving Day Parade), headed by the date it sums up.

The image is generated once and shipped in this repository as
entry.png; the program copies it to the output directory, which is
the simplest reliable entry the rules allow (the program runs with
no network). Before writing it out, the program re-checks the
gate limits itself: at most 1 MiB and at most 1024 by 1024 pixels,
reading the dimensions straight from the file's own header with
only the standard library.
"""

import os
import shutil
import struct

MAX_BYTES = 1048576
MAX_DIM = 1024


def image_size(path):
    """Return (width, height) for a PNG or JPEG file, stdlib only."""
    with open(path, "rb") as f:
        head = f.read(32)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        width, height = struct.unpack(">II", head[16:24])
        return width, height
    if head[:2] == b"\xff\xd8":
        with open(path, "rb") as f:
            data = f.read()
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                height, width = struct.unpack(">HH", data[i + 5:i + 9])
                return width, height
            length = struct.unpack(">H", data[i + 2:i + 4])[0]
            i += 2 + length
    raise ValueError("not a PNG or JPEG file")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")

    size = os.path.getsize(src)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB limit")
    width, height = image_size(src)
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit(f"entry.png is {width}x{height}, over 1024x1024")

    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({size} bytes, {width}x{height})")


if __name__ == "__main__":
    main()
