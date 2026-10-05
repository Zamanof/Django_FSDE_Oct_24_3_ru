from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='notes',)

    tags = models.ManyToManyField(
        Tag,
        related_name='notes',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes',
    )

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# ============================================================
# DJANGO MODEL FIELDS + SQL ANALOGS
# ============================================================


# ============================================================
# STRING / TEXT
# ============================================================

# Django:
# models.CharField(max_length=100)
#
# SQL:
# VARCHAR(100)
#
# Используется для короткого текста.
# max_length обязателен.
#
# Example:
# name = models.CharField(max_length=100)


# Django:
# models.TextField()
#
# SQL:
# TEXT
#
# Используется для большого текста.
#
# Example:
# description = models.TextField()


# Django:
# models.EmailField()
#
# SQL:
# VARCHAR(254)
#
# Отдельного EMAIL типа в SQL обычно нет.
# Django дополнительно проверяет формат email.
#
# Example:
# email = models.EmailField()


# Django:
# models.URLField()
#
# SQL:
# VARCHAR(200)
#
# Django проверяет корректность URL.
#
# Example:
# website = models.URLField()


# Django:
# models.SlugField()
#
# SQL:
# VARCHAR
#
# Обычно используется для URL.
#
# Example:
# slug = models.SlugField(max_length=100)



# ============================================================
# INTEGER NUMBERS
# ============================================================

# Django:
# models.IntegerField()
#
# SQL:
# INT / INTEGER
#
# Example:
# age = models.IntegerField()


# Django:
# models.PositiveIntegerField()
#
# SQL:
# INT
#
# Дополнительно можно использовать:
# CHECK (value >= 0)
#
# Example:
# count = models.PositiveIntegerField()


# Django:
# models.SmallIntegerField()
#
# SQL:
# SMALLINT
#
# Example:
# small_number = models.SmallIntegerField()


# Django:
# models.PositiveSmallIntegerField()
#
# SQL:
# SMALLINT
#
# Дополнительно:
# CHECK (value >= 0)
#
# Example:
# count = models.PositiveSmallIntegerField()


# Django:
# models.BigIntegerField()
#
# SQL:
# BIGINT
#
# Example:
# big_number = models.BigIntegerField()



# ============================================================
# DECIMAL / FLOAT NUMBERS
# ============================================================

# Django:
# models.FloatField()
#
# SQL:
# FLOAT
#
# Используется для приблизительных дробных значений.
#
# Example:
# rating = models.FloatField()


# Django:
# models.DecimalField(
#     max_digits=10,
#     decimal_places=2
# )
#
# SQL:
# DECIMAL(10, 2)
# NUMERIC(10, 2)
#
# max_digits:
# общее количество цифр
#
# decimal_places:
# количество цифр после точки
#
# Хорошо подходит для денег.
#
# Example:
# price = models.DecimalField(
#     max_digits=10,
#     decimal_places=2
# )



# ============================================================
# BOOLEAN
# ============================================================

# Django:
# models.BooleanField()
#
# SQL:
#
# PostgreSQL:
# BOOLEAN
#
# SQL Server:
# BIT
#
# MySQL:
# BOOLEAN / TINYINT(1)
#
# Example:
# is_active = models.BooleanField(default=True)



# ============================================================
# DATE / TIME
# ============================================================

# Django:
# models.DateField()
#
# SQL:
# DATE
#
# Example:
# birth_date = models.DateField()


# Django:
# models.DateTimeField()
#
# SQL:
#
# PostgreSQL:
# TIMESTAMP
#
# SQL Server:
# DATETIME2
#
# MySQL:
# DATETIME
#
# Example:
# created_at = models.DateTimeField()


# Django:
# models.DateTimeField(auto_now_add=True)
#
# SQL:
# DATETIME / TIMESTAMP
#
# Django автоматически устанавливает
# дату и время при создании объекта.
#
# Example:
# created_at = models.DateTimeField(auto_now_add=True)


# Django:
# models.DateTimeField(auto_now=True)
#
# SQL:
# DATETIME / TIMESTAMP
#
# Django автоматически обновляет
# дату и время при каждом save().
#
# Example:
# updated_at = models.DateTimeField(auto_now=True)


# Django:
# models.TimeField()
#
# SQL:
# TIME
#
# Example:
# start_time = models.TimeField()


# Django:
# models.DurationField()
#
# SQL:
#
# PostgreSQL:
# INTERVAL
#
# В других СУБД реализация может отличаться.
#
# Example:
# duration = models.DurationField()



# ============================================================
# FILES / IMAGES
# ============================================================

# Django:
# models.FileField(upload_to="documents/")
#
# SQL:
# обычно VARCHAR
#
# Важно:
# сам файл обычно НЕ хранится в базе данных.
#
# В базе хранится путь к файлу.
#
# Example:
# document = models.FileField(
#     upload_to="documents/"
# )


