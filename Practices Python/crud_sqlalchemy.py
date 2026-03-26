from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create database engine
engine = create_engine('sqlite:///crud_app.db')
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# CREATE
def create_user(name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} created successfully!")

# READ
def get_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user

# UPDATE
def update_user(user_id, name=None, email=None):
    user = get_user(user_id)
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        print(f"User {user_id} updated successfully!")

# DELETE
def delete_user(user_id):
    user = get_user(user_id)
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user_id} deleted successfully!")

if __name__ == "__main__":
    create_user("John Doe", "john@example.com")
    create_user("Jane Smith", "jane@example.com")
    
    user = get_user(1)
    if user:
        print(f"Found: {user.name} - {user.email}")
    
    update_user(1, name="John Updated")
    delete_user(2)