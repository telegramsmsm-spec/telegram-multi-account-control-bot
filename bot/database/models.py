from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True, nullable=False)
    session_string = Column(Text, nullable=False)
    country = Column(String, default="Custom")
    status = Column(String, default="active")  # active, limited, banned, warming
    proxy_id = Column(Integer, ForeignKey("proxies.id"), nullable=True)
    last_activity = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    proxy = relationship("Proxy", back_populates="accounts")

class Proxy(Base):
    __tablename__ = "proxies"
    id = Column(Integer, primary_key=True)
    type = Column(String, default="socks5")  # socks5, http, mtproto
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    country = Column(String, default="")
    is_alive = Column(Boolean, default=True)
    last_check = Column(DateTime, default=datetime.utcnow)

    accounts = relationship("Account", back_populates="proxy")

class Template(Base):
    __tablename__ = "templates"
    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)  # internal_report, external_report, message
    language = Column(String, default="ar")
    title = Column(String)
    body = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)

class ActionLog(Base):
    __tablename__ = "action_logs"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    action = Column(String)
    target = Column(String)
    result = Column(String)
    details = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
