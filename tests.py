import pyodbc
import pytest

SERVER = 'EPUAKHAW0118\SQLEXPRESS'
DATABASE = 'AdvetureWorks2012'


@pytest.fixture(scope='session')
def conn():
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};Trusted_Connection=yes;TrustServerCertificate=no;Encrypt=no'
    conn = pyodbc.connect(connectionString)
    yield conn
    conn.close()


def test_address_table_row_count(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM AdventureWorks2012.[Person].[Address]')
    count = cursor.fetchone()[0]
    assert count == 19614
    cursor.close()

def test_document_table_row_count(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM AdventureWorks2012.[Production].[Document]')
    count = cursor.fetchone()[0]
    assert count == 13
    cursor.close()


def test_unitmeasure_table_row_count(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM AdventureWorks2012.[Production].[UnitMeasure]')
    count = cursor.fetchone()[0]
    assert count == 38
    cursor.close()

def test_unitmeasure_table_no_duplicates(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT UnitMeasureCode, Name, COUNT(*) FROM AdventureWorks2012.[Production].[UnitMeasure] GROUP BY UnitMeasureCode, Name HAVING COUNT(*) > 1')
    rows = cursor.fetchall()
    assert len(rows) == 0
    cursor.close()

def test_document_table_no_duplicates(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT DocumentNode, Title, COUNT(*) FROM AdventureWorks2012.[Production].[Document] GROUP BY DocumentNode, Title HAVING COUNT(*) > 1')
    rows = cursor.fetchall()
    assert len(rows) == 0
    cursor.close()

def test_address_table_no_duplicates(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT AddressID, AddressLine1, COUNT(*) FROM AdventureWorks2012.[Person].[Address] GROUP BY AddressID, AddressLine1 HAVING COUNT(*)>1')
    rows = cursor.fetchall()
    assert len(rows) == 0
    cursor.close()
if __name__ == "__main__":
    pytest_args = ['-v', '--html=report.html', __file__]
    pytest.main(pytest_args)
