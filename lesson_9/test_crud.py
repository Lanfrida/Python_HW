import pytest
from sqlalchemy.exc import IntegrityError
from models import Student, Subject  # Без точки!

def test_create_student(db_session):
    """Тест создания студента"""
    student_data = {
        'name': 'Иван Иванов',
        'email': 'ivan@test.ru',
        'course': 'Математика'
    }
    
    student = Student(**student_data)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    
    assert student.id is not None
    assert student.name == 'Иван Иванов'
    assert student.email == 'ivan@test.ru'
    assert student.course == 'Математика'
    
    saved = db_session.query(Student).filter_by(email='ivan@test.ru').first()
    assert saved is not None
    assert saved.id == student.id
    
    db_session.delete(student)
    db_session.commit()
    
    deleted = db_session.query(Student).filter_by(id=student.id).first()
    assert deleted is None


def test_update_subject(db_session):
    """Тест обновления предмета"""
    
    subject = Subject(
        name='Математика',
        professor='Петров П.П.',
        credits=5
    )
    db_session.add(subject)
    db_session.commit()
    db_session.refresh(subject)
    
    subject_id = subject.id
    
    subject.credits = 6
    subject.professor = 'Сидоров С.С.'
    db_session.commit()
    db_session.refresh(subject)

    assert subject.credits == 6
    assert subject.professor == 'Сидоров С.С.'
   
    updated = db_session.query(Subject).filter_by(id=subject_id).first()
    assert updated.credits == 6
    assert updated.name == 'Математика'
   
    db_session.delete(subject)
    db_session.commit()


def test_delete_student(db_session):
    """Тест удаления студента"""
    student = Student(
        name='Петр Петров',
        email='petr@test.ru',
        course='Физика'
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    
    student_id = student.id
 
    created = db_session.query(Student).filter_by(id=student_id).first()
    assert created is not None
    assert created.name == 'Петр Петров'
  
    db_session.delete(student)
    db_session.commit()
   
    deleted = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted is None