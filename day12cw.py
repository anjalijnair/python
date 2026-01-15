import re
def validate_booktitle(title):
    pattern=r"^[a-zA-Z\s]+$"
    if re.match(pattern,title):
        return True
    return False
def validate_publishyear(year):
    pattern=r"^(19|20)\d{2}$"
    if re.match(pattern,year):
        return True
    return False
def main():
    try:
        book_title=input("Enter the book title:")
        publish_year=input("Enter the publication year:")
        if not validate_booktitle(book_title):
            print("Error : Boook title should contain only alphabets and spaces")
        elif not validate_publishyear(publish_year):
            print("Error : publilacton year should be a 4-digit no starting with 19 or 20")
        else:
            print("Book title and publication year are valid")
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        print("program execution is completed")
main()
