# schemas.py

from pydantic import BaseModel
from datetime import date,time

class UserCreate(BaseModel):
    name:str
    email:str
    password:str


class Login(BaseModel):
    email:str
    password:str


class ProviderCreate(BaseModel):
    name:str
    service_type:str
    email:str
    phone:str
    availability_status:str


class ServiceCreate(BaseModel):
    service_name:str
    duration:int


class AppointmentCreate(BaseModel):
    user_id:int
    provider_id:int
    service_id:int
    appointment_date:date
    appointment_time:time