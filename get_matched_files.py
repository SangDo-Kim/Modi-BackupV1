"""# Get Matched Files V1.0
get_matched_files() go through all the subdirectories (limited by depth),
and return a list of matched files.
The element in the list is full path (e.g C:\\My Folder\\ABC.txt, with only one backslash).
root_dir example: "E:/OneDrive/My_Documents/Study/Python Programs"
    * Single backslash instead of a slash (/) is also allowed.
pattern_string example: "*.py; *.ui; *.png; *.jpg; *.ico; *.mdp"
"""
import glob
import os


def get_matched_files(root_dir: str, pattern_string: str, depth=99) -> list:
    root_dir = root_dir.replace("/", "\\")

    # Set patterns (a list)
    pattern_temp = [pattern.strip() for pattern in pattern_string.split(";")]
    patterns = []
    for pattern in pattern_temp:
        if len(pattern) > 1:
            patterns.append(pattern)

    # Define how much level go down to subdirectories.
    root_level = root_dir.count("\\")
    max_level = root_level + depth

    # Walk through the directory tree
    matched_files = []
    for root, dirs, _ in os.walk(root_dir):
        # Limit level
        current_level = root.count("\\")
        if current_level > max_level:
            continue

        # Get matches
        for pattern in patterns:
            full_pattern = os.path.join(root, pattern)
            current_matches = glob.glob(full_pattern)
            if len(current_matches) > 0:
                matched_files.append(current_matches)

    # Make nested list to simple list
    match_list = []
    for matches in matched_files:
        for match in matches:
            match_list.append(match)

    # Get unique list
    unique_matched = list(set(match_list))
    return unique_matched

if __name__ == "__main__":
    matches_all = count_matched_files()
    for match in matches_all:
        print(match)
    print(len(matches_all))