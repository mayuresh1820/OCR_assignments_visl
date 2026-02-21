import pandas as pd

#loading excel file into Dataframe
df=pd.read_excel(r"C:\Users\visl2441\workspace\OCR_PRAC\pandas_prac\pandasdata\dummy_excel.xlsx")



#col name lowercase and replace and replace spaces with underscore
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

#remove extra spaces from col values(only strings)
df=df.replace(r"\s+"," ",regex=True)

#strip leading/trailing spaces (on strings)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#convert string vals into lowercase
for col in["customer_name","product","city"]:
    df[col]=df[col].str.lower()

#handle mising val in price col by making it 0
df["price"]=df["price"].fillna(0)

#convert vals in price to int
df["price"]=df["price"].astype(int)

#convert order_date to datetime  format
df["total_amt"]=df["quantity"]*df["price"]

#print total sales per city
total_sales_per_city = df.groupby("city")["total_amt"].sum()
print("Total Sales Per City:")
print(total_sales_per_city)

#top 3 customers by total_amt
top_3_customers = (
    df.groupby("customer_name")["total_amt"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\nTop 3 Customers by Total Amount:")
print(top_3_customers)