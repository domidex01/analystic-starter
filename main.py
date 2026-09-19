from pydantic import BaseModel
import duckdb
import pandas as pd


class Sale(BaseModel):
    item: str
    qty: int
    price: float


# 1. Pydantic: validate raw data
sales = [Sale(item=item, qty=qty, price=price)
         for item, qty, price in [("apple", 3, 1.2), ("pear", 2, 0.8), ("apple", 1, 1.2)]]

# 2. Pandas: turn validated models into a table
sales_df = pd.DataFrame([s.model_dump() for s in sales])

# 3. DuckDB: query it with SQL
df = duckdb.sql("SELECT item, SUM(qty * price) AS revenue FROM sales_df GROUP BY item ORDER BY revenue DESC").df()

# 4. Show the result
print(df)
