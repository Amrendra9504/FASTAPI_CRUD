from database import Base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger

class Users(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True,index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True)
    phone = Column(BigInteger)
    address = Column(String(1000))
    is_active = Column(Boolean, default=True)