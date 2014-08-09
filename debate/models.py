from django.db import models
from debate.evidence import Evidence

#TODO: should buisness logic be outside of the modle?
#TODO: cache the calculated argument state
#TODO: record posting user

# statementst have arguments for and against themselves
# arguments are comprised of statments

class Statement(models.Model):
    text = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text
    
    # a statment is strong becuase for the reasons for it, and weak becuase f the reasons against it
    def validity(self):
        best_for = Evidence.contredicted
        for argumentFor in self.argumentfor_set.all():
            if argumentFor.argument.validity().value >= best_for.value:
                best_for = argumentFor.argument.validity()
        
        best_against = Evidence.contredicted
        for argumentAgainst in self.argumentagainst_set.all():
            if argumentAgainst.argument.validity().value >= best_for.value:
                best_against = argumentAgainst.argument.validity()
        
        if best_for.value >= Evidence.unsupported.value:  # @UndefinedVariable
            if best_against.value >= Evidence.unsupported.value:  # @UndefinedVariable
                return Evidence.conflicting
            else:
                return Evidence.supported
        else:
            if best_against.value >= Evidence.unsupported.value:  # @UndefinedVariable
                return Evidence.contredicted
            else:
                return Evidence.unsupported




class Argument(models.Model):
    pub_date = models.DateTimeField('date published')
    
#     def argumentParts(self):
#         return self.unsorted_parts.all()
#         return self.unsorted_parts.order_by('part')
#     

# an argument is only as strong as its weakest statment
    def validity(self):
        out = Evidence.supported
        for argument_part in self.unsorted_parts.all():
            if argument_part.content.validity().value < out.value: # TODO: make the order part of the enum, so I don't have to keep calling .value
                out = argument_part.content.validity()
            
        # TODO I would like a cleaner way to write this logic
        if len(self.unsorted_parts.all()) == 0:
            return Evidence.wrong
        return out
        
    def __str__(self):
        return 'Argument:'+str(self.id)+ ' ('+str(self.validity())+')'


class ArgumentFor(models.Model):
    statment = models.ForeignKey(Statement)
    argument =  models.ForeignKey(Argument)
    
    
    def __str__(self):
        return 'ArgumentFor:'+str(self.id)


class ArgumentAgainst(models.Model):
    statment = models.ForeignKey(Statement)
    argument =  models.ForeignKey(Argument)
    
    
class ArgumentPart(models.Model):
    part = models.IntegerField('part')
    content = models.ForeignKey(Statement)
    parent =  models.ForeignKey(Argument, related_name='unsorted_parts') #this feels really wrong to me, shouldn't this be defined on the Argument classsss
#TODO: something aroud the modle is fucking this up too,  perhaps that's a thing?
#TODO: create function for this, drop a breakpoint
    
    def __str__(self):
        return 'ArgumentPart:'+str(self.id)
