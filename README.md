# person-service
project praktikum MK komputasi awan , dep informatika 2018 gasal

uuid:
-- pip install uuid

pickledb:
-- pip install pickledb

flask:
-- pip install flask

flask_restful
-- pip install flask_restful

run service dengan :
python Service.py


atau lihat file requirements.txt
instalasi dependensi dengan pip install -r requirements.txt


Persons.py

merupakan implementasi data model yang berhubungan dengan class Person

Service.py

merupakan interface antara data model kepada user dengan mengimplementasikan REST interface
terdapat dua class yang digunakan untuk melayani user yaitu personlist dan person
masing masing diidentifikasi dengan memanggil /personlist dan /person/<id>


untuk mencoba, jalankan service dengan 

python Service.py

akan menjalankan service di localhost pada port 5000
gunakan command curl

- untuk mendapatkan data dari db
curl http://localhost:5000/personlist

Royyanas-MacBook-Pro:komputasi_awan royyana$ curl http://localhost:5000/personlist
{
    "e44c5fb3-cb43-11e8-bc5f-c4b301d9a59b": {
        "alamat": "Ketintang",
        "nama": "Royyana"
    },
    "e44e4e8a-cb43-11e8-a476-c4b301d9a59b": {
        "alamat": "SMP 6",
        "nama": "Ananda"
    },
    "e44e6f94-cb43-11e8-8732-c4b301d9a59b": {
        "alamat": "TK Perwanida",
        "nama": "Ibrahim"
    },
    "e44e8cb0-cb43-11e8-a44e-c4b301d9a59b": {
        "alamat": "SD Alfalah Surabaya",
        "nama": "Azam"
    }
}

- untuk mendapatkan detil dari record
Royyanas-MacBook-Pro:komputasi_awan royyana$ curl http://localhost:5000/person/e44e6f94-cb43-11e8-8732-c4b301d9a59b
{
    "alamat": "TK Perwanida",
    "nama": "Ibrahim"
}


- untuk menambah data 
royyana@royyana-desktop:~$ curl  http://127.0.0.1:5000/personlist -X POST -d 'data={ "nama": "John 4"}'
{
    "uid": "7c0c2284-d417-11e8-82c8-f44d306426ad"
}
