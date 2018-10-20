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


Dockerized version:

build image:
docker build -t person_service .

run image into container
-container 1
docker run -d --name person1 person_service
-container 2
docker run -d --name person2 person_service
-container 3
docker run -d --name person3 person_service



melihat container yang aktif
docker ps --all
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS               NAMES
55f234c9168d        person_service      "python /usr/src/a..."   4 seconds ago        Up 4 seconds        5000/tcp            person2
34a0e6d58c8a        person_service      "python /usr/src/a..."   About a minute ago   Up About a minute   5000/tcp            person1


masing-masing akan mempunyai ip address dan bertindak sebagai instance yang berdiri sendiri

untuk melihat ip address dari masing-masing container
 docker inspect --format "{{ .Id }} {{ .Name }} {{ .NetworkSettings.IPAddress }}" $(docker ps  -q)
55f234c9168d687b1e2641e4336484575c896157d2306a6f3ac6cc9bb655ff2f /person2 172.17.0.3
34a0e6d58c8af0337a6f9b2a32ae6d14399b498a58ef60208f03f5c5f630fc49 /person1 172.17.0.2

gunakan container person1 untuk mencoba service tsb
root@royyana-desktop:~# curl  http://172.17.0.2:5000/personlist -X POST -d 'data={ "nama" : "Mr John 3"}'
{
    "uid": "aa4325e1-d41b-11e8-864b-0242ac110002"
}
root@royyana-desktop:~# curl  http://172.17.0.2:5000/person/aa4325e1-d41b-11e8-864b-0242ac110002
{
    "nama": "Mr John 3"
}
root@royyana-desktop:~#
