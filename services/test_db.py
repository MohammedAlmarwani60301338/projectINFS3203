from services.db import test_connection

if test_connection():
    print("Database is working")
else:
    print("Database not working")