class DotException(Exception):
    pass
class AtTheRateException(Exception):
    pass
class DomainException(Exception):
    pass
def validate_email(email):
    if email.count('@')>1:
        raise AtTheRateException
    if not email.endswith('.com') or email.endswith('.in') or email.endswith('.org') or email.endswith('.net'):
        raise DomainException

email=input("enter the mail here:")
try:
    validate_email(email)
    print("valid email")
except DotException as e:
    print("")
except AtTheRateException as e:
    print("only one at the rate require")
except DotException as e:
    print("domain is not right")