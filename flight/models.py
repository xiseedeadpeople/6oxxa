from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    from_city = Column(String)
    to_city = Column(String)
    departure_date = Column(Date)
    return_date = Column(Date)

class PurchaseHistory(Base):
    __tablename__ = 'purchase_history'

    id = Column(Integer, primary_key=True)
    from_city = Column(String)
    to_city = Column(String)
    departure_date = Column(Date)
    return_date = Column(Date)

    def __repr__(self):
        return f"<PurchaseHistory(from_city='{self.from_city}', to_city='{self.to_city}', " \
               f"departure_date='{self.departure_date}', return_date='{self.return_date}')>"

engine = create_engine('sqlite:///flights.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
