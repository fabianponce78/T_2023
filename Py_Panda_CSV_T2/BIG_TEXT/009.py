'''
Created on Mar 30, 2023

@author: fponce
'''
import json

def main():

    # creating JSON array
    j_String = '{"Gaurav":"Pro-Coder","Car":"Ferrari","Home":"Seattle"}'

    # changing JSON string into a JSON object
    j_Object = json.loads(j_String)
    
    print(j_Object)

    # printing keys and values
    for i in j_Object:
        value = j_Object[i]
        print("Key and Value pair are ({}) = ({})".format(i, value))
        print(i, '---', value)

    pass

if __name__ == '__main__':
    main()