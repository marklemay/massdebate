massdebate
==========

As much as I love to work on massdebate alone, I happily accept pull requests.

What?
-----
This is a simple web app, that tries to encourage good debate though the user interface.  It is meant to be easy for visitors to oject to specific points in a transparent way. All critisism branches must be dealt with for an argument to be conidered correct.

History
-------
This was a idea I had years ago, and now that I have some freetime I figure why not try it out again.

Why python django?
------------------
I've been wanting to learn python for a wile now.  So that's why the code might be awkward in places.  Also I figured that I'd get more pull requests in django then if I had written it in an experimental nightly build of scala.

TODO:
-----
github
review and delete cruft
 - remove the debug lines
 - spelling
 - kirk code review
top level arguments
authentication
record the submitting user, (use whatever the admin interface does if possible
tox
huroku
sort arguments by validity
inner argument navigation

cloudbees or travis or whatever

readme
authenticate everything
unit tests
enumeration?
huroku
add feedback widgit
add link to github
seed issuetracker with freature requests
 - tags, searching, nice ajax and css, ...
 
jenkins test

what are best practices for commenting? something like javadocs would be nice

review more complicated systems for dealing with.  (lots f thought need to be given becuase these trees could get complicated)
 - nonsequeters
 - external forms of evidence
  - give stronger weight to testable emperical claims?
 - referencing other arguments
  - perhaps in a functional style 
    e.g. 1. "exceptional claims require exceptional evidence"
         used as "Exceptional claims require exceptional evidence.  This is an exceptional claim.  It only has modest evidence"
    2. "nouns of a statment must exist to perform actions"
     "Santa will kill you"
     "nouns of a statment must exist to perform actions. Santa does not exist."
 - mathmatical facts
 - right now there is effectively no reason to give suppoting evidence in depth more then 1.  more powerful supporting evidence types could solve this problem.
 -grey out conversational falavor text? "I agree..."
Aguments to seed:
santa will kill you
you should not wear shoes on consecutive days
the 2014 Boston/Cambrige/Sommervile ballot choices
 - to up the ante, agree to vote wherever the concensus lands (hacker news: "to get my vote, just convince me")

 -test features by seleting them as on or off by defult and seeing what users change the value to
 
random scratch
from django.contrib import admin
from debate.models import Statement
from debate.models import Argument
from debate.models import ArgumentFor
from debate.models import ArgumentPart

a = Argument.objects.get(id=1)
