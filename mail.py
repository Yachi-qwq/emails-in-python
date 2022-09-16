import smtplib

toaddrs = input("Recever E-mail: ")
fromaddrs = 'your email'
password = 'app password'
well = input("Enter password: ")
lmao = '- ' *15
if well == "177013":
    message = input("Message: ")

    with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(fromaddrs, password)

        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(f"\n your message got sent . . .\n{lmao}\n- Message: [{message}]\n- From: [{fromaddrs}]\n- To: [{toaddrs}]\n{lmao}")
else:
    print(f"\n WRONG PASSWORD\n{lmao}\nAccess denied!!!")
