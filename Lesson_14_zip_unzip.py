f = open('fileone.txt','w+')
f.write('One File')
f.close()

f = open('filetwo.txt','w+')
f.write('Two File')
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')

comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


# to extract

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')

import shutil

dir_to_zip = '/home/threat_hunter/Desktop/python_practice/oop/advance/extracted_content'

output_file = 'example'

shutil.make_archive(output_file,'zip',dir_to_zip)

shutil.unpack_archive('example.zip','final_unzip','zip')
