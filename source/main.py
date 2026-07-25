import os
import sys
from pathlib import Path

from fastapi import Depends, FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.orm import Session

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from database import Base, SessionLocal, engine
from models import Users

Base.metadata.create_all(bind=engine)

app = FastAPI()

jinja_env = Environment(loader=FileSystemLoader(str(ROOT_DIR / "templates")))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    all_user = db.query(Users).filter_by(is_active=True).all()
    template = jinja_env.get_template("home.html")
    html = template.render(request=request, all_user=all_user)
    return HTMLResponse(content=html)

@app.get("/add_student", response_class=HTMLResponse)
def add_student(request: Request, db: Session = Depends(get_db)):
    template = jinja_env.get_template("add_student.py")
    html = template.render(request=request)
    return HTMLResponse(content=html)


@app.post("/insert_student")
async def insert_student(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    first_name = form_data['first_name']
    last_name = form_data['last_name']
    email = form_data['email']
    phone = form_data['phone']
    address = form_data['address']
    # is_active = form_data['is_active']
    email_exist = db.query(Users).filter_by(email=email).first()
    if email_exist:
        d = {'value': 2}
    else:
        u = Users(first_name=first_name, last_name=last_name, email=email,
                phone=phone, address=address)
        db.add(u)
        db.commit()
        d = {'value': 1, 'insert_id':u.id}
    dt = jsonable_encoder(d)
    return dt


@app.get("/edit_student/{student_id}")
def edit_student(student_id:int, request: Request, db: Session = Depends(get_db)):
    stu_data = db.query(Users).filter_by(id=student_id).first()
    d = {'id': student_id, 'first_name': stu_data.first_name,'last_name': stu_data.last_name,
         'email': stu_data.email, 'phone': stu_data.phone, 'address': stu_data.address}
    dt = jsonable_encoder(d)
    return dt


@app.post("/update_student")
async def update_student(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    id = form_data['id']
    first_name = form_data['first_name']
    last_name = form_data['last_name']
    email = form_data['email']
    phone = form_data['phone']
    address = form_data['address']

    upd = db.query(Users).filter_by(id=id).first()
    upd.first_name = first_name
    upd.last_name = last_name
    upd.email = email
    upd.phone = phone
    upd.address = address
    db.commit()
    db.refresh(upd)
    d = {'value': 1}
    dt = jsonable_encoder(d)
    return dt

@app.get("/delete_student/{student_id}")
def delete_student(student_id:int, request: Request, db: Session = Depends(get_db)):
    stu_data = db.query(Users).filter_by(id=student_id).first()
    stu_data.is_active = 0
    db.commit()
    db.refresh(stu_data)
    d = {'value': 1}
    dt = jsonable_encoder(d)
    return dt