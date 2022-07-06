# Product Catalog application

Product Catalog app which offer REST API endpoints for CRUD operations on Product and Rating entities.

**Local test user provided in fixtures.** \
**Username:** test_user \ **Password:** test_password


## Run Locally

Build docker images

```bash
  docker-compose build
```

Apply migrations to DB

```bash
  docker-compose run web python manage.py migrate
```

Load initial dummy data

```bash
  docker-compose run web python manage.py loaddata product_catalog/fixtures/data.json
```

Rebuild ES search indexes

```bash
  docker-compose run web python manage.py search_index --rebuild 
```

Start the server

```bash
  docker-compose up
```

Run test suite

```bash
  docker-compose run web pytest
```

 
## API Reference

#### Products endpoints

```http
  GET /products/
  GET /products/:product_id:/
  POST /products/
  PATCH /products/:product_id:/
  DELETE /products/:product_id:/

```

#### Ratings endpoints

```http
  GET /ratings/
  GET /ratings/:rating_id:/
  POST /ratings/
  PATCH /ratings/:rating_id:/
  DELETE /ratings/:rating_id:/
```

#### Search powered by ElasticSearch

```http
  GET /search/products/name=:search_param:
```

#### API Schema generator

```http
  GET /schema/
```




## 🚀 About Me
I'm a full stack developer proficient in Python/Django and Typescript/React. 


## Running Tests

To run tests, run the following command

```bash
  docker-compose run web pytest
```

