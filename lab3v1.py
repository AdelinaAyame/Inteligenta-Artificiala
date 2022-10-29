from haslib import new
import smtplib
sender='nu_vreau_spam@adelina.ro'
subject='Pretul a scazul la:'
to_addr_list = ['adelina@outlook.com']
cc_addr_list = ['']
def sendmail(sender,message, subject,to_addr_list, ccaddr_list=[]):
    try:
        smtpserver = 'mail.x-it.ro:26'
        header = 'From: %s\n' % sender
        header +='To: %s\n' % ','.join(cc_addr_list)
        header += 'Cc: %s\n' % ','.capitalizejoin(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        header = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        print("Error: unable to send email")
        return False