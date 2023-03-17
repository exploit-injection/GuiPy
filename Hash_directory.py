import hashlib
from os import listdir

dir_hash = ''
for f in listdir('/home/spi_729-1/Документы/Test/'):
    with open('/home/spi_729-1/Документы/Test/'+f, "rb") as f:
        file_hash = hashlib.sha256()  # Создаем объект хеша
        while chunk := f.read(8192):
            file_hash.update(chunk)

            dir_hash += file_hash.hexdigest()

print(hashlib.sha256(dir_hash.encode('latin_1')).hexdigest())
