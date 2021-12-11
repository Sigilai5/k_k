import pandas as pd



def main(file_path,n):
    cust_data = pd.read_csv(file_path)
    unique_rows = cust_data["Customer ID"].unique()
    cust_ids  = []
    cust_amount = []
    for cust_id in unique_rows:
        user_data = cust_data[cust_data["Customer ID"] == cust_id]
        total_amount = user_data['Transaction Amount'].sum()
        cust_ids.append(cust_id)
        cust_amount.append(total_amount)
    user_dict = dict( zip(cust_ids,cust_amount) )
    best_customers = sorted(user_dict,key=user_dict.get, reverse=True)[:n]

    print(sort(best_customers))

#Function to Sort Customer ID alphanumerically
def sort(lst):
    lst.sort(key = str)
    return lst

if __name__ == '__main__':
    main("transaction_data_1.csv",n=2)
