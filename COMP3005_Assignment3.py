import psycopg2
from psycopg2 import sql

# Function to establish a connection to the PostgreSQL database

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="Students",
            user="postgres",
            password="daethaENdgrFAt",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


# Function to retrieve and display all records from the students table

def get_all_students():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error retrieving students:", e)
    finally:
        cursor.close()
        conn.close()


# Function to insert a new student record into the students table

def add_student(first_name, last_name, email, enrollment_date):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        insert_query = sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)")
        cursor.execute(insert_query, (first_name, last_name, email, enrollment_date))
        conn.commit()
        print("Student added successfully.")
    except psycopg2.Error as e:
        print("Error adding student:", e)
    finally:
        cursor.close()
        conn.close()

# Function to update the email address for a student with the specified student_id

def update_student_email(student_id, new_email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE students SET email = %s WHERE student_id = %s")
        cursor.execute(update_query, (new_email, student_id))
        conn.commit()
        print("Email updated successfully.")
    except psycopg2.Error as e:
        print("Error updating email:", e)
    finally:
        cursor.close()
        conn.close()


# Function to delete the record of the student with the specified student_id

def delete_student(student_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        delete_query = sql.SQL("DELETE FROM students WHERE student_id = %s")
        cursor.execute(delete_query, (student_id,))
        conn.commit()
        print("Student deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting student:", e)
    finally:
        cursor.close()
        conn.close()

# Example usage of the functions
if __name__ == "__main__":

    # Example usage

    # add_student("Sam", "Wilson", "sam.wilson@example.com", "2024-03-13")
    # update_student_email(6, "sam.wilson@example.org")
    delete_student(6)
    get_all_students()
