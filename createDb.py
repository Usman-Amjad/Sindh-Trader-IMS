import sqlite3


def stDatabase():
    con = sqlite3.connect(database=r'std.db')
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, gender TEXT,"
        "contact TEXT)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS locations(lid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, address TEXT)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT,"
        "name TEXT, price INTEGER, qty INTEGER, totalPrice INTEGER, status TEXT, location TEXT)")
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS sellDetails(item_id INTEGER,'''
                '''name TEXT, price INTEGER, qty INTEGER, totalPrice INTEGER, sellerName TEXT, custName TEXT, phoneNo TEXT, location TEXT, discount INTEGER, netPay INTEGER, payType TEXT, sellDate TEXT);''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS creditCustomers(item_id INTEGER,'''
                '''name TEXT, price INTEGER, qty INTEGER, totalPrice INTEGER, sellerName TEXT, custName TEXT, phoneNo TEXT, location TEXT, discount INTEGER, netPay INTEGER, payType TEXT, sellDate TEXT);''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS returnedItems(item_id INTEGER, category TEXT, item_name TEXT, item_price INTEGER, item_qty INTEGER, item_totalPrice INTEGER, item_returnDate TEXT);''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS orders(orderId INTEGER, orderItemName TEXT, perItemPrice FLOAT, orderQty INTEGER, orderTotalPrice FLOAT, orderStatus TEXT, orderDiscount FLOAT, orderNetPrice FLOAT, orderPayType TEXT, orderCustomerName TEXT, orderCustomerPhone TEXT, orderDate TEXT, orderTime TEXT);''')
    con.commit()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS returnedOrders(orderId INTEGER, orderItemName TEXT, perItemPrice FLOAT, orderQty INTEGER, orderTotalPrice FLOAT, orderStatus TEXT, orderDiscount FLOAT, orderNetPrice FLOAT, orderPayType TEXT, orderCustomerName TEXT, orderCustomerPhone TEXT, orderDate TEXT, orderTime TEXT);''')
    con.commit()


stDatabase()
