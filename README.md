








# Exercise : Product Delivery Pipline


Design an object-oriented solution and write a (Python) program that manages product pipelines for the company.

Problem description:
We are building a product deployment pipline to automatically deliver our products to various repositories. The pipline needs to be easily extensible to new **repository targets**, new ***notification*** channels, and future **actions**.


Requirements 
1. Each product has to folow attributes and actions : `scheduled time`,`build()`, `deploy()` and `notify()`.
2. Deploy may br to one or more of the following targets: `Artifactory`, `Nexus`, `s3`.
3. Notfication can be done to one or more channels and user groups (Example : Mail, Slack ...)
4. The main program should run a product pipline with the following stages : buils, deploy, notify at the scheduled time each day.`*`

Assignment
1. Design the solution.
2. Define the input for the program.
3. Write a program that run the product deployment pipelines based on the input.



`*` Build, Deploy and Notofy no need for the true implementation, can be orinting the time, product and action to the stdout/log file.