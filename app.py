import re #

def password_strength(Password):
    if len(Password)<8:
        return"Weak Password: Must be Atleast 8 Character"
    if not re.search(r"[A-Z]",Password):
         return"Weak Password: Must be include UPPERCASE Letter"
    if not re.search(r"[a-z]",Password):
         return"Weak Password: Must be include lowercase letter"
    if not re.search(r"\d",Password):
         return"Weak Password: Must be include atleast One Number"
    if not re.search(r"[!@$#%^&*(),.?:{}|<>]",Password):
         return"Weak Password: Must be include Special Character"
    return"Strong Password!"
if __name__ == "__main__":
    user_password = input("Enter Your Password: ")
    result = password_strength(user_password)
    print(result)