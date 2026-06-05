CREATE DATABASE edulearn;

USE edulearn;

CREATE TABLE registrations (

id INT AUTO_INCREMENT PRIMARY KEY,

fullname VARCHAR(100),

email VARCHAR(100),

phone VARCHAR(30),

course VARCHAR(100),

experience VARCHAR(30),

comments TEXT,

created_at TIMESTAMP
DEFAULT CURRENT_TIMESTAMP

);