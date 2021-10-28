**cloud app**

|Feature|Past|Present|  
|---|---|---|  
|Clients|Enterprise/Intranet|Public/Internet|
|Demand|Stable(small)|Dynamic(small -> massive)|
|Datacenter|Single tenant|Multi-tenant|
|Operations|People(expensive)|Automation(cheap)|
|Scale|Up via few reliable(expensive) PCs|Out via lots of (cheap) commodity PCs|
|Failure|Unlikely but possible|Very likely|
|Machine loss|Catastrophic|Normal(no big deal)|
|Exceptions|Catch, swallow & keep running|Crash & restart|
|Communication|In order<br> Exactly once|Out of order<br> Client must retry & servers must be idempotent|

request/reply pattern
1. Client may send to busy(not idle) service instance
2. Client may crash/scale down while waiting for service instance's reply

Messaging communication
1. Client doesn't wait for service reply(no blocked threads/long-lived locks)
2. Service instance pulls work vs busy service instances pushed more work
3. Services don't need listening endpoints; client/services talk to queue service
4. Client/service instances can come, go, & move at will without message loss.
5. Use queue length to determine need to scale up/down

```
net start docker
docker images
docker build -t contoso/ads-support .
docker run -d --name testcontainer contoso/ads-support
docker ps
docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" testcontainer
docker stop testcontainer
docker rm testcontainer
docker ps -a
docker login <login server> -u <username> -p <password>
docker tag contoso/ads-support <login server>/contoso/ads-support
docker push <login server>/contoso/ads-support
```
