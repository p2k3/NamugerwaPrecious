import sqlite3
import re


class ContactManager:

    def __init__(self):
        self.conn = sqlite3.connect("contacts.db")
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT
                )
            """)

    # -------------------------
    # Validation Methods
    # -------------------------

    def validate_phone(self, phone):
        pattern = r'^[+\d-]+$'

        if re.match(pattern, phone):
            return True

        print("Error: Phone number can only contain digits, '+' and hyphens.")
        return False

    def validate_email(self, email):

        if email == "":
            return True

        if "@" in email and "." in email:
            return True

        print("Error: Invalid email address.")
        return False

    # -------------------------
    # CRUD Methods
    # -------------------------

    def add_contact(self, name, phone, email=""):

        if not self.validate_phone(phone):
            return

        if not self.validate_email(email):
            return

        with self.conn:
            self.conn.execute(
                "INSERT INTO contacts(name, phone, email) VALUES (?, ?, ?)",
                (name, phone, email)
            )

        print("Contact added successfully.")

    def view_contact(self, contact_id):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM contacts WHERE id=?",
            (contact_id,)
        )

        contact = cursor.fetchone()

        if contact:
            self.display_contacts([contact])
        else:
            print("Contact not found.")

    def update_contact(self, contact_id, name=None, phone=None, email=None):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM contacts WHERE id=?",
            (contact_id,)
        )

        contact = cursor.fetchone()

        if not contact:
            print("Contact not found.")
            return

        if phone and not self.validate_phone(phone):
            return

        if email and not self.validate_email(email):
            return

        new_name = name if name else contact[1]
        new_phone = phone if phone else contact[2]
        new_email = email if email else contact[3]

        with self.conn:
            self.conn.execute("""
                UPDATE contacts
                SET name=?, phone=?, email=?
                WHERE id=?
            """, (new_name, new_phone, new_email, contact_id))

        print("Contact updated successfully.")

    def delete_contact(self, contact_id):

        with self.conn:
            self.conn.execute(
                "DELETE FROM contacts WHERE id=?",
                (contact_id,)
            )

        print("Contact deleted successfully.")

    # -------------------------
    # Search & Display Methods
    # -------------------------

    def display_contacts(self, contacts):

        if not contacts:
            print("No contacts found.")
            return

        print("\n===== CONTACTS =====")

        for contact in contacts:
            print(f"ID    : {contact[0]}")
            print(f"Name  : {contact[1]}")
            print(f"Phone : {contact[2]}")
            print(f"Email : {contact[3]}")
            print("-" * 30)

    def search_contacts(self, keyword):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT * FROM contacts
            WHERE name LIKE ?
            OR phone LIKE ?
            OR email LIKE ?
        """, (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        results = cursor.fetchall()

        self.display_contacts(results)

    def list_contacts(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM contacts")

        contacts = cursor.fetchall()

        self.display_contacts(contacts)


# -------------------------
# CLI Menu
# -------------------------

def main():

    manager = ContactManager()

    while True:

        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":

            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")

            manager.add_contact(name, phone, email)

        elif choice == "2":

            contact_id = int(input("Enter Contact ID: "))
            manager.view_contact(contact_id)

        elif choice == "3":

            contact_id = int(input("Enter Contact ID: "))

            name = input("New Name (leave blank to keep current): ")
            phone = input("New Phone (leave blank to keep current): ")
            email = input("New Email (leave blank to keep current): ")

            manager.update_contact(
                contact_id,
                name if name else None,
                phone if phone else None,
                email if email else None
            )

        elif choice == "4":

            contact_id = int(input("Enter Contact ID: "))
            manager.delete_contact(contact_id)

        elif choice == "5":

            keyword = input("Enter search term: ")
            manager.search_contacts(keyword)

        elif choice == "6":

            manager.list_contacts()

        elif choice == "7":

            print("Goodbye!")
            break

        else:

            print("Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    main()