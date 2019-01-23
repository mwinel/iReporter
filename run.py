from api import app
from db.database import DatabaseConnection

db = DatabaseConnection()

if __name__ == "__main__":
    db.create_tables()
    app.run(debug=True)
