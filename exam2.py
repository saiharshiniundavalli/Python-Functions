# from functools import reduce
# sales = [
#     {"item": "Pen", "price": 10, "qty": 5},
#     {"item": "Bag", "price": 500, "qty": 0},
#     {"item": "Book", "price": 120, "qty": 3},
#     {"item": "Eraser", "price": 5, "qty": 10},
# ]
# grandtotal=reduce(lambda total,amount:total+amount,
#     map(lambda x:x["price"]*x["qty"],
#         filter(lambda x:x["qty"]>0,sales)),
# )
# print(grandtotal)

students = [
 {"name": "Ravi", "score": 45},
 {"name": "Sneha", "score": 78},
 {"name": "Kiran", "score": 60},
 {"name": "Divya", "score": 92}
]
results=sorted(
    map(lambda x:{**x,"grade":"Pass"},
        filter(lambda x:x["score"]>=60,students)
    ),
    key=lambda s:s["score"],
    reverse=True
)
print(results)