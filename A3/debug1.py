import pdb
import sys
def dividir(a,b):
    return a/b

try:
    dividir(10,0)
except:
    pdb.post_mortem(sys.exc_info()[2])