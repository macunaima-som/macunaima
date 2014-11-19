
import string

def text_to_dict(input_text):
    output_dict = dict()
    
    lines = string.split(input_text, '\n')
    for l in lines:
        
        p = string.split(l, ':')
        if len(p) > 1:
            key = p[0]
            value = p[1]
            i = 2
            while i < len(p):
                value = value + ":" + p[i]
                i = i + 1

            key = string.strip(key)
            value = string.strip(value)
            output_dict[key] = value

    return output_dict

def dict_to_text(input_dict):
    output_text = ""

    for k in input_dict.keys():
        output_text = string.join([output_text, k,  u": ", unicode(input_dict[k]), u"\n"], "")

    return output_text

if __name__ == "__main__":
    text = "Data: this much data!\n \
    Test: This much text!\n \
    My title: title: subtitle! \
    "
    print text_to_dict(text)
    print dict_to_text(text_to_dict(text))
