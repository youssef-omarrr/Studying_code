## Courses
- [Backend web development - a complete overview](https://youtu.be/XBu54nfzxAQ?si=NvPWfaiRRWUtapUz)

## Notes
**API (Application Programming Interface)**: A set of rules that lets one software talk to another. Defines request types (GET, POST, etc.) and data formats.

**REST**: An architectural style for building web services. Uses standard HTTP methods and follows conventions like `/users` for resources.

**REST API**: An API that follows REST principles. Example: `GET /users` retrieves all users.

**Load Balancer**: Distributes incoming traffic across multiple servers so no single server gets overwhelmed. Example: Nginx or cloud load balancers.

**PaaS (Platform as a Service)**: Cloud platform that lets you deploy code without managing servers. Example: Heroku, Vercel - just upload your code and it handles scaling, load balancers, and VMs.

**Microservices**: Small, independent services that each handle a specific business function. Each has its own codebase, database, and can be deployed separately. Good for large teams and scaling different parts independently.

**Cloud Computing tiers**:
- IaaS (Infrastructure as a Service): Raw virtual machines and network. You manage OS, runtime, data. Example: AWS EC2.
- PaaS (Platform as a Service): You manage code; provider handles VMs, scaling, load balancing. Example: Heroku, Firebase.
- SaaS (Software as a Service): Complete software solution you use over the internet. Example: Gmail, Salesforce.

**Additional Tech**:
- **Primary Database**: Main data store for your application. Example: PostgreSQL, MongoDB.
- **Blob Storage & CDN**: Stores static files (images, videos) and delivers them fast via edge locations. Example: AWS S3 + CloudFront.
- **Search Database (Elasticsearch)**: Specialized for full-text search and analytics. Example: searching through product catalogs.
- **Cache (Redis)**: In-memory key-value store for fast lookups. Reduces database load by caching frequent requests. Example: caching user sessions.
- **Analytic Database (Snowflake)**: Cloud-based data warehouse for business intelligence and data science workloads. Keeps analytics separate from your primary database.
- **Job Queue (RabbitMQ)**: Manages background tasks (email sending, image processing). Jobs are placed in a queue and workers process them one by one.