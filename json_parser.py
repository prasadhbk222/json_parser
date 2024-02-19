import json
import sys
from typing import Dict, Any
from json_processor import valid_brackets, check_first_and_last, parse_key_value, JsonParsingError

def json_from_string(s: str) -> Dict[str, Any]:

    result = {}

    # remove all leading and trailing whitespace characters
    s = s.strip()
    input_length = len(s)
    cursor = 0



    # minimum valid json length
    if input_length < 2:
        raise JsonParsingError('JSON string length less than 2')
    
    # first and last char should be equal and they should be { or [
    if not check_first_and_last(s):
        raise JsonParsingError('first and last char should be opposite brackets and they should be { or [')
    

    if not valid_brackets(s):
        raise JsonParsingError('Bracket structure not valid')
    

    i = 1
    complete = False
    while i < input_length - 1:
        parsed_key = None
        parsed_value = None
        next_index = -1
        
        while not parsed_key or not parsed_value:
            character = s[i]

            if character.isspace():
                i += 1
            elif character != '"':
                raise JsonParsingError("line 43")
            elif character == '"':
                parsing_key = True
                parsed_key, parsed_value, next_index = parse_key_value(s, i)

        
       
        result[parsed_key] = parsed_value
        print(f'result {result}')

        if next_index == -1:
            complete = True
            break

        else:
            i = next_index + 1




        
        

    if not complete:
        raise JsonParsingError("Incomplete JSON") 

    
    return result




def main():
    if len(sys.argv) != 2:
        print("Usage: python json_validator.py <json_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    try:
        with open(json_file, 'r') as f:
            json_string = f.read()
            try:
                json_dict = json_from_string(json_string)
                print(f'final result: {json_dict}')
            except JsonParsingError as e:
                print(e)
                sys.exit(1)
        sys.exit(0)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    main()