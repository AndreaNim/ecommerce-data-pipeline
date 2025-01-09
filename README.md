# E-commerce Data Pipeline

We will build a data ingestion pipeline that stores raw data, then
transform it by combining order and inventory information.

## A detailed list of tools and technologies used in the solution

- Python: Core programming language for implementing the data pipeline.

  Reason for Use:

  - Python is a widely used language for data processing and analytics.
  - Have lots of libraries like pandas (for data manipulation) and pymongo (for MongoDB interaction).
  - Easy to write, maintain, and extend for future requirements.
  
- pandas (Python Library) - Load, validate, and transform data from the CSV files.

  Reason for Use:
  
  - Industry-standard library for data manipulation.
  - Provides support for working with structured data (CSV files).
  Simplifies operations like filtering, merging, and aggregations.
  
- MongoDB - Database for storing raw and transformed data.
  
  Reason for Use:
   - Database for storing raw and transformed data.
   - Scalability: MongoDB is a NoSQL database that handles large volumes of unstructured or semi-structured data efficiently.
   - Flexibility: Allows dynamic schema design, making it suitable for e-commerce data that might evolve over time.
Analytics: Supports aggregation pipelines for querying and analyzing data.
Local Setup: Easy to deploy locally using Docker

- Docker - containerize and run MongoDB locally.

  Reason for Use:

  - Ensures the database environment is consistent across all setups.
  - Simplifies local deployment without requiring a manual MongoDB installation.
  - Containers are lightweight and easy to manage.
  
- Docker Compose - Define and run multi-container Docker applications (for MongoDB)

   Reason for Use:
   - Simplifies the management of dependent services like MongoDB.
   - Allows the database setup to be easily shared and reproduced using the docker-compose.yml file.
  
- pymongo (Python Library) - Connect to and interact with MongoDB.
 
   Reason for Use:

   - Official library for MongoDB in Python.
   - Provides easy-to-use methods for CRUD operations and advanced queries.
   
 ## Prerequisites
 1. Python
 2. Docker & Docker Compose
 
 ### Let’s get started
 
 **1.Add Dependencies**
 
   Add the required libraries by running the below command.
 
  `pip install -r requirements.txt`
 
  This will install pandas,pymongo and docker-compose.
 
 **2.Start the MongoDB container**
 
   Run the below command.
   
   `docker-compose up -d`
   
 **3.Execute the pipeline**
  
   Run the below command.
 
   `python main.py`
 
 **4.Verify Data in MongoDB**
 
 There are different Options which you can choose to use.

  - Option 1: MongoDB Compass**

    MongoDB Compass is a graphical user interface (GUI) for MongoDB.

    Steps to follow
    - Download MongoDB Compass
    - Install it on your system
    - Open MongoDB Compass.In the connection dialog, enter the connection URL:
  
      `mongodb://localhost:27017`
  
    - Once connected, you’ll see a list of databases in the left panel.
  
  - Option 2: MongoDB Shell
  
    - Install the Mongo Shell
    - Open a terminal or command prompt and run the following command to connect to your MongoDB instance
  
      `mongosh`
    
      This connects to the default instance at localhost:27017
   
    
5.Aggregate Queries
 
 1.Total Orders Per Product: Groups orders by productId and calculates the total quantity ordered for each product.
 
 `pipeline = [
        {"$group": {"_id": "$productId", "totalOrders": {"$sum": "$quantity"}}},
        {"$sort": {"totalOrders": -1}}
    ]`
    
 2.Top 10 Selling Products : calculate the total number of orders for each product and then sort the results in descending order.
 
 `pipeline = [
        {
            "$group": {
                "_id": "$productId",
                "totalOrders": {"$sum": 1},
            }
        },
        {"$sort": {"totalOrders": -1}},
        {"$limit": limit},
    ]`
    
 3.Products with Low Inventory : identifies products with inventory below a specified threshold, helping to monitor stock levels and prevent shortages.
 
 `pipeline = [
        {"$match": {"quantity": {"$lt": threshold}}},
        {"$project": {"_id": 0, "productId": 1, "productName": 1, "quantity": 1}},
    ]`
  
 ## Tools and technology recommendations for large scale of e-commerce data
 
 - Data Ingestion
 
   Apache Kafka, handles real-time streaming and batch ingestion of high-velocity data, making it ideal for e-commerce platforms with frequent transactions and updates.
   
   Google Pub/Sub for managed cloud streaming.
   
 - Data Storage
    1. Raw Data 
    
       NoSQL Database, NoSQL databases are designed to handle scalability, high availability, and schema flexibility, making them better suited for large-scale e-commerce platforms.
       
       Cassandra or Amazon DynamoDB for distributed NoSQL storage.
       
    2. Processed and Analytical Data
    
       Columnar Database, Optimized for OLAP (Online Analytical Processing) queries.
       Supports large-scale data analytics with fast query performance.
       Amazon Redshift, Google BigQuery, or Snowflake.
       
     3. Data Lake
     
        Efficient storage of raw, semi-processed, and processed data for analytics and machine learning.
        
 - Data Transformation
 
   Apache Spark,Scalable distributed data processing for ETL.
   Apache Flink for real-time processing.
   
 - Data Orchestration
   
   Apache Airflow, Orchestrates workflows for data ingestion, transformation, and storage.
   Prefect or Dagster for modern data workflow orchestration.
   
 - Query and Analytics
   Athena (AWS Managed Service): Query S3-based data lakes directly
 
 - Visualization
 
   Tableau, Power BI, or Looker for interactive dashboards and insights.
   Apache Superset,Open-source
   
 - Infrastructure
 
   1. Containerization - Docker
   2. Container Orchestration - Kubernetes
   3. Infrastructure as Code - Terraform or Pulami
   4. Cloud Platforms - AWS or Azure, or Google Cloud Platform
   
  - Scalability and Fault Tolerance
  
    Caching - Redis
  
  - Logging and Monitoring
  
    Prometheus or Grafana
  