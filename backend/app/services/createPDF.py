import psycopg2
import os
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib import colors
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from reportlab.lib.units import inch
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# load_dotenv()

c2e = {
    "藍莓蛋糕": "Blueberry Cake",
    "超好吃牛肉丸": "Super Delicious Beef Balls",
    "油條豆漿": "Fried Dough Sticks with Soy Milk",
    "花生湯": "Peanut Soup",
    "控肉飯": "Braised Pork Rice",
    "雞腿飯": "Chicken Drumstick Rice",
    "紅絲絨蛋糕": "Red Velvet Cake"
}


def fetch_order_data():

    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
        host, user, dbname, password, sslmode
    )
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()

    try:
        start_date = "2024-05-01"
        end_date = "2024-05-30"

        query = """SELECT 
                       orders.user_id,
                       orders.order_id,
                       orders.order_date,
                       orders.order_status, 
                       orders.paid,
                       orders.total_price FROM 
                       orders WHERE 
                       orders.order_date BETWEEN %s AND %s;"""
        cursor.execute(query, (start_date, end_date,))
        orders = cursor.fetchall()

        order_history = []
        for user_id, order_id, order_date, order_status, paid, total_price in orders:
            cursor.execute(
                """SELECT 
                           item_id, 
                           quantity, 
                           price FROM 
                           orders_items WHERE 
                           order_id = %s""",
                (order_id,),
            )
            items = cursor.fetchall()
            item_list = []
            for item_id, quantity, item_total_price in items:
                cursor.execute(
                    "SELECT item_name FROM menus_items WHERE item_id = %s", (item_id,)
                )
                item_name = cursor.fetchall()
                item_list.append(
                    {
                        "item_id": item_id,
                        "item_name": item_name,
                        "quantity": quantity,
                        "unit_price": item_total_price / quantity,
                    }
                )

            cursor.execute('''SELECT username FROM users WHERE user_id = %s''', (user_id,))
            username = cursor.fetchone()[0]
            
            cursor.execute('''SELECT department, position FROM employees WHERE user_id = %s''', (user_id,))
            employee_info = cursor.fetchall()
            department, position = "", ""
            if employee_info != []:
                department, position = employee_info[0][0], employee_info[0][1]
            
            order_history.append(
                {
                    "username": username,
                    "department": department,
                    "position": position,
                    "order_id": order_id,
                    "order_date": order_date.strftime("%Y-%m-%dT%H:%M:%S"),
                    "items": item_list,
                    "total_price": total_price,
                    "order_status": order_status,
                    "paid": paid,
                }
            )

        cursor.close()
        conn.close()
        return order_history
    except Exception as e:
        return str(e)

def generate_pdf(order_history):
    pdf_filename = "order_history.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 14)

    # Define font properties for Chinese characters
    chinese_font = FontProperties(fname="SimSun.ttf")

    logo_path = "./images/logo.png"
    logo_width = 100  
    logo_height = 50  
    
    y = 750
    for order in order_history:
        c.drawString(50, y, "Username: " + order["username"])
        c.drawString(50, y - 15, "Department: " + order["department"])
        c.drawString(50, y - 30, "Position: " + order["position"])
        c.drawString(50, y - 45, "Order ID: " + str(order["order_id"]))
        c.drawString(50, y - 60, "Order Date: " + order["order_date"])
        
        y -= 75

        c.drawImage(logo_path, letter[0] - inch - logo_width, letter[1] - inch, width=logo_width, height=logo_height)
        
        # Draw items
        for item in order["items"]:
            item_name = item["item_name"][0][0] if item["item_name"] else ""
            c.drawString(70, y, "Item: " + c2e[item_name])
            y -= 15
            c.drawString(90, y, "Quantity: " + str(item["quantity"]))
            c.drawString(200, y, "Unit Price: $" + str(item["unit_price"]))
            y -= 15
        
        c.drawString(50, y, "Total Price: $" + str(order["total_price"]))
        c.drawString(50, y - 15, "Order Status: " + order["order_status"])
        c.drawString(50, y - 30, "Paid: " + str(order["paid"]))
        c.drawString(50, y - 45, "===============================================================")
        y -= 60

        if y < 50:
            c.showPage()
            y = 750

    c.save()
    print("PDF generated successfully.")

def send_email():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")

    # real email address to avoid error
    email = [
        "wangbosh0604@gmail.com",
        "estheryangyujie.mg12@nycu.edu.tw",
        "sharon.lin.2001@gmail.com",
        "sharon77.mg12@nycu.edu.tw",
        "willie0310@gmail.com",
        "york1287657@gmail.com",
    ]

    for receiver_email in email:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "[Notification from Meal Provider] Order Report"

        body = (
            "Hi there!\n\nWe're pleased to inform you that your order report is now available. Please find the attached order report for your reference.\n\nThank you!\n\nBest,\nMeal Provider Team"
        )
        message.attach(MIMEText(body, "plain"))

        with open("order_history.pdf", "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=order_history.pdf",
        )
        message.attach(part)

        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(sender_email, password)
                text = message.as_string()
                smtp.sendmail(sender_email, receiver_email, text)
                print(f"Email sent successfully to {receiver_email}!")
            except Exception as e:
                print(f"Failed to send email. Error: {e}")

def pdf_service():
    orders = fetch_order_data()
    generate_pdf(orders)
    send_email()
    return {"message": "PDF generated and email sent successfully."}


