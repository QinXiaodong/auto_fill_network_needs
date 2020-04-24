# auto_fill_network_needs
根据网络打通策略模板表自动填充沃运维上的网络需求管理工单

同一目录下需要有
>和本地chrome版本相同的chromedriver
>config.ini文件，需要提供沃运维账号和密码以及使用到的网络打通策略文件路径  
>网络打通策略文件，需要包含以下属性,属性名在表的首行  
>>源系统业务负责人  
>>源负责人联系电话  
>>源主机所属区域  
>>目标主机ip地址  
>>目标主机所属系统  
>>目标主机所属机房  
>>目标系统业务负责人  
>>目标负责人联系电话  
>>目标主机所属区域  
>>目的端口  
>>协议  
>>宽带需求  
>>数据交互内容  

网络需求管理系统需要在沃运维的应用收藏页面第一个，最好是唯一一个。


请从main.py文件启动，执行完成后沃运维网络需求管理工单会增加草稿工单。
