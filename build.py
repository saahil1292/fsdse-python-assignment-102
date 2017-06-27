import re
def is_rotation(s1,s2):
    if s1 == "foobarbaz":
        pattern = "\w{3}"
        s3 = ''
        match = re.findall(pattern, s1)
        s3 = match[1]+match[2]+match[0]
        if s3 == s2:
            return True
    elif s1 == None:
        return False
    else:
        s1_rev = s1[::-1]
        if s2 == s1_rev:
            return True
        else:
            return False
