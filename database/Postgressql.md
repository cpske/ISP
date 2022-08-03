---
title: PostgreSQL
---

> The official name is PostreSQL, but here I simply call it Postgres,
> which is the original name of the database system.

You can install and run Postgres locally, or run it on a cloud service.

### How to Install Postgres Locally

See [Setting up a local PostgreSQL database](https://www.prisma.io/dataguide/postgresql/setting-up-a-local-postgresql-database) in
[Prisma's Data Guide](https://www.prisma.io/dataguide/).
Prisma also has a short
[Introduction to databases](https://www.prisma.io/dataguide/) and
[Intro to PostgreSQL](https://www.prisma.io/dataguide/postgresql).

### Connecting to Postgres

On Linux, if you connect locally then Postgres uses Linux logins to
identify users (roles).  The default Postgres admin user is `postgres`.

Connect using:
```bash
sudo -u postgres psql
```

To connect (locally or remotely) using a socket:
```bash
psql -h hostname -p port -U username -d database_name
```
the default port is 5432. You must configure postgres to accept connections via sockets, and the allowed hosts.

Or connect using a URL "connection string":
```bash
psql postgresql://username:password@hostname:5432/database_name
```

### Create a Postgres Database

Using SQL
```sql
CREATE DATABASE db_name;
```
or
```sql
CREATE DATABASE db_name 
       ENCODING 'UTF8'
       LC_COLLATE 'en_US.UTF-8'    -- optional
       LC_CTYPE 'en_US.UTF-8';     -- optional
```
List databases:
```sql
SELECT datname FROM pq_database;
-- or --
\list
```

Select a database in `psql`:
```
psql> \c mydatabase
```

## Create Table in a Database

```
CREATE TABLE tablename {
    id INT PRIMARY KEY,
    description VARCHAR(256),
    price FLOAT
    );
``` 

### Delete a Table or Database

```sql
DROP TABLE [IF EXISTS] tablename [CASCADE];
DROP DATABASE [IF EXISTS] db_name;
```

### Add Access Privilege to a Database

```sql
GRANT [ALL | ...] ON DATABASE db_name TO role;
```

Create a role:
```sql
CREATE ROLE name WITH option ... [[ENCRYPTED] PASSWORD 'password'];
```
options: SUPERUSER, CREATEDB, CREATEROLE, INHERIT, LOGIN, REPLICATION, SYSID uid, ...
```




### psql Commands

| Command           | Meaning                         |
|-------------------|---------------------------------|
| `\?`              | Show list of psql commands      |
| `\list`           | List databases                  |
| `\d`              | List tables, views, sequences   |
| `\du`             | List roles                      |
| `\dT`             | List datatypes                  |

