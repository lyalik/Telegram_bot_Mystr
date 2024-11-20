from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    ton_wallet = Column(String, unique=True)
    referral_link = Column(String, unique=True)
    invited_count = Column(Integer, default=0)
    status = Column(String, default='regular')
    balance = Column(Float, default=0.0)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    type = Column(String)
    date = Column(String)
    user = relationship("User", back_populates="transactions")

User.transactions = relationship("Transaction", order_by=Transaction.id, back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    type = Column(String)
    date = Column(String)

Base.metadata.create_all(engine)

def get_user(telegram_id):
    return session.query(User).filter_by(telegram_id=telegram_id).first()

def create_user(telegram_id, username):
    new_user = User(telegram_id=telegram_id, username=username)
    session.add(new_user)
    session.commit()

def update_balance(telegram_id, amount):
    user = get_user(telegram_id)
    if user:
        user.balance += amount
        session.commit()

def get_transactions(user_id):
    return session.query(Transaction).filter_by(user_id=user_id).all()
