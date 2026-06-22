# Appointment Scheduling & Service Booking Platform

## Project Overview

This project is a backend application developed using FastAPI and MySQL. It allows customers to book appointments with service providers, manage schedules, track booking status, and prevent duplicate bookings.

## Technologies Used

* Python
* FastAPI
* MySQL
* SQLAlchemy
* JWT Authentication
* Uvicorn

## Features

### User Authentication

* Register User
* Login User
* JWT Token Generation

### Provider Management

* Add Provider
* View Providers

### Service Management

* Add Service
* View Services

### Appointment Booking

* Book Appointments
* Prevent Duplicate Bookings
* Manage Appointment Status

### Appointment Status Workflow

* Pending
* Confirmed
* Completed
* Cancelled

## Database Tables

### Users

* id
* name
* email
* password

### Providers

* id
* name
* service_type
* email
* phone
* availability_status

### Services

* id
* service_name
* duration

### Appointments

* id
* user_id
* provider_id
* service_id
* appointment_date
* appointment_time
* status

## API Endpoints

### Authentication

* POST /register
* POST /login

### Providers

* POST /providers
* GET /providers

### Services

* POST /services
* GET /services

### Appointments

* POST /appointments
* POST /appointments/{id}/confirm
* POST /appointments/{id}/cancel
* POST /appointments/{id}/complete

## Running the Project

Install dependencies:

pip install -r requirements.txt

Run the application:

uvicorn app:app --reload

Open Swagger Documentation:

http://127.0.0.1:8000/docs

## Author

Sravani
