
https://docs.docker.com/get-started/part4/

siapkanlah dua node NODE1 dan NODE2

NODE1
docker swarm init --advertise-addr <node1 ip>
Swarm initialized: current node <node ID> is now a manager.

To add a worker to this swarm, run the following command:

  docker swarm join \
  --token <token> \
  <myvm ip>:<port>

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

NODE2
  docker swarm join \
  --token <token> \
 <node1  ip>:<port>


pada konfigurasi ini NODE2 adalah workder bagi NODE1 yang merupakan manager dari swarm


ceklah node yang akan terlibat

docker node ls


masuklah pada NODE1

git clone https://github.com/rm77/person-service.git
cd person-service
git checkout  swarm_version

lihatlah config pada docker-compose.yml
deploylah service pada swarm

docker stack deploy -c docker-compose.yml personservice

lihatlah status dari service dgn

docker stack ps personservice

untuk melihat apakah workder bekerja

pindahlah ke node2
jalankan:

docker ps --all

akan terlihat proses yang berjalan

