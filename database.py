
import sqlite3


class Database:
    def __init__(self, db):
        self.new = sqlite3.connect(db)
        self.newcur = self.new.cursor()
        sqlupdate = """
        CREATE TABLE IF NOT EXISTS empolyees (
            id integer Primary Key,
            name text , 
            email text,
            age text ,
            phone integer,
            address text ,
            gender text,
            job text
        )
        """
        self.newcur.execute(sqlupdate)
        self.new.commit()

    def insert(self, name, email, age, phone, address, gender, job):
        self.newcur.execute('insert into empolyees Values (NULL ,?,?,?,?,?,?,?) ',
                            (name, email, age, phone, address, gender, job))
        self.new.commit()

    def display(self):
        self.newcur.execute('SELECT * FROM empolyees')
        rowdata = self.newcur.fetchall()
        return rowdata

    def remove(self, id):
        self.newcur.execute("delete from empolyees  where id=?", (id,))
        self.new.commit()

    def update(self, id, name, email, age, phone, address, gender, job):
        self.newcur.execute('update empolyees set name= ? ,email= ? , age= ?,phone=?,address=?,gender=?,job=? where id =?',
                            (name, email, age, phone, address, gender, job, id))
        self.new.commit()
