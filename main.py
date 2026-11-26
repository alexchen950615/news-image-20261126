"""Entry for make.fun news-image-20261126.

Sums up the world news of Thursday 26 November 2026 in one image:
a front-page style illustration with six panels (US tariffs on 14
nations, Ukraine's strike on a Russian air base, Kim Jong Un's call
for wider tactical nuclear deployment, the Cairo fuel-tanker fire,
doubt over Netanyahu's bribery charge, and the postponed Macy's
Thanksgiving Day Parade), headed by the date it sums up.

The image is generated once and shipped in this repository as
entry.png; the program simply copies it to the output directory,
which is the simplest reliable entry the rules allow (the program
runs with no network).
"""

import os
import shutil


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
