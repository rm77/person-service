REDISSERVERCONTAINER=redis_server
POOL=$(sudo docker inspect $(sudo docker-compose ps -q personservice) -f '{{.NetworkSettings.Networks.personservice_default.IPAddress}}:5000')
i=1
for rc in $POOL
do
	echo $rc
	cmd="set upstreamhost_$i $rc"
	sudo docker exec -ti redis_server redis-cli -h redis_server $cmd
	i=$((i+1))
done
sudo docker exec -ti balancer sh /tmp/update_upstream.sh
sudo docker-compose restart reverseproxy
