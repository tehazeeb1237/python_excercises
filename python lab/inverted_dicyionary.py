old_dict={'d':3,'g':4,'t':5}
new_dict=([(value,key) for key,value in old_dict.items()])
print(dict(new_dict))