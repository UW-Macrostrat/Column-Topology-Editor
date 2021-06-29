from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

#from settings import DATABASE
from utils import run_sql_file, run_sql, run_query


here = Path(__file__).parent
fixtures = here / "fixtures"
procedures = here / "procedures"

class Database:

    engine = create_engine("postgresql://postgres@localhost:54321/geologic_map", echo=True)
    Session = sessionmaker(bind=engine)

    @classmethod
    def run_sql_file(cls, sql_file, params={}, **kwargs):
        return run_sql_file(sql_file, params=params, session=cls.Session(), **kwargs)
    
    def run_sql_string(self, sql_string):
        '''Dangerous method'''
        return self.Session().execute(sql_string)
    
    @classmethod
    def exec_query(cls, filename_or_query, **kwargs):
        """
            Returns a Pandas DataFrame from a SQL query
            need to pass query as sql
        """
        return run_query(cls.engine, filename_or_query, **kwargs)

    @classmethod
    def print_hello(cls):
        '''Class method to test if I have imported database class'''
        print("Hello")