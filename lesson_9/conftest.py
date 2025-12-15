import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

TEST_DATABASE_URL = "postgresql://postgres:1236987a@localhost:5432/postgres"

@pytest.fixture(scope="function")
def db_session():
    """Фикстура для тестовой сессии БД с PostgreSQL"""
    engine = create_engine(TEST_DATABASE_URL)
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
  
    session.rollback() 
    session.close()
   
    Base.metadata.drop_all(engine)