

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
# SUM(quantity *price) as Total_Purchase_Amount
def cus_total_purchase_amt():
    conn=connect_db()
    cursor=conn.cursor()
    query = """
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.quantity * p.price) AS Total_Purchase_Amount

FROM customer_order_pdbc AS c

INNER JOIN customer_order_details AS o
ON c.customer_id = o.customer_id

INNER JOIN product_order_pdbc AS p
ON o.product_id = p.product_id

GROUP BY c.customer_id, c.customer_name

ORDER BY c.customer_id;
    """
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    conn.close()
cus_total_purchase_amt()