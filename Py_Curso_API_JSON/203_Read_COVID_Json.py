'''
Created on Feb 9, 2023

@author: fponce
'''
import json

str_Line = '___________________________________________________ '
Str_JSON_File = '#_COVID_20230209_165642.JSON'

#####===============================================================================================
#####===============================================================================================

def fn_100_Read_JSON():
    print(str_Line , "fn_01_Read_JSON", str_Line, " START")
    Str_FileName_InPut =  r'.\\JSON\\'+Str_JSON_File
    
    print("Str_FileName_InPut = ", Str_FileName_InPut)
    
    #https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ 
    # Opening JSON file
    f = open(Str_FileName_InPut,)      
    data = json.load(f)      
        
    print('\t data    :    ', data)    
    # Print the type of data variable
    print("\t Type    :    ", type(data))  ##    Type: <class 'list'>
        
    #===========================================================================
    # print('\t data     : ', data[1])
    # print('\t data     : ', data[2])
    # print('\n')
    # print('\t data     : ', data[2]["id"])
    # print('\t data     : ', data[2]["Country"])
    # print('\t data     : ', data[2]["TotalRecovered"])
    #===========================================================================
    with pytest.raises(ValueError, match=msg):
        json_normalize(data, 'data', meta=['foo', 'bar'])

        result = json_normalize(data, 'data', meta=['foo', 'bar'],
                                meta_prefix='meta')

        for val in ['metafoo', 'metabar', 'foo', 'bar']:
            assert val in result    
    


    # Closing file    
    f.close
        
#####===============================================================================================
#####===============================================================================================

def main():
    print(str_Line, "main")

    fn_100_Read_JSON()
    print('\n\n\t------ Done :) \n\n')
    
    
#####===============================================================================================
#####===============================================================================================
if __name__ == "__main__":
    main()