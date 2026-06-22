# models.py

from sqlalchemy import Column,Integer,String,ForeignKey,Date,Time
from database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    email=Column(String(100),unique=True)
    password=Column(String(255))


class Provider(Base):
    __tablename__="providers"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    service_type=Column(String(100))
    email=Column(String(100))
    phone=Column(String(20))
    availability_status=Column(String(50))


class Service(Base):
    __tablename__="services"

    id=Column(Integer,primary_key=True,index=True)
    service_name=Column(String(100))
    duration=Column(Integer)


class Appointment(Base):
    __tablename__="appointments"

    id=Column(Integer,primary_key=True,index=True)

    user_id=Column(Integer,ForeignKey("users.id"))
    provider_id=Column(Integer,ForeignKey("providers.id"))
    service_id=Column(Integer,ForeignKey("services.id"))

    appointment_date=Column(Date)
    appointment_time=Column(Time)

    status=Column(String(50),default="Pending")