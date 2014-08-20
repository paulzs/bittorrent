class BencodeError(Exception): pass

def bencode(data):
    if isinstance(data,int):
        return "i" + str(data) +"e"
    elif isinstance(data,str):
        return str(len(data)) + ":" + data
    elif isinstance(data,list):
        string = "l"
        for element in data:
            string += bencode(element)
        string = string + "e"
        return string
    elif isinstance(data,dict):
        string = "d"
        for key in data:
            string += bencode(key)
            string += bencode(data[key])
        string += "e"
        return string
    else:
        raise BencodeError("Not a valid type")

def bdecode(data):
    pass

def bdecode_int(data):
    if data[0] == "i" and data[-1] == "e":
        return int(data[1,len(data)-1])
    else:
        raise BencodeError(data + " is not a valid Integer")

def bdecode_str(data):
    string_list = data.split(":")
    if len(string_list) != 2:
        raise BencodeError("There is no colon!")
    try:
        size = int(string_list[0])
    except ValueError as e:
        raise e
    if len(string_list[1]) != size:
        raise BencodeError("Inconsistent string size: " + data)
    return string_list[1]

def bdecode_list(data):
#    temp_list = []
#    if data[0] == "l" and data[-1] == "e":
#        trimmed_string = data[1,-1]
#        if trimmed_string[0] == "d":
#            temp_list.append(bdecode_dict(trimmed_string)
#        elif trimmed_string[0] == "l":
#            temp_list.append(bdecode_list(trimmed_string)
#        elif trimmed_string[0] == "i":
#            temp_list.append(bdecode_int(data):
#        else:
#            try:
#                string_list = trimmed_string.split
#    else:
#        raise BencodeError(data + "is not a valid List")
#    return temp_list
    pass;

def bdecode_dict(data):
    pass



if __name__ == "__main__":
    assert bencode(123) == "i123e"
    assert bencode("Luke, I am your father") == "22:Luke, I am your father"
    assert bencode(["a","b","c","d"]) == "l1:a1:b1:c1:de"
    assert bencode({"NY":"Albany","PA":"Harrisburg","NJ":["Trenton","New Brunswick"],"IL":{"North":"Chicago","South":"Skokie"}}) == "d2:NY6:Albany2:NJl7:Trenton13:New Brunswicke2:PA10:Harrisburg2:ILd5:North7:Chicago5:South6:Skokieee"
    try:
        bencode(3.1415)
    except BencodeError as e:
        pass
    else:
        assert False == True

    assert bdecode_str("4:spam") == "spam"

    try:
        bdecode_str("5:spam") == "spam"
    except BencodeError as e:
        pass
    else:
        assert False == True

    assert bdecode_str("4spam") == "spam"
