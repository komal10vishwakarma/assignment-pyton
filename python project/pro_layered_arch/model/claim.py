
# +---------------+---------------------------------------+------+-----+-------------------+-------------------+
# | Field         | Type                                  | Null | Key | Default           | Extra             |
# +---------------+---------------------------------------+------+-----+-------------------+-------------------+
# | claim_id      | int                                   | NO   | PRI | NULL              | auto_increment    |
# | item_id       | int                                   | NO   | MUL | NULL              |                   |
# | user_id       | int                                   | NO   | MUL | NULL              |                   |
# | claim_message | text                                  | NO   |     | NULL              |                   |
# | claim_status  | enum('PENDING','APPROVED','REJECTED') | YES  |     | PENDING           |                   |
# | created_at    | timestamp                             | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
# +---------------+---------------------------------------+------+-----+-------------------+-------------------+

class Claim:
    def __init__(self,claim_message ,claim_status):
        self.claim_message=claim_message
        self.claim_status=claim_status
        