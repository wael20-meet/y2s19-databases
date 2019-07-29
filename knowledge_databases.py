from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_url,article_name,article_topic,article_rating):
	new_article = Knowledge(
        article_url=article_url,
        article_name=article_name,
        article_topic=article_topic,
        article_rating=article_rating)
	session.add(new_article)
	session.commit()


def query_all_articles():
	articles = session.query(
      Knowledge).all()
	return articles




def query_article_by_topic(the_name):
	article = session.query(
	Knowledge).filter_by(
	article_topic = the_name).first()
	return article





def delete_article_by_topic(the_name):
	session.query(Knowledge).filter_by(
		article_topic=the_name).delete()
	session.commit()


def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
	

def edit_article_rating(the_name, article_rating):
    article_object = session.query(
        Knowledge).filter_by(
        article_name=the_name).first()
    article_object.article_rating = article_rating
    session.commit()