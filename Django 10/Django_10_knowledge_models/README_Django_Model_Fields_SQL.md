# Django Model Fields & SQL Analogs

Краткая шпаргалка по основным полям Django Models и их ближайшим аналогам в SQL.

---

## String / Text Fields

| Django Field | SQL Analog | Description |
|---|---|---|
| `CharField(max_length=100)` | `VARCHAR(100)` | Короткий текст |
| `TextField()` | `TEXT` | Большой текст |
| `EmailField()` | `VARCHAR(254)` | Email с Django-валидацией |
| `URLField()` | `VARCHAR(200)` | URL |
| `SlugField()` | `VARCHAR` | Slug для URL |

### Example

```python
name = models.CharField(max_length=100)
description = models.TextField()
email = models.EmailField()
website = models.URLField()
slug = models.SlugField(max_length=100)
```

---

## Integer Fields

| Django Field | SQL Analog |
|---|---|
| `IntegerField()` | `INT` |
| `PositiveIntegerField()` | `INT + CHECK >= 0` |
| `SmallIntegerField()` | `SMALLINT` |
| `PositiveSmallIntegerField()` | `SMALLINT + CHECK >= 0` |
| `BigIntegerField()` | `BIGINT` |

---

## Float & Decimal

| Django Field | SQL Analog | Usage |
|---|---|---|
| `FloatField()` | `FLOAT` | Приблизительные дробные числа |
| `DecimalField()` | `DECIMAL / NUMERIC` | Точные значения, деньги |

```python
rating = models.FloatField()

price = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
```

```sql
price DECIMAL(10, 2)
```

`max_digits` — общее количество цифр.  
`decimal_places` — количество цифр после точки.

---

## Boolean

```python
is_active = models.BooleanField(default=True)
```

```text
PostgreSQL  -> BOOLEAN
SQL Server  -> BIT
MySQL       -> BOOLEAN / TINYINT(1)
```

---

## Date & Time

| Django Field | SQL Analog |
|---|---|
| `DateField()` | `DATE` |
| `DateTimeField()` | `TIMESTAMP / DATETIME / DATETIME2` |
| `TimeField()` | `TIME` |
| `DurationField()` | `INTERVAL` / DB-specific |

```python
birth_date = models.DateField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
start_time = models.TimeField()
```

---

## File & Image Fields

```python
document = models.FileField(upload_to="documents/")
image = models.ImageField(upload_to="images/")
```

SQL analog:

```text
VARCHAR
```

Django обычно хранит в базе путь к файлу, а не сам файл.

Для `ImageField`:

```bash
pip install Pillow
```

---

## Primary Key & Auto Increment

### AutoField

```python
id = models.AutoField(primary_key=True)
```

```text
PostgreSQL  -> SERIAL
SQL Server  -> INT IDENTITY(1,1)
MySQL       -> INT AUTO_INCREMENT
```

### BigAutoField

```python
id = models.BigAutoField(primary_key=True)
```

```text
PostgreSQL  -> BIGSERIAL
SQL Server  -> BIGINT IDENTITY(1,1)
MySQL       -> BIGINT AUTO_INCREMENT
```

---

## UUID

```python
uuid = models.UUIDField()
```

```text
PostgreSQL  -> UUID
SQL Server  -> UNIQUEIDENTIFIER
MySQL       -> CHAR(36) / BINARY(16)
```

---

## IP Address

```python
ip_address = models.GenericIPAddressField()
```

SQL:

```text
VARCHAR
```

PostgreSQL также поддерживает `INET`.

---

## JSON

```python
settings = models.JSONField()
```

```text
PostgreSQL  -> JSONB
MySQL       -> JSON
SQL Server  -> NVARCHAR(MAX)
```

---

## Binary Data

```python
binary_data = models.BinaryField()
```

```text
PostgreSQL  -> BYTEA
MySQL       -> BLOB
SQL Server  -> VARBINARY(MAX)
```

---

# Relationships

## ForeignKey

