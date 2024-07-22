import pandas as pd

#l1 = ["apple", "cvb"]
#nl = []
'''
for x in l1:
    if "a" in x:
        nl.append(x)
print(nl)

nl = [x for x in l1 if "a" in x]
print(nl)
'''

df = pd.read_excel(r"C:\Users\adity\PycharmProjects\pythonProject\testing.xlsx")
data = df.to_json(indent=4)
print(data)

