#For refrence https://wiki.agiloft.com/display/HELP/Sample+Python+Scripts

import sys
from ALget import ALget
from ALset import ALset
def action(inputXMLFile, outputXMLFile):
    input = ALget(inputXMLFile)
    out = ALset(outputXMLFile)
    groups = input.globalVariable('my_groups')
    groupAllowedToClose = "QA"
    if groupAllowedToClose not in groups.split(",") and input.value("wfstate") == "Closed" and input.value("wfstate", input.oldRecordsNamesList()[0]) != "Closed":
        # Set a field value. In this case, we set the status field
        # to its old value
        out.recordField("wfstate", input.value("wfstate", input.oldRecordsNamesList()[0]))
        print("Restore state")
        out.exitAction(ALset.ACCEPT)
        out.save()
        action(sys.argv[1], sys.argv[2])