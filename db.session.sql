select p.*, s.name
from bangazon_api_product p
    join bangazon_api_store s
        on p.store_id = s.id
where p.price > 1000