# Django:
# models.ImageField(upload_to="images/")
#
# SQL:
# обычно VARCHAR
#
# В базе хранится путь к изображению.
#
# Для ImageField нужен Pillow:
#
# pip install Pillow
#
# Example:
# image = models.ImageField(
#     upload_to="images/"
# )



# ============================================================
# PRIMARY KEY / AUTO INCREMENT
# ============================================================

# Django:
# models.AutoField(primary_key=True)
#
# SQL:
#
# PostgreSQL:
# SERIAL
#
# SQL Server:
# INT IDENTITY(1,1)
#
# MySQL:
# INT AUTO_INCREMENT
#
# Example:
# id = models.AutoField(primary_key=True)


# Django:
# models.BigAutoField(primary_key=True)
#
# SQL:
#
# PostgreSQL:
# BIGSERIAL
#
# SQL Server:
# BIGINT IDENTITY(1,1)
#
# MySQL:
# BIGINT AUTO_INCREMENT
#
# Django обычно автоматически создаёт:
#
# id = models.BigAutoField(primary_key=True)



# ============================================================
# UUID
# ============================================================

# Django:
# models.UUIDField()
#
# SQL:
#
# PostgreSQL:
# UUID
#
# SQL Server:
# UNIQUEIDENTIFIER
#
# MySQL:
# CHAR(36)
# или
# BINARY(16)
#
# Example:
# uuid = models.UUIDField()



# ============================================================
# IP ADDRESS
# ============================================================

# Django:
# models.GenericIPAddressField()
#
# SQL:
# VARCHAR
#
# PostgreSQL также поддерживает:
# INET
#
# Example:
# ip_address = models.GenericIPAddressField()



# ============================================================
# JSON
# ============================================================

# Django:
# models.JSONField()
#
# SQL:
#
# PostgreSQL:
# JSONB
#
# MySQL:
# JSON
#
# SQL Server:
# обычно NVARCHAR(MAX)
#
# Example:
# settings = models.JSONField()



# ============================================================
# BINARY
# ============================================================

# Django:
# models.BinaryField()
#
# SQL:
#
# PostgreSQL:
# BYTEA
#
# MySQL:
# BLOB
#
# SQL Server:
# VARBINARY(MAX)
#
# Example:
# binary_data = models.BinaryField()



# ============================================================
# RELATIONSHIPS
# ============================================================


# ------------------------------------------------------------
# FOREIGN KEY
# ------------------------------------------------------------

# Django:
#
# author = models.ForeignKey(
#     Author,
#     on_delete=models.CASCADE
# )
#
# Relationship:
# Many-to-One
#
# Один Author может иметь много Book.
#
#
# SQL:
#
# author_id INT
#
# FOREIGN KEY (author_id)
# REFERENCES Author(id)
# ON DELETE CASCADE



# ------------------------------------------------------------
# ONE TO ONE
# ------------------------------------------------------------

# Django:
#
# profile = models.OneToOneField(
#     User,
#     on_delete=models.CASCADE
# )
#
#
# SQL:
#
# user_id INT UNIQUE
#
# FOREIGN KEY (user_id)
# REFERENCES User(id)
# ON DELETE CASCADE
#
#
# OneToOne в SQL обычно:
#
# FOREIGN KEY + UNIQUE



# ------------------------------------------------------------
# MANY TO MANY
# ------------------------------------------------------------

# Django:
#
# tags = models.ManyToManyField(Tag)
#
#
# SQL:
#
# Создаётся отдельная связующая таблица.
#
#
# Например:
#
# ArticleTag
#
# article_id
# tag_id
#
#
# SQL:
#
# CREATE TABLE ArticleTag
# (
#     article_id INT,
#     tag_id INT,
#
#     FOREIGN KEY (article_id)
#         REFERENCES Article(id),
#
#     FOREIGN KEY (tag_id)
#         REFERENCES Tag(id),
#
#     UNIQUE(article_id, tag_id)
# );



# ============================================================
# DJANGO FIELD OPTIONS + SQL ANALOGS
# ============================================================


# Django:
# primary_key=True
#
# SQL:
# PRIMARY KEY
#
# Example:
# id = models.IntegerField(primary_key=True)



# Django:
# unique=True
#
# SQL:
# UNIQUE
#
# Example:
# email = models.EmailField(unique=True)



# Django:
# null=True
#
# SQL:
# NULL
#
# Разрешает NULL в базе данных.
#
# Example:
# phone = models.CharField(
#     max_length=20,
#     null=True
# )



# Django:
# null=False
#
# SQL:
# NOT NULL
#
# Это поведение по умолчанию в Django.



# Django:
# blank=True
#
# SQL:
# прямого аналога нет
#
# blank относится к Django Form / Admin.
#
# Разрешает оставить поле пустым
# при валидации формы.
#
# Example:
# description = models.TextField(
#     blank=True
# )



