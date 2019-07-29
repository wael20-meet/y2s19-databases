from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'sport'
	sport_id = Column(Integer, primary_key=True)
	topic = Column(String)
	year = Column(Integer)
	rating = Column(Integer)
	finished_lab = Column(Boolean)
	pass
	def __repr__(self):
		return ("topic Name: {}\n"
			"sport Year: {} \n"
			"Has Finished Lab: {}").format(
			self.topic, self.year, self.finished_lab)

print(repr(Knowledge.__table__))

x = Knowledge(topic="football", year=1869)
print(x)