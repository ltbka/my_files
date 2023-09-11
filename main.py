# CRUD

# Create
# Read
# Update
# Delete

# import datetime

# #база данных 
# data = [{'id': 1,'name':'iphone 8','price':8000,'created_at': datetime.datetime(2022, 9, 4),'is_active':True},
#         {'id': 2,'name':'redmi6','price':5000,'creadet_at': datetime.datetime(2023, 10, 5),'is_active':True},
#         {'id': 3,'name':'lenovo','price':4500,'creadet_at': datetime.datetime(2021, 9, 3),'is_active':False}]

# def get_all():
#     return data

# def get_one(id):
#     product = [i for i in data if i['id'] == id]
#     if product:
#         return product
#     return 'нет такого продукта'
    
# def post_product():
#     max_id =[i[id]for i in data]
#     new_data = {'id':max_id + 1,
#                 'name':input('Имя: '),
#                 'price':int(input('Цена: ')),
#                 'created_at':datetime.datetime.now(),
#                 'is_active':True}
#     data.append(new_data)
#     return '201 CREATED', new_data
   
# def patch_product(id):
#     product = [i for i in data if['id']== id]
#     if product:
#         data.remove(product[0])
#         name = input('Имя: ')
#         price = input('Цена: ')
#         product[0]['name'] = name
#         product[0]['price'] = price
#         product[0]['created_at'] = datetime.datetime.now()
#         product[0]['is_active'] = True
#         data.insert(index, product[0])
#         return 'Успешно изменен'
#     else:
#         return '404', 'Вы ввели неправильные данные'
    
#  def delete_product(id):
#      product = [i for i in data if i ['id']== id]
#      if product:
#          data.remove(product[0])
#          return 'Удален'
#     else:
#         return 'НЕТ ТАКОГО ПРОДУКТА'
    

# def main():
#     print('Привет,тебе достпуны следующие функции:\n\tPOST\n\tGEtT\n\tDETAIL\n\tPUT\n\tDELETE')
#     method = input('Введите одну из функций: ')
    
#     if method == 'GET':
#         print(get_all())
    
#     elif method == 'DELAIL':
#         id = int(input('Введите id: '))
#         print(get_one(id))
#     elif 
