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
