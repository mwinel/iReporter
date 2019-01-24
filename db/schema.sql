-- create database tables

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    othernames VARCHAR(20),
    username VARCHAR(20),
    email VARCHAR(20),
    password VARCHAR(200),
    phone_number VARCHAR(20),
    is_admin BOOLEAN DEFAULT FALSE,
    created_on TEXT
);

CREATE TABLE IF NOT EXISTS incidents (
    incident_id SERIAL PRIMARY KEY,
    incident_type VARCHAR(20),
    location VARCHAR(100),
    status VARCHAR(50) DEFAULT 'draft',
    images VARCHAR(50),
    videos VARCHAR(50),
    comment VARCHAR(50),
    created_on TEXT,
    created_by TEXT
);

INSERT INTO users (firstname, lastname, othernames, username, email, password,
                   phone_number, is_admin)
SELECT * FROM (SELECT 'nelson', 'murungi', 'mwiru', 'mwinel', 'mwinel@live.com', '123456', '0781916565', TRUE)
AS tmp WHERE NOT EXISTS
(SELECT firstname FROM users WHERE firstname = 'nelson') LIMIT 1;
