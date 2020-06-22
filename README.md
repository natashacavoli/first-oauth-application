# First Oauth Application
My first OAuth2 API Application with Flask

## Installing Packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
pip install bcrypt
pip install Flask
pip install Flask-Migrate
pip install Flask-SQLAlchemy
pip install psycopg2
pip install PyJWT
```
## Create Table
```sql
CREATE TABLE users (
    id integer NOT NULL,
    name character varying(75) NOT NULL,
    email character varying(75) NOT NULL,
    username character varying(75) NOT NULL,
    password character varying(75) NOT NULL,
    bio text
);

ALTER TABLE public.users ALTER id SET DEFAULT nextval('users_id_seq'::regclass);

ALTER TABLE users ADD CONSTRAINT unique_username
  UNIQUE (username);
ALTER TABLE users ADD CONSTRAINT users_pkey
  PRIMARY KEY (id);

CREATE TABLE clients (
    id integer NOT NULL,
    client_id uuid NOT NULL,
    client_secret character varying(120) NOT NULL,
    expires timestamp without time zone NOT NULL
);

ALTER TABLE clients ADD CONSTRAINT clients_pkey
  PRIMARY KEY (id);
ALTER TABLE clients ADD CONSTRAINT clients_id_fkey
  FOREIGN KEY (id) REFERENCES users(id);
```
## Running
Change string of connection with database in main.py
```python
_con = "postgresql://username:password@address:port/database"
```
Change string o secret keys in auth.py
```python
secret = "your secret key"
```
