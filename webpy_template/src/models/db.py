#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import Column, Integer, String, Numeric, Sequence, or_
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config
db = config.site.db

db_str = "%s%s://%s:%s@%s:%s/%s?charset=%s" % (db['engine'], db['adapt'], db['user'], db['pawd'], db['host'], db['port'], db['name'], db['char'])
engine = create_engine(db_str, echo=db['log'])

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id       = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name     = Column(String(100))
    weight   = Column(Numeric(3.2))
    address  = Column(String(100))
    fullname = Column(String(100))
    password = Column(String(32))
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)
       
class Shop(Base):
    __tablename__ = 'items'
    id      = Column(Integer, primary_key=True)
    title   = Column(String(1024))
    link    = Column(String(1024))
    summary = Column(String(5000))
    image   = Column(String(1024))
    buy     = Column(String(2048))
    link_md5= Column(String(32))
    fetch_time = Column (String(100))
    
    def __repr__(self):
       return "<Shop(title='%s')>" % self.title
       
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
db_session = Session()


'''
g = globals()
def query (table):
    temp = g.get(table)
    return session.query (temp)

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
print ed_user.name
print ed_user.fullname
print ed_user.id
session.add(ed_user)
print ed_user.id
our_user = session.query(User).filter_by(name='ed').first()
print our_user


session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])

session.dirty
session.new 
session.commit()


print ed_user.id

session.query(User).filter(User.name == 'ed')
session.query(User).filter(User.name != 'ed')
session.query(User).filter(User.name.like('%ed%'))
session.query(User).filter(User.name.in_(['ed', 'wendy', 'jack']))
session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy'))


print session.query(User).all()
print session.query(User).first()
#print session.query(User).one()


print session.query(User).filter("id<:value and name=:name").params(value=224, name='fred').order_by(User.id).first()


'''