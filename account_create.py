def create_user_account():
    """***Crete the user account"""
    print("For Creating User Account")

## 1. Get user information
    user_name = input("\nplease enter username :")
    user_email = input("\nplease enter email address :")
    user_password = input("\nplease enter password :")

## 2. Validate inputs
    if not user_name or not user_email or not user_password:
        print("\nplease submit complete information")
        return

## 3. Check password strength
    if len(user_password) < 8 :
        print("\nplease enter more than 8 length password")
        return

## 4. Create user account (simulated)
    print("\nCreating User Account Information")

    print(f"\nConfirmation email address is {user_email}")

    print(f"\nYour account {user_name} is complete creation Done. ")

create_user_account()
