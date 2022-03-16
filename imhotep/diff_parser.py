from collections import namedtuple
    r"@@ \-(?P<removed_start>\d+),(?P<removed_length>\d+) "
    r"\+(?P<added_start>\d+),(?P<added_length>\d+) @@"
class Entry:
        if re.search(r"index \w+..\w+( \d)?", line):
        elif re.search(r"(-|\+){3} (a|b)?/.*", line):
        elif re.search("new file mode.*", line):
                line = line.decode("utf-8")
            match = re.search(
                r"diff .*a/(?P<origin_filename>.*) " r"b/(?P<result_filename>.*)", line
            )
                z = Entry(
                    match.group("origin_filename"), match.group("result_filename")
                )
                before_line_number = int(header.group("removed_start"))
                after_line_number = int(header.group("added_start"))
            if line.startswith("-"):
            elif line.startswith("+"):