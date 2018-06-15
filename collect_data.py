# Created by Abhijeet Singh on 15-June-2018

# desired data
name = []
epic = []
price = []
bidPrice = []
askPrice = []
openPrice = []
prevPrice = []
def collect_data(filename):
    filename = str("pages/" + filename)
    f = open(filename, 'r', encoding='utf-8')
    page = f.read()

    global name
    global epic
    global price
    global bidPrice
    global askPrice
    global openPrice
    global prevPrice

    # collect Bid Price
    start_link = page.find('id="bid-price">')
    if start_link == -1:
	    return
    start_quote = page.find('>', start_link)
    start_quote += 1
    end_quote = page.find('<', start_quote)
    bidPrice.append(page[start_quote : end_quote])

    # collect Ask Price
    start_link = page.find('id="ask-price">')
    if start_link == -1:
	    return
    start_quote = page.find('>', start_link)
    start_quote += 1
    end_quote = page.find('<', start_quote)
    askPrice.append(page[start_quote : end_quote])

    # collect Open Price
    start_link = page.find('<th>Open price</th>')
    if start_link == -1:
	    return
    start_quote = page.find('<td>', start_link)
    start_quote += 4
    end_quote = page.find('<', start_quote)
    openPrice.append(page[start_quote : end_quote])

    # collect Prev Price
    start_link = page.find('<th>Prev close</th>')
    if start_link == -1:
	    return
    start_quote = page.find('<td>', start_link)
    start_quote += 4
    end_quote = page.find('<', start_quote)
    prevPrice.append(page[start_quote : end_quote])

    # collect Price
    start_link = page.find('<span id="current-price"')
    if start_link == -1:
	    return
    start_quote = page.find('>', start_link)
    start_quote += 1
    end_quote = page.find('<', start_quote)
    price.append(page[start_quote : end_quote])

    # collect Epic
    start_link = page.find('<h1>')
    if start_link == -1:
	    return
    start_quote = page.find('(', start_link)
    start_quote += 1
    end_quote = page.find(')', start_quote)
    epic.append(page[start_quote : end_quote])

    # collect Name
    start_link = page.find('<h1>')
    if start_link == -1:
	    return
    start_quote = page.find('>', start_link)
    start_quote += 1
    end_quote = page.find('Share', start_quote)
    name.append(page[start_quote : end_quote])

def column_format(df):
    import pandas as pd
    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter("Shares.xlsx", engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    # Get the xlsxwriter worksheet object
    worksheet = writer.sheets['Sheet1']
    # Set the column widths
    worksheet.set_column('A:A', 45)
    worksheet.set_column('C:G', 10)
    writer.save()

def save_to_excel():
    from pandas import DataFrame
    df = DataFrame({'Name': name})
    df['Epic'] = epic
    df['Price'] = price
    df['Bid Price'] = bidPrice
    df['Ask Price'] = askPrice
    df['Open Price'] = openPrice
    df['Prev Price'] = prevPrice
    #df.to_excel('Shares.xlsx', sheet_name='sheet1', index=False)
    column_format(df)

# Main program
# traverse shares dataset
import os
for dirs,dirlist,filenames in os.walk("pages/"):
    for filename in filenames:
        if filename.endswith(".html") or filename.endswith(".HTML"):
            print("Working on", filename)
            collect_data(filename)

save_to_excel()