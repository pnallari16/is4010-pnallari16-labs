class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        """Calculates the age of the book based on the year 2025."""
        current_year = 2025
        return current_year - self.year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

class EBook(Book):
    def __init__(self, title, author, year, file_size):
        # Use super() to call the Book constructor for shared attributes
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        # Use super() to get the base string and append the file size
        base_info = super().__str__()
        return f"{base_info} ({self.file_size} MB)"

if __name__ == "__main__":
    # 1. Test the base Book class and get_age()
    paper_book = Book("1984", "George Orwell", 1949)
    print("Standard Book:")
    print(paper_book)
    print(f"Age: {paper_book.get_age()} years\n")

    # 2. Test the EBook child class
    my_ebook = EBook("Digital Fortress", "Dan Brown", 1998, 12)
    print("EBook (with file size):")
    print(my_ebook)
    
    # 3. Verify inheritance: EBook uses the Book's get_age() method
    print(f"EBook Age: {my_ebook.get_age()} years")