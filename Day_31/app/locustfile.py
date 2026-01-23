from locust import HttpUser, task, between
import random
import logging

class FastAPIUser(HttpUser):
    wait_time = between(0.1, 1)
    product_ids = set()

    def on_start(self):
        self.client.get("/")

    @task(1)
    def get_products(self):
        try:
            if self.product_ids:
                product_id = random.choice(list(self.product_ids))
            else:
                product_id = random.randint(1, 10)

            self.client.get(f"/products/{product_id}")

        except Exception as e:
            logging.error(f"Error fetching product {product_id}: {e}")

    @task(2)
    def create_product(self):
        try:
            payload = {
                "name": f"Product {random.randint(1, 10000)}",
                "price": round(random.uniform(10.0, 100.0), 2)
            }
            response = self.client.post("/products", json=payload)
            if response.status_code == 200:
                product = response.json()
                self.product_ids.add(product["id"])
        except Exception as e:
            logging.error(f"Error creating product: {e}")

    @task(3)
    def list_products(self):
        try:
            self.client.get("/products")
        except Exception as e:
            logging.error(f"Error listing products: {e}")