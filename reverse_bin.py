import sys, getopt
'''hex_list = []
with open('daolnwod.zip','rb') as f:
    while True:
        a=f.read(1)
        if(not a):
            break
        hex_list.append(a)
mylist=hex_list[::-1]
filename = 'test_text.zip'
with open(filename, 'wb') as f:
    for value in mylist:
       f.write(value)'''
def reverse_bin(inputfile,outputfile):
    hex_list = []
    with open(inputfile,'rb') as f:
        while True:
            a=f.read(1)
            if(not a):
                break
            hex_list.append(a)
    mylist=hex_list[::-1]
    with open(outputfile, 'wb') as f:
        for value in mylist:
           f.write(value)
    print("complete!")
def main(argv):
    inputfile = ''
    outputfile = ''
    
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print ('reverse_bin.py -i <inputfile> -o <outputfile>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print( 'reverse_bin.py -i <inputfile> -o <outputfile>')
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
    if inputfile == '' or outputfile == '':
       print( 'reverse_bin.py -i <inputfile> -o <outputfile>')
       sys.exit()
    reverse_bin(inputfile,outputfile)
if __name__ == "__main__":
    main(sys.argv[1:])
