"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View


from levelupreports.views.helpers import dict_fetch_all

class ExpensiveProductList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            db_cursor.execute("""
            select p.*, s.name as StoreName
                from bangazon_api_product p
                    join bangazon_api_store s
                        on p.store_id = s.id
                where p.price > 1000
            """)
            dataset = dict_fetch_all(db_cursor)


            expensive_products = []

            for row in dataset:
                product = {
                        "name": row['name'], 
                        'store': row['store_id'], 
                        'description': row['description'], 
                        'location': row['location'], 
                        'category': row['category']
                }
                
       
                
                user_dict = next(
                    (
                        expensive_product for expensive_product in expensive_products
                        if expensive_product['store_id'] == row['store_id']
                    ),
                    None
                )
                
                if user_dict:
                    user_dict['products'].append(product)
                else:
                    expensive_products.append({
                        "user_id": row['user_id'],
                        "full_name": row['full_name'],
                        "products": [product]
                    })
        
        template = 'expensive_products.html'
        
        context = {
            "expensive_products_list": expensive_products
        }

        return render(request, template, context)

