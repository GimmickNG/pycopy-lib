#!/usr/bin/env pycopy
#
# Script to install modules from pycopy-lib tree locally.
#
# This module is part of pycopy-lib https://github.com/pfalcon/pycopy-lib
# project.
#
# Copyright (c) 2019 Paul Sokolovsky
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import shutil
from pathlib import Path

# First check for installability - paths which don't here, aren't even reported.
skip_names = [i.name for i in Path(".").resolve().glob("*.py")]
def should_skip(f):
    return f.name in skip_names

def should_install_1(f):
    return ("test" not in f.name and f.name != "setup.py" and "testdata" not in f.as_posix() and "/_/" not in f.as_posix())

# Second check for installability
def should_install_2(f):
    return not (f.is_symlink() or "/example" in f.as_posix() or "/test_" in f.as_posix() or "/_tool_" in f.as_posix())

mod = Path(sys.argv[1].rstrip("/"))
dest_dir = Path(sys.argv[2]).expanduser()

for path in mod.rglob("*.py"):
    if should_skip(path) or not (should_install_1(path) and should_install_2(path)):
        continue

    dest = dest_dir / path.relative_to(path.parent.parent)
    if dest.parent.name == dest.with_suffix('').name:
        dest = dest.with_name("__init__.py")
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path.as_posix(), dest.as_posix())
