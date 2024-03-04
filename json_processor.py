from typing import Tuple, Any

def is_empty_json(json_string: str) -> bool:
    # Strip leading and trailing whitespace and spaces
    stripped_json = json_string.strip().replace(" ", "")
    # Return True if the stripped string is '{}'
    return stripped_json == '{}'



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

    key = None
    value = None
    # parse key
    key, end_of_key = parse_string(json_string, index + 1)
    if end_of_key >= len(json_string):
        raise JsonParsingError()

    #find colon
    colon_index = end_of_key + 1
    while  colon_index < len(json_string) - 1 and json_string[colon_index] != ':':
        if json_string[colon_index].isspace():
            colon_index += 1
        else:
            raise JsonParsingError()

    


    #parse value
    value_start_index = colon_index + 1

    while value_start_index < len(json_string) - 1 and json_string[value_start_index].isspace():
        value_start_index += 1

    # print(value_start_index)

    # value is a string
    if json_string[value_start_index] == '"':
        value, end_of_value = parse_string(json_string, value_start_index + 1)
        substring =  json_string[end_of_value:]
        comma_index = substring.find(',')
        if comma_index == -1:
            # parsing complete
            return key, value, -1
        
        return key, value, end_of_value + comma_index



    elif json_string[value_start_index] == 't' or json_string[value_start_index] == 'f' or json_string[value_start_index] == 'n':

        substring = json_string[value_start_index:]
        comma_index = substring.find(',')

        if comma_index == -1:
            end_index = len(substring) - 1
        else:
            end_index = comma_index
        
        resultant = substring[: end_index].strip()

        if resultant == 'true':
            value = True
        elif resultant == 'false':
            value = False
        elif resultant == 'null':
            value = None
        else:
            raise JsonParsingError()
        
        if comma_index == -1:
            # parsing complete
            return key, value, -1

        return key, value, value_start_index + comma_index
    
    elif json_string[value_start_index].isnumeric() or json_string[value_start_index] == '-':
        substring = json_string[value_start_index:]
        comma_index = substring.find(',')

        if comma_index == -1:
            end_index = len(substring) - 1
        else:
            end_index = comma_index
        
        resultant = substring[: end_index].strip()

        numeric_value =  parse_int_or_float(resultant)

        if comma_index == -1:
            # parsing complete
            return key, numeric_value, -1

        return key, numeric_value, value_start_index + comma_index
    
    else:
        raise JsonParsingError("Unexpected value")





        


def parse_int_or_float(s: str):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            raise JsonParsingError("Failed to parse as integer or float: {}".format(s))
    
    
    





def parse_string(json_string:str, index:int) -> Tuple[str, int]:

    end_of_key = index
    substring = json_string[index:]
    string_end_index = substring.find('"')
    if string_end_index == -1:
        raise JsonParsingError()
    value = substring[: string_end_index]
    return value, index + len(value)
    # while end_of_key < len(json_string) and json_string[end_of_key] != '"':
    #     end_of_key += 1

    # if end_of_key >= len(json_string):
    #     raise JsonParsingError('error in key parsing')

    # key = json_string[index : end_of_key]

    # return key, end_of_key


    





class JsonParsingError(Exception):

    def __init__(self, message="Error in parsing json"):
        self.message = message
        super().__init__(self.message)