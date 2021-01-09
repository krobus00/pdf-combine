from pdf import pdf
import sys
import os
if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[1] == "merge":
            p = pdf(sys.argv[2])
            p.pdfmerger()
        elif(sys.argv[1] == "combine"):
            p = pdf(str(sys.argv[2]))
            p.savetopdf()
        else:
            print("?")
    else:
        print("python main.py merge path\npython main.py combine path")




    