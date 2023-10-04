# define a class Book with 3 properties: title, author, page_count
# define a class attribute all that stores all objects
    # when should this attribute be initialized? when should it be used?
# define 3 class methods: get_all_books that returns all books,
#                         get_avg_page_count that returns the mean page count,
#                         get_longest that returns the longest book
    # what are two ways of defining these class methods?

import statistics # necessary if using mean() function

class Book:

    all = [] # class attribute (for class Book, not instances of class Book)

    '''
        constructor for objects
    '''

    # constructor
    def __init__(self, title, author, page_count):
        self._title = title
        self._author = author
        self._page_count = page_count

        Book.all.append(self) # upon creation of object, appends object to class attribute

    '''
        properties for objects
    '''

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title
        else:
            raise Exception("The title must be a string!")
        
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        # if isinstance(author, str) and len(author) > 4:
        if type(author) == str and len(author) > 4:
            self._author = author
        else:
            raise Exception("The author must be a string of greater than 4 characters!")
        
    author = property(get_author, set_author)

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        # if type(page_count) == int and page_count > 0:
        if isinstance(page_count, int) and page_count > 0:
            self._page_count = page_count
        else:
            raise Exception("Page count must be a positive integer!")
        
    # these could be used to check if number (integer or float) were acceptable
    # if type(page_count) == int or type(page_count) == float:
    # if isinstance(page_count, int) or isinstance(page_count, float):
        
    '''
        class methods
    '''
    
    def get_all_books():
        """
            returns list of all book objects
        """
        return Book.all
    
    @classmethod
    def get_longest(cls):
        """
            calculates maximum page count of all book objects
            and returns book object associated with that page count
        """
        max_page_count = 0
        max_page_count_book = None

        for book in cls.all:
            page_count = book.page_count
            if page_count > max_page_count:
                max_page_count = page_count
                max_page_count_book = book

        return max_page_count_book

        max_page_count_book = max([book for book in Book.all], key = lambda book : book.page_count)

        return max_page_count_book
    
    @classmethod
    def get_avg_page_count(cls):
        """
            calculates mean/average page count of all book objects
            and returns that page count integer
        """

        sum_page_counts = 0

        for book in cls.all:
            sum_page_counts = sum_page_counts + book.page_count # sum_page_counts += book.page_count

        avg = sum_page_counts / len(cls.all)

        return avg

        avg = sum([book.page_count for book in cls.all]) / len(cls.all)

        return avg

        avg = statistics.mean([book.page_count for book in cls.all])

        return avg
        
    '''
        printable overriding magic method
    '''    

    # similar to __str__()
    # allows human-readable version of object when object is printed
    def __repr__(self):
        return f"Title: {self.title}"

'''
    instances of Book class/Book objects
'''

twilight = Book("Twilight", "Stephanie Meyer", 430)
new_moon = Book("New Moon", "Stephanie Meyer", 375)
eclipse = Book("Eclipse", "Stephanie Meyer", 500)
breaking_dawn = Book("Breaking Dawn", "Stephanie Meyer", 520)

print("Longest book: " + Book.get_longest().title)
print("Average page count: " + str(Book.get_avg_page_count()))

second_life = Book("The Short Second Life of Bree Tanner", "Stephanie Meyer", 120)

print("Longest book: " + Book.get_longest().title)
print("Average page count: " + str(Book.get_avg_page_count()))