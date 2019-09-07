# Problem Statement - "Based on the instance types and on demand costs put forward some recommendations on how to increase the RI coverage."

`````````````
The solutions or the recommendations for reducing the on-demand cost and increasing the RI coverage depends on individual use cases. For the given data in ri-instanceType.csv, below are few observations which can bring down on-demand cost - 
    1. We notice that there are few instances which are being run for 1000+ on-demand hours. Running such (non-temporary)     instances as RI, we can bring down the on-demand costs. 
    2. Depending on the requirement, by deploying right sized instances and in regions where the chosen instance type comes with less price can bring down the on-demand cost to an extent.
    3. Going for convertible reserved instances, we would be able to increase or decreasr the instance size or exhange it with another convertible instance, thereby helping to achieve scalability of instance size.
    4. Buying reserved instances with full or partial upfront cost for long running instances, the on-demand cost can be significantly brought down.
`````````````````