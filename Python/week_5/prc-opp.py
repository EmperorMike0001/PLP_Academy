from datetime import datetime


class Customer :
    def __init__ (self, name , level , membership_type, ):
        self.name= name
        self.level = level
        self.membership_type = membership_type
        
    def paid (self ):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Dear {self.name},\nYou have renewed your {self.membership_type} package on {current_date}"
    def printallcustomers(customers):
            for customer in customers:
                 print(f"name : {customer.name}, level : {customer.level}, memmbership : { customer.membership_type}") 
   





'''
c = customer("mike", "1","gold")
print(c.name, c.membership_type, )

c2 = customer("yvonne", "1","gold")
print(c2.name, c2.membership_type, )'''

customers = [Customer("mike", "1","gold"),
             Customer("yvonne", "1","gold"),
             Customer("gio", "1","silver")
             ]


print(customers[1].name, )


Customer.printallcustomers(customers)

print(customers[0].paid())