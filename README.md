# compare-hadoop-confs

This is a python script which can compare two directories containing hadoop configuration files. When compared it would print the following
 - Added configuration to second directory
 - Removed configuration from second directory
 - Configuration which has different value in second directory

It usees nice colors for the output for better readability.

### Requirement

    pip install termcolor
   
### How to run
    
    python compare_hadoop_conf.py <base-conf-directory> <new-conf-directory>
    
### Sample output

    Added configuration:

    mapreduce.client.submit.file.replication : 7
    mapreduce.map.java.opts : -Djava.net.preferIPv4Stack=true -Xmx825955249
    io.file.buffer.size : 65536
    
    Removed configuration, with old values:
    
    yarn.scheduler.capacity.resource-calculator : org.apache.hadoop.yarn.util.resource.DefaultResourceCalculator
    mapred.fairscheduler.eventlog.enabled : true
    yarn.nodemanager.local-dirs : /data/hadoop/hadoop-yarn/cache/${user.name}/nm-local-dir
    
    Modified configuration:
    
    yarn.scheduler.fair.assignmultiple:
    true
    false
    mapreduce.reduce.cpu.vcores:
    4
    1