```python
author = models.ForeignKey(
    Author,
    on_delete=models.CASCADE
)
```

Relationship:

```text
Many-to-One
```

SQL:

```sql
author_id INT,

FOREIGN KEY (author_id)
REFERENCES Author(id)
ON DELETE CASCADE
```

---

## OneToOneField

```python
user = models.OneToOneField(
    User,
    on_delete=models.CASCADE
)
```

SQL:

```sql
user_id INT UNIQUE,

FOREIGN KEY (user_id)
REFERENCES User(id)
```

`OneToOneField = FOREIGN KEY + UNIQUE`

---

## ManyToManyField

```python
tags = models.ManyToManyField(Tag)
```

SQL создаёт отдельную связующую таблицу:

```sql
CREATE TABLE ArticleTag
(
    article_id INT,
    tag_id INT,

    FOREIGN KEY (article_id)
        REFERENCES Article(id),

    FOREIGN KEY (tag_id)
        REFERENCES Tag(id),

    UNIQUE(article_id, tag_id)
);
```

---

# Django Field Options

| Django Option | SQL |
|---|---|
| `primary_key=True` | `PRIMARY KEY` |
| `unique=True` | `UNIQUE` |
| `null=True` | `NULL` |
| `default=value` | `DEFAULT` |
| `db_index=True` | `INDEX` |
| `max_length=100` | `VARCHAR(100)` |
| `choices` | `CHECK` / application validation |
| `blank=True` | Django only |
| `editable=False` | Django only |

---

## on_delete Options

| Django | SQL / Meaning |
|---|---|
| `models.CASCADE` | `ON DELETE CASCADE` |
| `models.PROTECT` | примерно `RESTRICT / NO ACTION` |
| `models.SET_NULL` | `ON DELETE SET NULL` |
| `models.SET_DEFAULT` | `ON DELETE SET DEFAULT` |
| `models.DO_NOTHING` | Django ничего автоматически не делает |

---

# Quick Cheat Sheet

| Django | SQL |
|---|---|
| `CharField` | `VARCHAR` |
| `TextField` | `TEXT` |
| `EmailField` | `VARCHAR` |
| `URLField` | `VARCHAR` |
| `SlugField` | `VARCHAR` |
| `IntegerField` | `INT` |
| `PositiveIntegerField` | `INT + CHECK` |
| `SmallIntegerField` | `SMALLINT` |
| `BigIntegerField` | `BIGINT` |
| `FloatField` | `FLOAT` |
| `DecimalField` | `DECIMAL` |
| `BooleanField` | `BOOLEAN / BIT` |
| `DateField` | `DATE` |
| `DateTimeField` | `TIMESTAMP / DATETIME2` |
| `TimeField` | `TIME` |
| `AutoField` | `SERIAL / IDENTITY` |
| `BigAutoField` | `BIGSERIAL / BIGINT IDENTITY` |
| `UUIDField` | `UUID / UNIQUEIDENTIFIER` |
| `JSONField` | `JSON / JSONB` |
| `BinaryField` | `BLOB / BYTEA / VARBINARY` |
| `FileField` | `VARCHAR` |
| `ImageField` | `VARCHAR` |
| `ForeignKey` | `FOREIGN KEY` |
| `OneToOneField` | `FOREIGN KEY + UNIQUE` |
| `ManyToManyField` | Separate relation table |

---

# Full Django Example

```python
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    count = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
```

---

# Approximate SQL Version

```sql
CREATE TABLE Product
(
    id BIGINT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    description TEXT NULL,

    price DECIMAL(10, 2) NOT NULL,

    count INT NOT NULL DEFAULT 0
        CHECK (count >= 0),

    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL,

    updated_at TIMESTAMP NOT NULL
);
```

---

# Important

Django Fields не всегда имеют точный 1:1 аналог в SQL.

Реальный тип данных зависит от используемой СУБД:

- PostgreSQL
- Microsoft SQL Server
- MySQL
- SQLite
- Oracle

Django ORM абстрагирует эти различия и позволяет работать с моделями через Python-код.
