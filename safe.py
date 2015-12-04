"""Safe_Ploblem"""
def safe():
    """print count of how many step"""
    pas_box = input()
    code = input()
    count = 0
    for i in range(len(pas_box)):
        if (ord(code[i])-ord(pas_box[i]))%26 >\
        (ord(pas_box[i])-ord(code[i]))%26:
            count += (ord(pas_box[i])-ord(code[i]))%26
        else:
            count += (ord(code[i])-ord(pas_box[i]))%26
    print(count)
safe()
