import yagmail

sender_email = 'seth.benson.test.email@gmail.com'
receiver_email = ''
subject = "JAMES ARE YOU IMPRESSED???"
sender_password = 'test123test'

yag = yagmail.SMTP(user=sender_email, password=sender_password)

contents = [
  "James",
  "James",
  "James",
]

yag.send(receiver_email, subject, contents)