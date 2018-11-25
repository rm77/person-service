
deployment menggunakan docker-compose 

1. build lah masing-masing container image di masing-masing folder seperti yang terlihat di tobuild.txt

cd person-service-container
docker build -t person_service .
cd ..
cd reverseproxy
docker build -t nginx-reverseproxy .
cd ..

konfigurasi ini menggunakan redis sebagai central config yang bertugas untuk menyimpan info tentang cluster container
yang berjalan. hal ini karena nginx sebagai balancer tidak dapat mengupdate info tentang cluster secara otomatis. oleh karena
itu dalam konfigurasi ini disiapkan program update_ip_pool.sh sebagai otomasi untuk mengupdate info cluster pada balancer nginx



2. jalankan service dengan menjalankan docker-compose up -d

sudo docker-compose up -d
sh update_ip_pool.sh

pada awalnya personservice hanya akan dijalankan 1 instance container saja,
jalankan update_ip_pool.sh untuk mengupdate informasi cluster dari personservice

tes dengan curl, misalkan ip address nya adalah 192.168.100.19 maka

curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.2  Bcast:192.168.31.255  Mask:255.255.240.0\n"}


3. menambah jumlah service personservice untuk load balancing

$sudo docker-compose scale personservice=10

Starting personservice_personservice_1 ... done
Creating personservice_personservice_2  ... 
Creating personservice_personservice_3  ... 
Creating personservice_personservice_4  ... 
Creating personservice_personservice_5  ... 
Creating personservice_personservice_6  ... 
Creating personservice_personservice_7  ... 
Creating personservice_personservice_8  ... 
Creating personservice_personservice_9  ... 
Creating personservice_personservice_10 ... 
Creating personservice_personservice_2  ... done
Creating personservice_personservice_3  ... done
Creating personservice_personservice_4  ... done
Creating personservice_personservice_5  ... done
Creating personservice_personservice_6  ... done
Creating personservice_personservice_7  ... done
Creating personservice_personservice_8  ... done
Creating personservice_personservice_9  ... done
Creating personservice_personservice_10 ... done

$sh update_ip_pool.sh

192.168.16.2:5000
OK
192.168.16.12:5000
OK
192.168.16.5:5000
OK
192.168.16.6:5000
OK
192.168.16.7:5000
OK
192.168.16.8:5000
OK
192.168.16.10:5000
OK
192.168.16.11:5000
OK
192.168.16.9:5000
OK
192.168.16.13:5000
OK
Restarting balancer ... done

jika dijalankan lagi, maka cluster dan balancer akan menyesuaikan

royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.5  Bcast:192.168.31.255  Mask:255.255.240.0\n"}
royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.10  Bcast:192.168.31.255  Mask:255.255.240.0\n"}
royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.7  Bcast:192.168.31.255  Mask:255.255.240.0\n"}
royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.9  Bcast:192.168.31.255  Mask:255.255.240.0\n"}
royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.2  Bcast:192.168.31.255  Mask:255.255.240.0\n"}
royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.11  Bcast:192.168.31.255  Mask:255.255.240.0\n"}
royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ curl http://192.168.100.19:9999/version
{"info": "0.01", "ip": "          inet addr:192.168.16.6  Bcast:192.168.31.255  Mask:255.255.240.0\n"}
royyana@royyana-VPCCW18FJ:~/Downloads/komputasi_awan/person-service$ 

untuk melihat proses yang sedang berjalan gunakan

$sudo docker-compose ps

             Name                           Command               State               Ports             
--------------------------------------------------------------------------------------------------------
balancer                         nginx -g daemon off;             Up      80/tcp, 0.0.0.0:9999->8080/tcp
personservice_personservice_1    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_10   python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_2    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_3    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_4    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_5    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_6    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_7    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_8    python /usr/src/app/Service.py   Up      5000/tcp                      
personservice_personservice_9    python /usr/src/app/Service.py   Up      5000/tcp                      
redis_server                     docker-entrypoint.sh redis ...   Up      6379/tcp  




