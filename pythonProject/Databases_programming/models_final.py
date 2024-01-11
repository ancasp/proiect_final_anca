"""
SLQAlchemy este un ORM, cel mai popular - ORM Object Relational Mapping = o reprezentare a obiectelor in python in o alta forma
Nu foloeste deloc sintaxa SQL ci doar limbaj Python
- clasa reprezinta un tabel
- atribuitele instantelor reprezinta coloanele
- o instanta reprezinta un rand

Tabelele sunt reprezentate de clase, clasele pentru a putea fi luate in considerare trebuie sa mosteneasca declarative_base()
"""


from sqlalchemy import create_engine, Column, String, Integer, Date, Boolean, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Cars(Base):
    __tablename__ = 'cars'

    ####################################################################
    ### columns ### id, producer, model, year, horse_power, price_per_day ###

    id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(DECIMAL(6,2), nullable=False)
    ####################################################################


    ####################################################################
    ### relationships ### from bookings table to cars table ###

    bookings_r = relationship('Bookings', back_populates='car_r', cascade="all, delete", passive_deletes=True)
    ####################################################################


    ####################################################################
    ### methods ###

    def __str__(self):
        return f"{self.producer}  -  {self.model}  -  {self.year}  -  {self.horse_power}CP  -  ${self.price_per_day}"
    ####################################################################


class Clients(Base):
    __tablename__ = 'clients'

    ####################################################################
    ### columns ### id, name, surname, address, city ###

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    ####################################################################


    ####################################################################
    ### relationships ### from bookings table to clients table ###

    bookings_r = relationship('Bookings', back_populates='client_r', cascade="all, delete", passive_deletes=True)
    ####################################################################


    ####################################################################
    ### methods ###

    def __str__(self):
        return f"{self.surname} {self.name}"
    ####################################################################


class Bookings(Base):
    __tablename__ = 'bookings'

    ####################################################################
    ### columns ### id, client_id, car_id, start_date, end_date, total_amount ###

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.id', ondelete="CASCADE"), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.id', ondelete="CASCADE"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(DECIMAL(8,2), nullable=False)
    ####################################################################


    ####################################################################
    ### relationships ###

    client_r = relationship('Clients', back_populates='bookings_r')
    car_r = relationship('Cars', back_populates='bookings_r')
    ####################################################################


    ####################################################################
    ### methods ###

    def __str__(self):
        return f"{self.client_id}  -  {self.car_id}  -  {self.total_amount}"
    ####################################################################
