## Courses
-[Backend web development - a complete overview](www.youtube.com/watch?v=XBu54nfzxAQ)

## Notes
- API: Application Programming Interface-> list of all the different types of requests that the backend allows
- REST: REpresentational State Transfer -> naming convention for our requests
- REST API -> API that uses the REST naming convention

- Load Balancer: distributes requests evenly across VMs.
- PaaS: Platform As A Service -> just upload your backend code and it handles all the VMs and load balancer

- Microservices (Saas): split our backend into multiple codebases, each with thier own backend (VMs, load balancers, and database)

- Cloud computing:
  - IaaS -> infrastructure
  - PaaS -> platform
  - Saas -> software

- Additional Tech:
  - Primary Database -> the main database that the website uses
  - Blob storage & CDN -> store and load user uploaded images 
  - Search database (elastic search) -> text search
  - Cache (redis) -> takes the load off the primary database/ improve performance
  - Analyticl database (snowflake) -> do data science on the side, without busing the primary database further
  - Job Queue (rabiit mq) -> schedule a job for latter
  - 