# Django:
# default=value
#
# SQL:
# DEFAULT
#
# Example:
#
# status = models.CharField(
#     max_length=20,
#     default="active"
# )
#
# SQL:
#
# status VARCHAR(20)
# DEFAULT 'active'



# Django:
# db_index=True
#
# SQL:
# CREATE INDEX
#
# Example:
#
# username = models.CharField(
#     max_length=100,
#     db_index=True
# )



# Django:
# editable=False
#
# SQL:
# прямого аналога нет
#
# Поле нельзя редактировать
# через стандартный ModelForm/Admin.



# Django:
# max_length=100
#
# SQL:
# VARCHAR(100)



# Django:
# choices=
#
# SQL:
# прямого полного аналога нет
#
# Можно использовать CHECK.
#
# Django:
#
# STATUS_CHOICES = [
#     ("draft", "Draft"),
#     ("published", "Published"),
# ]
#
# status = models.CharField(
#     max_length=20,
#     choices=STATUS_CHOICES
# )
#
#
# SQL:
#
# status VARCHAR(20)
#
# CHECK (
#     status IN ('draft', 'published')
# )



# ============================================================
# ON DELETE OPTIONS
# ============================================================

# Django:
# on_delete=models.CASCADE
#
# SQL:
# ON DELETE CASCADE
#
# При удалении родителя
# связанные записи тоже удаляются.



# Django:
# on_delete=models.PROTECT
#
# SQL:
# примерно RESTRICT / NO ACTION
#
# Нельзя удалить объект,
# если на него есть ссылки.



# Django:
# on_delete=models.SET_NULL
#
# SQL:
# ON DELETE SET NULL
#
# Поле ForeignKey должно иметь:
#
# null=True



# Django:
# on_delete=models.SET_DEFAULT
#
# SQL:
# ON DELETE SET DEFAULT
#
# Требуется default.



# Django:
# on_delete=models.DO_NOTHING
#
# SQL:
# Django ничего автоматически не делает.
#
# Поведение зависит от ограничений базы данных.



# ============================================================
# SHORT CHEAT SHEET
# ============================================================

# Django                      SQL
# ------------------------------------------------------------

# CharField                   VARCHAR
# TextField                   TEXT

# EmailField                  VARCHAR
# URLField                    VARCHAR
# SlugField                   VARCHAR

# IntegerField                INT
# PositiveIntegerField        INT + CHECK >= 0

# SmallIntegerField           SMALLINT
# BigIntegerField             BIGINT

# FloatField                  FLOAT
# DecimalField                DECIMAL

# BooleanField                BOOLEAN / BIT

# DateField                   DATE
# DateTimeField               DATETIME / TIMESTAMP / DATETIME2
# TimeField                   TIME

# AutoField                   INT IDENTITY / SERIAL
# BigAutoField                BIGINT IDENTITY / BIGSERIAL

# UUIDField                   UUID / UNIQUEIDENTIFIER

# JSONField                   JSON / JSONB / NVARCHAR(MAX)

# BinaryField                 BLOB / BYTEA / VARBINARY(MAX)

# FileField                   VARCHAR
# ImageField                  VARCHAR

# GenericIPAddressField       VARCHAR / INET

# ForeignKey                  FOREIGN KEY

# OneToOneField               FOREIGN KEY + UNIQUE

# ManyToManyField             separate relation table



# ============================================================
# DJANGO OPTIONS -> SQL
# ============================================================

# primary_key=True            PRIMARY KEY

# unique=True                 UNIQUE

# null=True                   NULL

# default=value               DEFAULT value

# db_index=True               INDEX

# max_length=100              VARCHAR(100)

# choices                     CHECK / application validation

# blank=True                  Django validation only

# editable=False              Django only



# ============================================================
# EXAMPLE DJANGO MODEL
# ============================================================

# from django.db import models
#
#
# class Product(models.Model):
#
#     name = models.CharField(
#         max_length=100
#     )
#
#     description = models.TextField(
#         blank=True
#     )
#
#     price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2
#     )
#
#     count = models.PositiveIntegerField(
#         default=0
#     )
#
#     is_active = models.BooleanField(
#         default=True
#     )
#
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )
#
#     updated_at = models.DateTimeField(
#         auto_now=True
#     )
#
#     def __str__(self):
#         return self.name



# ============================================================
# APPROXIMATE SQL VERSION
# ============================================================

# CREATE TABLE Product
# (
#     id BIGINT PRIMARY KEY,
#
#     name VARCHAR(100) NOT NULL,
#
#     description TEXT NULL,
#
#     price DECIMAL(10, 2) NOT NULL,
#
#     count INT NOT NULL DEFAULT 0
#         CHECK (count >= 0),
#
#     is_active BOOLEAN NOT NULL DEFAULT TRUE,
#
#     created_at TIMESTAMP NOT NULL,
#
#     updated_at TIMESTAMP NOT NULL
# );

