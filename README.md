# auto-catalog-ai
AutoCatalogAI is an AI-powered solution that leverages computer vision to analyze vehicle images, generate metadata, and automate database structuring for web catalogs.

### **AutoCatalogAI**  
**Description:**  
AutoCatalogAI is an AI-powered application that transforms [raw vehicle images](https://www.kaggle.com/datasets/alirezaatashnejad/over-20-car-brands-dataset/data) into a structured, web-ready catalog. Leveraging language models with computer vision capabilities, the app automatically analyzes images, extracts key metadata (make, model, color, year, etc.), and generates a relational database using SQL commands (DDL and DML). With a scalable, low-latency backend, AutoCatalogAI is perfect for creating vehicle catalogs quickly, accurately, and efficiently, even with large datasets.  

**Key Features:**  
1. **Image Analysis**: Identifies vehicle makes, models, and visual attributes.  
2. **Metadata Generation**: Extracts and structures key information for each vehicle.  
3. **Database Creation**: Generates SQL commands for table creation (DDL) and data insertion (DML).  
4. **Web Catalog Integration**: Prepares data for use in web platforms.  
5. **Scalability and Low Latency**: Processes large volumes of images in real-time with an optimized backend.  
6. **Validation and Correction**: Allows human review to ensure metadata accuracy.  

**Core Technologies:**  
- LLMs with computer vision (GPT-4 Vision, LLaVA).  
- Backend in FastAPI, Node.js, or Golang.  
- Relational databases (PostgreSQL, MySQL).  
- Message queues (RabbitMQ, Kafka) for asynchronous processing.  

AutoCatalogAI is the ultimate solution for automating vehicle catalog creation, reducing time and costs while maintaining data accuracy and quality.