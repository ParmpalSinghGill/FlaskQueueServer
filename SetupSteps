Install Redis

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04
sudo apt update
sudo apt install redis-server
sudo systemctl status redis.service

then run
rqworker
run at backend on server
nohup rqworker &

nohup rqworker > rq.out 2> rq.err &

for i in 1 2 3 4
do
    nohup rqworker > rq$i.out 2> rq$i.err &
done

proc=$(ps -xa | grep  QueueApi.py)
echo "procees Found $proc"
pids=$(echo "$proc" | cut -b 1,2,3,4,5,6,7,8)
echo "ids are $pids"
for pid in $pids
do
kill -9 $pid
echo "killed $pid"
done
rm nohup.out
nohup python QueueApi.py &
tail -f nohup.out


