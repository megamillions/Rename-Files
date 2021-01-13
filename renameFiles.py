#! python3 - renameFiles.py
# Rename files in current directory to specified format.

import os, re

files = os.listdir()

# Edit extension as needed.
file_format = '.pdf'

for file in files:
	if file[-4:] == file_format:

		old_name_raw = file[:-4]

		# Month-day-year.
		m, d, y = re.split('_|-', old_name_raw)

		# Edit flavor text as needed.
		new_name = 'Flavor %s-%s-%s.pdf' % (y, m, d)

		os.rename(file, new_name)

		print('File formerly known as %s has successfully been renamed to %s.'
		      % (file, new_name))