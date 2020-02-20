import random 
import string 
  
# defining function for random 
# string id with parameter 
def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for x in range(size)) 

class item(object):
    """description of class"""
    def __init__(self, name, description, value, useType="Use", use=None):
        self.name = name
        self.description = description
        self.value = value
        self.useType = useType
        self.id = (ran_gen(8, "AEIOSUMA23"))
        if use == None:
            self._use = {"msg":"Nothing happened", "action":"none"}
        elif use != None:
            self._use = use
    def use(self):
        return self._use
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}".format(self.name, self.description, self.value)
class Phone(item):
    def __init__(self):
        super(Phone, self).__init__(name="Phone",
                             description="An old phone, with your name written on the back.",
                             value=20,
                             useType = "Check",
                             use= {"msg":"No missed calls", "action":"none"}),
class Bar(item):
    def __init__(self, added=''):
        super(Bar, self).__init__(name="Bar" + added,
                             description="Restores 6 HP.",
                             value=4,
                             useType = "Consume",
                             use = {"msg":"You consumed the Bar. 6 HP gained.", "action":"heal_6"})

