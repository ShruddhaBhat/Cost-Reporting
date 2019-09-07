# Problem Statement - "Based on the instance types and on demand costs put forward some recommendations on how to increase the RI coverage."

`````````````
The solutions or the recommendations for reducing the on-demand cost and increasing the RI coverage depends on individual use cases. For the given data in ri-instanceType.csv, below are few observations which can bring down on-demand cost - 
``````````````
    1. The data shows that there are few instances which are being run for 1000+ on-demand hours with less RI coverage. Choosing appropriate RI, on-demand costs can be significantly brought down. 
    2. Depending on the requirement, by deploying right sized instances and in regions where the chosen instance type comes with less price can reduce the on-demand cost to an extent.These instances can be revisited regularly to analyse and determine whether the workload still demands such costly instances. 
    3. Going for convertible reserved instances for above stated instance types allows to increase or decrease the instance size or exhange it with another convertible instance, thereby helping in right sizing the instances, which inturn reduces the price without compromising the performance.
    4. Buying reserved instances with full or partial upfront cost for long running instances, the on-demand cost can be brought down by a large value.
