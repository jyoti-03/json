import json
shopping_dic={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
for p in shopping_dic["shopping_list"]:
    print(p)
b_a=input("buy or add- ")
if b_a =="buy":
    user_in=input("enter products u want to buy- ")
    if user_in in shopping_dic["shopping_list"]:
        how_many=int(input("enter how much u want- "))
        if how_many <= int(shopping_dic["shopping_list"][user_in]):
            c=int(shopping_dic["shopping_list"][user_in])-how_many
            shopping_dic["shopping_list"][user_in]=c

        else:
            print("sory we have only",shopping_dic["shopping_list"][user_in],"this much")
    else:
        print(user_in,"not avalable")
elif b_a == "add":
    add_item=input("enter item name- ")
    how_item=int(input("how much u want to add- "))
    shopping_dic[add_item]=how_item
else:
    print("u have to enter only buy/add ^_^")
j=json.dumps(shopping_dic)
print(j)
