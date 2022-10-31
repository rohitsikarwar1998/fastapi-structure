from curses import echo
from sqlalchemy.orm import sessionmaker, session
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DB_URL = 'postgresql+psycopg2://rohit:sikarwar@localhost/practice'


class SessionFactory:
    """A convenience wrapper over SQLAlchemy orm.sessionmaker instance"""

    _SESSION_FACTORY: session.Session = None

    @classmethod
    @contextmanager
    def get_session(cls):
        """Returns a new SQLAlchemy session.
        The returned object can also be used as a session manager.
        """

        if not cls._SESSION_FACTORY:
            db_engine = create_engine(DB_URL, echo=True)
            sess = sessionmaker(expire_on_commit=False)
            sess.configure(bind=db_engine)
            cls._SESSION_FACTORY = sess

        if not cls._SESSION_FACTORY:
            raise Exception("Improperly configured")

        session = cls._SESSION_FACTORY()  # pylint: disable=not-callable
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


def create_tables():
    engine = create_engine(DB_URL, echo=True)
    Base.metadata.create_all(bind=engine)
