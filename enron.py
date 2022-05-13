"""
This program parses through 10,000 Enron emails, pulling out the important
information in each email (Message-ID, subject, date, etc.)
"""
import argparse
import sys
import re

class Server:
    """
    This class stores the data for all emails found in the dataset.
    
    Attributes:
        emails (object): A list of email objects where each object 
        corresponds to one email.
    """
    def __init__(self, path):
        """
        Opens the file specified by the path for reading 
        and set the emails attribute  to  a  list  containing  Email  objects.  
        Each  email  instance  should  correspond  to each individual email found 
        in the text file.
        
        Args:
            self
            Path(String): The path to the file that we are going to read.
        
        """
        self.emails = []
        #Opens the file
        with open(path, 'r', encoding='utf-8') as f:
            file = f.read()
            #Separates each email
            split_file = file.split("End Email")
            split_file = split_file[:-1]
           
            
        for email in split_file:
            message_id = re.search(r"(?:Message-ID:) (<.+>)", email)
            if message_id == None:
                message_id = ' '
            else:
                message_id = message_id.groups()
            
                        
            date = re.search(r"(?:Date:) (.*)", email)
            if date == None:
                date = ' '
            else:
                date = date.groups()
            
            subject = re.search(r"(?:Subject:)(.*)", email)
            if subject == None:
                subject = ' '
            else:    
                subject = subject.groups()
            
            sender = re.search(r"From: (\w*.\w*.\w*.com)", email)
            if sender == None:
                sender = ' '
            else:
                sender = sender.groups()
            
            receiver = re.search(r"To: (\w*.\w*@\w*.com)", email)
            if receiver == None:
                receiver = ' '
            else:
                receiver = receiver.groups()
            
            body = re.search(r'FileName((?:.*?\n?)*)\n', email)
            if body == None:
                body = ' '
            else:
                body = body.groups()


            self.emails.append(Email(message_id, date, subject, sender, receiver, body))
       
class Email:
    """
    This class stores the data related to individual email messages.
    
    Attributes:
        message_id (String): The message-id that is unique to each email message. 
        
        date (String):  The  date  associated  with  each  email  message. 
        
        subject (String): The subject of each email message.
        
        sender (String): The sender of each email message.
        
        receiver (String): The receiver of each email message.
        
        body (String): The body message of each email message. 

    """
    def __init__(self, message_id, date, subject, sender, receiver, body):
        """
        Sets the parameters to the corresponding attributes.
        
        Args:
            message_id - A string representing the message_id
            date - A string representing the date of the email.
            subject - A string representing the subject of the email.
            sender - A string representing the email address of the sender.
            receiver - A string representing the email address of the receiver.
            body - A string representing the body text of the email.
        """
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body
            
def main(path):
    """
    Create an instance of server-class using the path that was passed 
    in and save that to a variable.
    
    Args:
        Path (String): Represents the path of the text file that will be parsed.
        
    Returns:
        An integer, the length of the emails attribute of that instance.
    """
    server_test = Server(path)
    return len(server_test.emails)

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as 
        arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('path', type = str, help = 'The path to the file.')
    
    
    args = parser.parse_args(args_list)
    
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.path)
    
        
        
