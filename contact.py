class Contact:
    
    contact_list = []

    def __init__(self,first_name,last_name,phone_number,email):
        
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    def save_contact(self):
    
        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)
     def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)
    