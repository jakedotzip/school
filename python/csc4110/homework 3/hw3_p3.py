string_list = ["John Q Public 541-233-7612", 
                "Jimmy A Timmy 123-456-7896", 
                "Frank B Fruit 135-718-6179", 
                "Alice D Petty 691-168-6819",
                "David J Ummer 946-614-1651"]


def separate(s):
  name = ""
  phone = ""
  # for each element in string list
  for i in s:
    # split the string into multiple parts
    re = [i for i in i.split(' ')]
    # group name parts into a name string
    name = " ".join(re[0:-1])
    # phone is the last part 
    phone = re[-1]
    print("Name: {0} \t Phone number: {1}".format(name, phone))
    
# run the program
separate(string_list)