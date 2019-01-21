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
    created_on TIMESTAMPTZ
);