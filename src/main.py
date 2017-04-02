import os

# importing AIBIN seems the change dirs, so get the path now
file = os.path.abspath('aiscript.bin')

import AIBIN
aibin = AIBIN.AIBIN()
aibin.load_file(file)
print(aibin.export_commands('TMCx'))
