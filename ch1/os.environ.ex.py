# import full os module then run submodules

import os


# retusn full environmental var value
print(os.environ)
# returns only value matching HOME
print(os.getenv('HOME'))
# returns only value matching PROCESSOR_REVISION
print(os.getenv('PROCESSOR_REVISION'))
