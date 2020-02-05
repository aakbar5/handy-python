""" Scan a folder to get list of all or specific files """

import os

def scan_folder(folder, file_exts):
	found_files = []

	if not os.path.exists(folder):
		return found_files

	with os.scandir(folder) as iterator:
		for entry in iterator:
			if entry.is_file() and os.path.splitext(entry.path)[1] in file_exts:
				found_files.append(entry.path)
			elif entry.is_dir(follow_symlinks=False):
				found_files += scan_folder(entry.path, file_exts)

	return found_files

print("Search a folder for file...")
files = scan_folder("/path/to/folder/to/search", ['.jpg', '.jpeg'])
for f in files:
	print(f)
