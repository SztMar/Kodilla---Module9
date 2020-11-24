import json

lista =[ {1:2,"text":3}, {"er":2,"text":3}]
print(lista)
def update(x):
    x.remove({1:2,"text":3})
    print(x)


update(lista)
