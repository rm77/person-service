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


Untuk mematikan container
root@royyana-desktop:~/komputasi_awan/person-service# docker rm -f person1
person1
root@royyana-desktop:~/komputasi_awan/person-service# docker rm -f person2
person2



Untuk menghapus image 
root@royyana-desktop:~/komputasi_awan/person-service# docker rmi -f person_service
Untagged: person_service:latest
Deleted: sha256:f6230da4de79510a4686754760e305678e609c80aa8660c2e51d37caea761b55
Deleted: sha256:6ce8bfaa306092e0a04ac0a869f962efd405ff5b6c8884ed4242cc48b014da2e
Deleted: sha256:c1bfd4421b60c9ee1df61ca0b27bf88c19fc70c5edb451ff3ea945864dded952
Deleted: sha256:c5294a8c298a595391c534389f20936f222bedfa2f4ca6a8dc8d86653bca8cfd
Deleted: sha256:c53bb35835101fbe5c2fc6b9dd525e361b830b15da8d1c3f8c911f36ed0c8cb2
Deleted: sha256:a6c32040bb8a94c14f4ae0d8f7f3746cbd3b19506c74c094a1277d43efd8e86a
Deleted: sha256:b2fcfadda7dc6d32bbe99f6b8d37eb46c2c91172969712105b7a8eb0712008aa
Deleted: sha256:ee472677962e57ddaf6f13644b429fd2cbf53b134d4ab55e2f73a15c9e966131
Deleted: sha256:ddb13c9ffb0e9e37e474f83eff96e5c8d374f6465837293ef44aa9ee412acb8e
Deleted: sha256:ab37253c5080ff6711757292bc9de8f48021236c891b9005ce2da840b4de2f3b
Deleted: sha256:a7449d2b07c24263dcbfe494401357cad1eeda17b0187d9b28907069f172e0b3
Deleted: sha256:4d6e2b7f010af035a1532c99a819b7056a528417d414c353a396413727bd69a0
Deleted: sha256:3f485cbbad079619ed9604aab34e9e8d6652c2414222cb707871a061320fe990
Deleted: sha256:9d64d0ad169c034068e8bc524afdf08d1b6c2a82810f06ee7f327c896a883596



- untuk membangun load balancer dengan reverse proxy

cd reverseproxy
docker build -t nginx-reverseproxy .


- jalankan reverse proxy
docker run -d -p 9999:8080 --name reverse nginx-reverseproxy

- reverseproxy akan berjalan di port9999
untuk mencoba
curl http://host:9999/version
{
    "info": "0.01"
}



- docker compose
docker-compose up -d

- untuk scale
docker-compose scale personservice=5

- untuk mematikan
docker-compose down
