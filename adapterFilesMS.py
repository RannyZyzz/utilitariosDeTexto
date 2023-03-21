import os
import codecs
import zipfile
import shutil
from pathlib import Path


dir_path = os.path.dirname(os.path.realpath(__file__))


#remove existing folder
deleteFolder = r'{0}/msConvert'.format(dir_path) 
if (os.path.exists(deleteFolder) == True):
    os.system("rm -rf "+ deleteFolder)

#create new folder
createFolder = r'{0}/msConvert'.format(dir_path) 
if not os.path.exists(createFolder):
    os.makedirs(createFolder)

# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

files=["GM_MS_ESPEC.CSV","GM_MS_PLANOS.CSV","GM_MS_CORPOCLI.CSV","GM_MS_HORARIOS.CSV","GM_MS_QUALIFICACAO.CSV","GM_MS_MEDICAMENTO.CSV","GM_MS_TPREDE.CSV","GM_MS_REDECRED.CSV"]

for file in files:

    # relative or absolute file path, e.g.:
    upperCaseFile = file.upper()
    file_path = r'{0}/{1}'.format(dir_path,upperCaseFile)

    # verify if file exists
    path = Path(file_path)
    if(path.is_file() == True):

        with open(file_path, 'rb') as open_file:
            content = open_file.read()

        # Windows ➡ Unix
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

        # Unix ➡ Windows
        # content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

        with open(file_path, 'wb') as open_file:
            open_file.write(content)


        BLOCKSIZE = 1048576 # or some other, desired size in bytes
        with codecs.open(file, "r", "ISO-8859-1") as sourceFile:
            with codecs.open('UTF8_'+file , "w", "utf-8") as targetFile:
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)

            with zipfile.ZipFile('UTF8_'+ file + '.zip', 'w') as jungle_zip:
                jungle_zip.write('UTF8_' + file, compress_type=zipfile.ZIP_DEFLATED)
        
        #move files to convertMS folder
        shutil.move(dir_path + '/UTF8_' + file + '.zip' , createFolder + '/UTF8_' + file + '.zip')
        
        #remove old files
        os.remove('UTF8_'+file)
