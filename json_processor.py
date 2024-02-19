from typing import Tuple, Any


def valid_brackets(json_string) -> bool:
    
    stack = []
    for char in json_string:
        if char in ['{', '[']:
            stack.append(char)
        elif char in ['}', ']']:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if (opening_bracket == '{' and char != '}') or (opening_bracket == '[' and char != ']'):
                return False
    return len(stack) == 0


def check_first_and_last(json_string: str) -> bool:

    opening_brackets = {'{' : '}',
                        '[': ']' }

    # import pdb
    # pdb.set_trace()

    if json_string[0] not in opening_brackets.keys() or json_string[-1] not in opening_brackets.values():
        return False
    
    if opening_brackets.get(json_string[0]) != json_string[-1]:
        return False
    
    return True


def parse_key_value(json_string: str, index: int) -> Tuple[str, Any, int]:

    # parse key
    key, end_of_key = parse_key(json_string, index)
    if end_of_key >= len(json_string):
        raise JsonParsingError
    print(f'{key} {end_of_key}')

    #find colon
    colon_index = end_of_key + 1
    while  colon_index < len(json_string) and json_string[colon_index] != ':':
        colon_index += 1

    

    print(colon_index)

    #parse value
    value_start_index = colon_index + 1

    while value_start_index < len(json_string) and json_string[value_start_index].isspace():
        value_start_index += 1

    print(value_start_index)




def parse_key(json_string:str, index:int) -> Tuple[str, int]:

    end_of_key = index
    while end_of_key < len(json_string) and json_string[end_of_key] != '"':
        end_of_key += 1

    if end_of_key >= len(json_string):
        raise JsonParsingError('error in key parsing')

    key = json_string[index : end_of_key]

    return key, end_of_key


    





class JsonParsingError(Exception):

    def __init__(self, message="Error in parsing json"):
        self.message = message
        super().__init__(self.message)