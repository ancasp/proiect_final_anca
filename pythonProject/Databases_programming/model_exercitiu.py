from sqlalchemy import create_engine, Column, String, Integer, Date, Boolean, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Departamente(Base):
    __tablename__ = "departamente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(50), nullable=False)
    descriere = Column(String(200))

    proiecte_r = relationship("Proiecte", back_populates="departament_r", cascade="all, delete", passive_deletes=True)
    angajati_r = relationship("Angajati", back_populates="departament_r", cascade="all, delete", passive_deletes=True)

    def __str__(self):
        return f"{self.nume} - {self.descriere}"

class Proiecte(Base):
    __tablename__ = "proiecte"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(50), nullable=False)
    descriere = Column(String(200), nullable=False)
    id_departament_responsabil = Column(Integer, ForeignKey('departamente.id', ondelete="CASCADE"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    priority = Column(String(10))
    cost = Column(DECIMAL(8,2), nullable=False)
    profit = Column(DECIMAL(8,2), nullable=False)

    aapp_r = relationship("AsignareAngajatiPeProiecte", back_populates="proiect_r", cascade="all, delete", passive_deletes=True)
    departament_r = relationship("Departamente", back_populates="proiecte_r")

    def __str__(self):
        return f"{self.nume} - {self.descriere} - {self.cost} - {self.profit}"

class Angajati(Base):
    __tablename__ = "angajati"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    telefon = Column(Integer, nullable=False)
    data_nasterii = Column(Date, nullable=False)
    pozitie = Column(String(30), nullable=False)
    is_team_leader = Column(String(2), nullable=False)
    data_angajarii = Column(Date, nullable=False)
    id_departament = Column(Integer, ForeignKey('departamente.id', ondelete="CASCADE"), nullable=False)
    salariu_de_baza = Column(Integer, nullable=False)

    departament_r = relationship("Departamente", back_populates="angajati_r")
    bonusuri_r = relationship("Bonusuri", back_populates="angajat_r", cascade="all, delete", passive_deletes=True)
    aapp_r = relationship("AsignareAngajatiPeProiecte", back_populates="angajat_r", cascade="all, delete", passive_deletes=True)

    def __str__(self):
        return f"{self.nume} - {self.pozitie} - {self.salariu_de_baza}"

class AsignareAngajatiPeProiecte(Base):
    __tablename__ = "aapp"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_angajat = Column(Integer, ForeignKey('angajati.id', ondelete="CASCADE"), nullable=False)
    id_proiect = Column(Integer, ForeignKey('proiecte.id', ondelete="CASCADE"), nullable=False)

    angajat_r = relationship("Angajati", back_populates="aapp_r")
    proiect_r = relationship("Proiecte", back_populates="aapp_r")

    def __str__(self):
        return f"{self.id_angajat} - {self.id_proiect}"

class Bonusuri(Base):
    __tablename__ = "bonusuri"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_angajat = Column(Integer, ForeignKey('angajati.id', ondelete="CASCADE"), nullable=False)
    explicatie = Column(String(200), nullable=False)
    suma = Column(DECIMAL(8,2), nullable=False)

    angajat_r = relationship("Angajati", back_populates="bonusuri_r")

    def __str__(self):
        return f"{self.id_angajat} - {self.suma}"


















# 2. create tables:
# 			a. table "departamente": id, nume, descriere
# 			b. table "proiecte": id, nume, descriere, id_departament_responsabil, start_date, end_date, priority, cost, profit
# 			c. table "angajati": id, nume, email, telefon, data_nasterii, pozitie, is_team_leader, data_angajarii, id_departament, salariu_de_baza
# 	        d. table "asignare_angajati_pe_proiecte": id, id_angajat, id_proiect
# 			e. table "bonusuri": id, id_angajat, explicatie, suma