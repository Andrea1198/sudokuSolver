print("# Initializing Packages..")
from time import process_time
tic = process_time()
from src.initPygame import start
print("# Time to import:    ", process_time()-tic)
print("# Starting..")
start()
