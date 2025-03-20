import json

class BookCollection:
    """A class to manage a collection of book, allowing users to store and organize their reading material."""
    def __init__(self):
        """initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "book_data.json"
        self.read_from_file()
    
    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)
    
    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input('Book Title: ')
        book_author = input('Author: ')
        publishing_year = input("Publishing Year: ")
        book_genre = input("Genre: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
        "title": book_title,
        "author": book_author,
        "year": publishing_year,
        "genre": book_genre,
        "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print(f"Added '{book_title}' to the book collection.\n")

    def delete_book(self):
        """Search for books in the collection by title or author name."""
        book_title = input("Enter title or author name to remove: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print(f"Book {book_title} removed successfully")
                return 
        print("Book not found!\n")
    
    

    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Search text term: ").lower()
        found_books = [
            book 
            for book in self.book_list
                if search_text in book["title"].lower()
                or search_text in book["author"].lower() 
        ]

        if found_books:
            print("Book found: ")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} - {book['year']} - {reading_status}"
                    )
        else:
            print("No books found matching your search.")
        
    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input("Enter new book title: ")
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book['author']
                )
                book["year"] = (
                    input(f"New year ({book['year']}): ") or book['year']
                )
                book["genre"] = (
                    input(f"New genre ({book['genre']}): ") or book['genre']
                )
                book["read"] = (
                    input(f"Have you read this book? (yes/no): ").strip().lower() == "yes"
                )
                self.save_to_file()
                print("Book details updated successfully.")
                return
        print("Book not found.")

    def show_all_book(self):
        """Display all books in the collection with their details."""
        if not self.book_list:
            print("No books in the collection.")
            return
        print("Your book collection.")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index} - ({book['title']}) by ({book['author']}) - ({book['year']}) - ({book['genre']}) {reading_status}"
            )
        print()

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_book = len(self.book_list)
        completed_book = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_book / total_book * 100) if total_book > 0 else 0
        )
        print(f"Total book in collection: {total_book}")
        print(f"Completed books: {completion_rate:.2f}%\n")

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("Welcome to our book collection manager!")
            print("1. Add a new book to collection")
            print("2. Remove a book from collection")
            print("3. Search for a book")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Kindly enter your choice: ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_book()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using our book collection manager. Goodbye!")
                break
            else:
                print("Invalid choice.\nBook not found.")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
