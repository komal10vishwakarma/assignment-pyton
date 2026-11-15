from connectivity import connect_db


# 9. CUSTOMER-WISE TOTAL PURCHASE AMOUNT
# --------------------------------------

# REQUIRED SQL CONCEPTS
# ---------------------
# INNER JOIN
# GROUP BY
# SUM()
# ORDER BY

# Required output columns:
# Customer ID, Customer Name, Total Purchase Amount

# EXPECTED OUTPUT
# ---------------
# Customer ID  Customer Name  Total Purchase Amount
# --------------------------------------------------
# 1            Amit           56600.00
# 2            Priya           1500.00
# 3            Rahul          24500.00
# 4            Neha           55000.00
# 5            Karan           200.00

# Formula:
# SUM(order_quantity * product_price) as Total_Purchase_Amount
def cus_toal_purchase_amt():
    conn=connect_db()
    cursor=conn.cursor()
    query=""