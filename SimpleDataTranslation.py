import csv

# Define the data
books = [
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'Animal Farm', 'author': 'George Orwell'},
    {'title': 'Brave New World', 'author': 'Aldous Huxley'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
    {'title': 'One Hundred Years of Solitude', 'author': 'Gabriel Garcia Marquez'},
    {'title': 'To the Lighthouse', 'author': 'Virginia Woolf'},
    {'title': 'The Bell Jar', 'author': 'Sylvia Plath'},
    {'title': 'Invisible Man', 'author': 'Ralph Ellison'},
    {'title': 'The Sound and the Fury', 'author': 'William Faulkner'},
    {'title': 'A Clockwork Orange', 'author': 'Anthony Burgess'},
    {'title': 'The Color Purple', 'author': 'Alice Walker'},
    {'title': 'Beloved', 'author': 'Toni Morrison'},
    {'title': 'Slaughterhouse-Five', 'author': 'Kurt Vonnegut'},
    {'title': 'Catch-22', 'author': 'Joseph Heller'},
    {'title': 'The Hitchhiker\'s Guide to the Galaxy', 'author': 'Douglas Adams'},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'},
    {'title': 'Harry Potter and the Philosopher\'s Stone', 'author': 'J.K. Rowling'},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien'}
]

# Write the data to a CSV file
with open('books.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'author']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for book in books:
        writer.writerow(book)