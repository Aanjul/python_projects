# For Refrence https://wiki.agiloft.com/display/HELP/Sample+Python+Scripts



######################################################################
# Synopsis:
#
# Redirect the user after he/she submits the ticket.
#
# There is no need to specify the Python interpreter if the script is named *.py
# because the system recognizes .py scripts as being Python based and will
# use the Python that is included in the distribution.
#
# If you use this script with your own copy of Python, please note that
# it requires ElementTree module to be installed
#
######################################################################

import sys
from ALget import ALget
from ALset import ALset

def action(inputXMLFile, outputXMLFile):
    input = ALget(inputXMLFile)
    out = ALset(outputXMLFile)
    ######################################################################
    #
    # Only log the user out if he/she is not a member of the Staff
    # group. In other words, we want all members of staff to be able
    # to log tickets on behalf of users without being logged out.
    ######################################################################


 groups = input.globalVariable('my_groups')
 groupAllowedToClose = "Staff"
 if groupAllowedToClose not in groups.split(","):
     out.redirect("http://www.example.com")
     out.exitAction(ALset.ACCEPT_REDIRECT)
     else:
         out.exitAction(ALset.ACCEPT)
         out.save()
         action(sys.argv[1], sys.argv[2])
