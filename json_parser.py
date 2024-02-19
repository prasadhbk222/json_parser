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
    

    
    parsing_key = False
    parsing_value = False

    for i in range(1, input_length - 1):
        
        while not parsing_key or not parsing_value:
            character = s[i]
            # print(ord(c))
            # import pdb
            # pdb.set_trace()
            if character.isspace():
                i += 1
            elif character != '"':
                raise JsonParsingError()
            elif character == '"':
                parsing_key = True
                parsed_key, parsed_value, index = parse_key_value(s, i + 1)

            

    
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
                return json_dict
            except JsonParsingError as e:
                print(e)
                sys.exit(1)
        sys.exit(0)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    main()