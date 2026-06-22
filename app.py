from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base

from models import (
    User,
    Provider,
    Service,
    Appointment
)

from schemas import (
    UserCreate,
    Login,
    ProviderCreate,
    ServiceCreate,
    AppointmentCreate
)

from auth import create_access_token

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


# Database Connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home API
@app.get("/")
def home():
    return {"message": "Appointment Booking System"}


# Register User
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully",
        "user_id": new_user.id
    }


# Login User
@app.post("/login")
def login(user: Login, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return {"message": "Invalid User"}

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Add Provider
@app.post("/providers")
def add_provider(
    provider: ProviderCreate,
    db: Session = Depends(get_db)
):

    new_provider = Provider(
        name=provider.name,
        service_type=provider.service_type,
        email=provider.email,
        phone=provider.phone,
        availability_status=provider.availability_status
    )

    db.add(new_provider)
    db.commit()

    return {"message": "Provider Added Successfully"}


# View Providers
@app.get("/providers")
def get_providers(db: Session = Depends(get_db)):
    return db.query(Provider).all()


# Add Service
@app.post("/services")
def add_service(
    service: ServiceCreate,
    db: Session = Depends(get_db)
):

    new_service = Service(
        service_name=service.service_name,
        duration=service.duration
    )

    db.add(new_service)
    db.commit()

    return {"message": "Service Added Successfully"}


# View Services
@app.get("/services")
def get_services(db: Session = Depends(get_db)):
    return db.query(Service).all()


# Book Appointment
@app.post("/appointments")
def book_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Appointment).filter(
        Appointment.provider_id == appointment.provider_id,
        Appointment.appointment_date == appointment.appointment_date,
        Appointment.appointment_time == appointment.appointment_time
    ).first()

    if existing:
        return {
            "message": "Slot Already Booked"
        }

    new_appointment = Appointment(
        user_id=appointment.user_id,
        provider_id=appointment.provider_id,
        service_id=appointment.service_id,
        appointment_date=appointment.appointment_date,
        appointment_time=appointment.appointment_time
    )

    db.add(new_appointment)
    db.commit()

    return {
        "message": "Appointment Booked Successfully"
    }


# Confirm Appointment
@app.post("/appointments/{id}/confirm")
def confirm_appointment(
    id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(Appointment).filter(
        Appointment.id == id
    ).first()

    if not appointment:
        return {"message": "Appointment Not Found"}

    appointment.status = "Confirmed"
    db.commit()

    return {"message": "Appointment Confirmed"}


# Cancel Appointment
@app.post("/appointments/{id}/cancel")
def cancel_appointment(
    id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(Appointment).filter(
        Appointment.id == id
    ).first()

    if not appointment:
        return {"message": "Appointment Not Found"}

    appointment.status = "Cancelled"
    db.commit()

    return {"message": "Appointment Cancelled"}


# Complete Appointment
@app.post("/appointments/{id}/complete")
def complete_appointment(
    id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(Appointment).filter(
        Appointment.id == id
    ).first()

    if not appointment:
        return {"message": "Appointment Not Found"}

    appointment.status = "Completed"
    db.commit()

    return {"message": "Appointment Completed"}