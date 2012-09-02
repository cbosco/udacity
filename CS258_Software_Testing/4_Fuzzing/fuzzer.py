#!/usr/bin/python

file_list = [
    "text_only.md",
    "h1_h5.md",
    "list.md",
    "link.md",
    "image.md",
    "code.md"
    ]

# List of applications to test
apps = [
    "/Applications/Mou.app/Contents/MacOS/Mou",
    "mvim"
    ]

fuzz_output = "./tmp/fuzz_"
fuzz_save = "fuzz.md."

FuzzFactor = 250
num_tests = 10000

import math
import random
import string
import subprocess
import time
import os

crash_count = 0
random.seed(17)
for test_no in range(num_tests):
    file_choice = random.choice(file_list)
    app = random.choice(apps)

    buf = bytearray(open('./source/' + file_choice, 'rb').read())

    numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1

    for byte_no in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte)

	filename = fuzz_output + str(test_no) + '.md'
	open(filename, 'wb').write(buf)

	process = subprocess.Popen([app, filename])

    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate()
    else:
        open(fuzz_save + str(crash_count), 'wb').write(buf)
        crash_count += 1

    os.unlink(filename)
