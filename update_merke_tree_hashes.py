import os
import hashlib
import time
#import xxhash


def comma_separated_list(dir_sha1s):
    dir_sha1s.sort()
    return ",".join(dir_sha1s)


def get_current_sha1(file):
    if not os.path.exists(file):
        return ""
    with open(file, 'r') as f:
        return f.read()


def write_sha1_file(sha1, sha1_file):
    with open(sha1_file, 'w') as f:
        print("Updating: " + sha1_file)
        f.write(sha1)


def make_sha1(json):
#    return xxhash.xxh64(json.encode('ascii')).hexdigest()
    return hashlib.sha1(json.encode('ascii')).hexdigest()


def process_directory(dirname):
    dir_sha1s = []
    count = 0
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            sha1, ct = process_directory(path)
            dir_sha1s.append(sha1)
            count += ct
        else:
            if path.endswith(".json"):
                sha1_file = path + ".sha1"
                with open(path, 'r') as f:
                    json = f.read()
                sha1 = make_sha1(json)
                if sha1 != get_current_sha1(sha1_file):
                    count += 1
                    write_sha1_file(sha1, sha1_file)
                dir_sha1s.append(sha1)
    sha1 = make_sha1(comma_separated_list(dir_sha1s))
    sha1_file = os.path.join(dirname, ".sha1")
    if sha1 != get_current_sha1(sha1_file):
        count += 1
        write_sha1_file(sha1, sha1_file)
    return (sha1, count)


while True:

    start = time.time()
    sha1, count = process_directory("data")
    print("Updates: " + str(count) + ", root SHA1: " + sha1 + ", duration: " + str(round(time.time() - start, 1)) + "s")