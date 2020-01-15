
contact_emails = {
    'Sue Reyn' : 's.rayn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Mate Arty':'narty042@nmail.com'
}

new_contact = input("Input new_contact: ")
new_email = input("Input email : ")
contact_emails[new_contact] = new_email

for k,v in contact_emails.items():
    print(f"{v} is {k}")

for name in contact_emails:
    # print(f"{name} is {contact_emails[name]}")
    print(f"{contact_emails[name]} is {name}")
