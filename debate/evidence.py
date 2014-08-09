from enum import Enum

# TODO: what is the idomatic way to do this in python?
# TODO: doc

class Evidence(Enum):
    wrong = 0 #this should never actually be used
    contradicted = 1
    conflicting = 2 #TODO rename?
    unsupported = 3
    supported = 4
    
    # TODO: where should code like this go?
    def color(self):
        if self == Evidence.wrong:
            return "Violet"
        elif self == Evidence.contradicted:
            return "DarkRed"
        elif self == Evidence.conflicting:
            return "DarkOrange"
        elif self == Evidence.unsupported:
            return "Black"
        elif self == Evidence.supported:
            return "Green"
            

    # statments witch are not contradicted are consitered good
    def isGood(self):
        return self == Evidence.unsupported or self == Evidence.supported