"""# Get Matched Files V1.1
get_matched_files() go through all the subdirectories (limited by depth),
and return a list of matched files.
The element in the list is full path (e.g C:\\My Folder\\ABC.txt, with only one backslash).
root_dir example: "E:/OneDrive/My_Documents/Study/Python Programs"
    * Single backslash instead of a slash (/) is also allowed.
pattern_string example: "*.py; *.ui; *.png; *.jpg; *.ico; *.mdp"

V1.0
- Initial creation

V1.1
- Add pattern_string_ex to exclude files
"""
import glob
import os


def get_matched_files(root_dir: str, pattern_string: str, pattern_ex_string: str, depth=99) -> list:
    root_dir = root_dir.replace("/", "\\")

    # Set patterns (a list)
    pattern_temp = [pattern.strip() for pattern in pattern_string.split(";")]
    patterns = []
    for pattern in pattern_temp:
        if len(pattern) > 1:
            patterns.append(pattern)

    # Set patterns to exclude (a list)
    pattern_temp_ex = [pattern_ex.strip() for pattern_ex in pattern_ex_string.split(";")]
    patterns_ex = []
    for pattern_ex in pattern_temp_ex:
        if len(pattern_ex) > 1:
            patterns_ex.append(pattern_ex)

    # Define how much level go down to subdirectories.
    root_level = root_dir.count("\\")
    max_level = root_level + depth

    # Walk through the directory tree
    matched_files = []
    matched_files_ex = []
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

        # Get matches_ex
        for pattern_ex in patterns_ex:
            full_pattern_ex = os.path.join(root, pattern_ex)
            current_matches_ex = glob.glob(full_pattern_ex)

            if len(current_matches_ex) > 0:
                matched_files_ex.append(current_matches_ex)

    # Make nested list to simple list
    match_list = []
    for matches in matched_files:
        for match in matches:
            match_list.append(match)

    # Make nested list to simple list
    match_list_ex = []
    for matches_ex in matched_files_ex:
        for match_ex in matches_ex:
            match_list_ex.append(match_ex)

    # Exclude and make unique list
    unique_matched = list(set(match_list) - set(match_list_ex))
    return unique_matched

if __name__ == "__main__":
    matches = get_matched_files(
        r"E:\OneDrive\My_Documents\Study\Python Programs",
        r"*.py;*.ui",
        "*.py",
        depth=2)
    for match in matches:
        print(match)
    print(len(matches))
