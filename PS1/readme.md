Challenge #1

A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources.


Iac Tool used: Terraform

Architecture:

Resources:
1. VPC with CIDR 10.0.0.0/16 has been created
2. 6 Subnets have been created
    a. 2 subnets for web-tier ( Public)- web-subnet-1 & web-subnet-2
    b. 2 subnets for Application tier (Private)-application-subnet-1 & application-subnet-2
    c. 2 subnets for DB tier (Private )-database-subnet-1 & database-subnet-2
3. Internet Gateway igw has been created with web-rt route table to allow connections from Internet associated to both web-tier subnets
4. 2 webservers have been created to serve requests - webserver1 & webserver2 in different As but same region
5. 3 security groups have been created :
    a. web-sg -Inbound rule opening http port 80 & all outbound traffic
    b. webserver-sg -  Inbound rule opening http port 80 & serving traffic from web-sg Security group only
    c. database-sg -  Inbound rule opening port 3306 & serving traffic from webserver-sg Security group only
6. External Application load balancer external-elb with both web-tier subents and web-sg security group has been created 
7. MySQL RDS instance with multi-AZ availabiltiy with db-tier subnet  & database-sg security group has been created

Output

ALB DNS Name to see the front end URL
