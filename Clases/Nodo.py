
class Nodo(object):
   
    def __init__(self, id):
        self.id = id
        self.attrs=dict()
        self.connected_to=[]

    def __eq__(self, other):
       
        return self.id == other.id

    def __repr__(self):
        return repr(self.id)

    def __hash__(self):
        return hash(self.id)