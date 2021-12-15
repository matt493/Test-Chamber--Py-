import requests
import json

url = 'https://emkc.org/api/v1/piston/execute'

src = """
# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
"""
stdin = """

"""
data = {
    "language": "python3",
    "source": src,
    "stdin": stdin,
    "args": []
}

response = requests.request('POST', url, data=data)

print(response.text)
input("Press any key...")