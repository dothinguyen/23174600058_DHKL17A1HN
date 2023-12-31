#11.1
a=[1,2,3]
b=[1,[2,3]]
c=[]
d=[1,2,3][1:]
print(len(a),len(b),len(c),len(d))
#11.2
teams = [['Steven','Neena','Lex','Alexander','Bruce'],['David','Jack','Bill','Tom','Mike','Daniel'],['Alexander','Adam','Payam','Kevin','Sigal','Mike']]
doi_te_nhat = teams[1]
doi_truong_doi_te_nhat = doi_te_nhat[1]
print("Đội trưởng của đội tệ nhất là ", doi_truong_doi_te_nhat)
#11.3
n=input("List of animals:").split(' ')
print("Number of animals:", len(n))
a=input("I want to find: ")
if a in n :
    print("There is",a, "in list of animals")
else:
    print("There isn't",a,"in list of animals")
#11.4
