from model import Base
from connection import engine
Base.metadata.create_all(engine)