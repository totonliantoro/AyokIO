from sys import argv

def celcius_to_fahr (temp_c):
    converted = temp_c*(9.0/5.0) + 32
    return converted

cels = float (sys.argv[1])
print('celcius_fahr(cels))
      
if __name__ == "__main__":
      dowork()

try:
cels = float (sys.argv[1])
print('celcius_fahr(cels))

except:
print ("First argument must be a number)

