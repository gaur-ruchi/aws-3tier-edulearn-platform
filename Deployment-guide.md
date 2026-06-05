## Deployment Guide

### Application Server Setup (Private App EC2)

Connect using AWS Systems Manager Session Manager.

Update packages:

```bash
sudo yum update -y
sudo dnf install python3 python3-pip -y
```

Install application dependencies:

```bash
pip3 install flask
pip3 install pymysql
pip3 install flask-cors
```

Verify installation:

```bash
python3 --version
pip3 --version
python3 -m pip list | grep Flask
```

Create project directory:

```bash
mkdir ~/edulearn
cd ~/edulearn
```

Create application file:

```bash
nano app.py
```

Paste the Flask application code and save.

Run the application:

```bash
python3 app.py
```

Verify Flask is running:

```bash
curl http://localhost:5000/health
```

Expected output:

```text
healthy
```

---

### Database Server Setup (Private DB EC2)

Install MariaDB:

```bash
sudo dnf install mariadb105-server -y
```

Enable and start service:

```bash
sudo systemctl enable mariadb
sudo systemctl start mariadb
```

Verify status:

```bash
sudo systemctl status mariadb
```

Login:

```bash
sudo mysql
```

Create database:

```sql
CREATE DATABASE edulearn;
```

Create database user:

```sql
CREATE USER 'edulearnuser'@'%'
IDENTIFIED BY 'Password123!';
```

Grant permissions:

```sql
GRANT ALL PRIVILEGES
ON edulearn.*
TO 'edulearnuser'@'%';

FLUSH PRIVILEGES;
```

Create registration table:

```sql
USE edulearn;

CREATE TABLE registrations (

id INT AUTO_INCREMENT PRIMARY KEY,

fullname VARCHAR(100),

email VARCHAR(100),

phone VARCHAR(30),

course VARCHAR(100),

experience VARCHAR(30),

comments TEXT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
```

---

### Security Group Configuration

#### ALB-SG

Inbound:

```text
HTTP 80
Source: 0.0.0.0/0
```

#### APP-SG

Inbound:

```text
Custom TCP 5000
Source: ALB-SG
```

#### DB-SG

Inbound:

```text
MYSQL/Aurora 3306
Source: APP-SG
```

---

### Database Connectivity Validation

Install MariaDB client on App EC2:

```bash
sudo dnf install mariadb1011 -y
```

Connect to database:

```bash
mysql -h <DB_PRIVATE_IP> -u edulearnuser -p
```

Successful connection confirms:

* Security Groups are configured correctly
* Private subnet routing is working
* Application tier can reach database tier

---

### Application Validation

Verify API health endpoint:

```bash
curl http://localhost:5000/health
```

Expected:

```text
healthy
```

Verify database connectivity:

```bash
curl http://localhost:5000/testdb
```

Expected:

```text
Database connection successful. Record inserted.
```

---

### Verify Database Records

Connect to MariaDB:

```bash
sudo mysql
```

Query records:

```sql
USE edulearn;

SELECT *
FROM registrations
ORDER BY id DESC;

SELECT * FROM registrations;
```

Successful output confirms end-to-end data flow from:

```text
Browser
→ Route53
→ CloudFront
→ S3
→ ALB
→ Flask API
→ MariaDB
```
