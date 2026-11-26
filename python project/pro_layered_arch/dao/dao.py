from model.claim import Claim
from model.item import Item
from model.user import User

from database.connectivity import get_connection
# 1-User RFegistration
# 2-User Login
# 3-Exit

# USER DASHBOARD
# 1-Report Lost Item
# 2-Report Found Item
# 3-View Lost Items
# 4-View Found Items
# 5-Search Items
# 6-View My Reports
# 7-Submit Claim
# 8-View My Claims

class Dao:
    def __init__(self):
        self.con=get_connection()
    def regi(self):
        cur=self.con.cursor()
        query=""

        
