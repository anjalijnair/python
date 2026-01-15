def customer_feedback():
    try:
        name=input("please enter your name : ")
        feedback=input("please enter the feedback : ")
        if not name or not feedback:
            raise ValueError("name and feedback cannt be empty")
        print(f"Thank you! ,{name}...")
    except ValueError as e:
        print(f"Error :{e}")
    except Exception as e:
        print(f"An unexpected error occured")
customer_feedback()
