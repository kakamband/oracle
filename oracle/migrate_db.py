import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

connection = psycopg2.connect(DATABASE_URL, sslmode='require')
connection.autocommit = True

# def create_staging_table(cursor) -> None:
#     cursor.execute("""
#         DROP TABLE IF EXISTS posts;
#         CREATE UNLOGGED TABLE posts (
#             id                  TEXT,
#             title               TEXT,
#             title_mentions      TEXT[],
#             text_mentions       TEXT[],
#             sentiment           DECIMAL,
#             upvotes             INTEGER,
#             comments            INTEGER
#         );
#     """)
#
# def create_staging_table2(cursor) -> None:
#     cursor.execute("""
#         DROP TABLE IF EXISTS comments;
#         CREATE UNLOGGED TABLE comments (
#             id                  TEXT,
#             text                TEXT,
#             sentiment           DECIMAL,
#             upvotes             INTEGER,
#             comments            INTEGER,
#             text_mentions       TEXT[]
#         );
#     """)

# def create_staging_table(cursor) -> None:
#     cursor.execute("""
#         DROP TABLE IF EXISTS posts;
#         CREATE TABLE posts (
#             datetime            TIMESTAMP WITH TIME ZONE,
#             id                  TEXT,
#             title               TEXT,
#             title_mentions      TEXT[],
#             text_mentions       TEXT[],
#             sentiment           DECIMAL,
#             upvotes             INTEGER,
#             comments            INTEGER
#         );
#     """)
#
# def create_staging_table2(cursor) -> None:
#     cursor.execute("""
#         DROP TABLE IF EXISTS comments;
#         CREATE TABLE comments (
#             datetime            TIMESTAMP WITH TIME ZONE,
#             id                  TEXT,
#             text                TEXT,
#             text_mentions       TEXT[],
#             sentiment           DECIMAL,
#             upvotes             INTEGER,
#             comments            INTEGER
#         );
#     """)
#
# def create_staging_table(cursor) -> None:
#     cursor.execute("""
#         DROP TABLE IF EXISTS posts;
#         CREATE TABLE posts (
#             posted              TIMESTAMP WITH TIME ZONE,
#             last_updated        TIMESTAMP WITH TIME ZONE,
#             id                  TEXT,
#             title               TEXT,
#             title_mentions      TEXT[],
#             text_mentions       TEXT[],
#             sentiment           DECIMAL,
#             upvotes             INTEGER,
#             comments            INTEGER
#         );
#     """)
#
# def create_staging_table2(cursor) -> None:
#     cursor.execute("""
#         DROP TABLE IF EXISTS comments;
#         CREATE TABLE comments (
#             posted              TIMESTAMP WITH TIME ZONE,
#             last_updated        TIMESTAMP WITH TIME ZONE,
#             id                  TEXT,
#             text                TEXT,
#             text_mentions       TEXT[],
#             sentiment           DECIMAL,
#             upvotes             INTEGER,
#             comments            INTEGER
#         );
#     """)

# def create_staging_table3(cursor) -> None:
#     cursor.execute("""
#         DROP TABLE IF EXISTS tickers;
#         CREATE TABLE tickers (
#             date                    TIMESTAMP WITH TIME ZONE,
#             ticker                  TEXT,
#             comment_sentiment       DECIMAL,
#             post_title_sentiment    DECIMAL,
#             post_text_sentiment     DECIMAL,
#             comment_upvotes         INTEGER,
#             post_title_upvotes      INTEGER,
#             post_text_upvotes       INTEGER,
#             comment_replies         INTEGER,
#             post_title_replies      INTEGER,
#             post_text_replies       INTEGER
#         );
#         CREATE UNIQUE INDEX CONCURRENTLY ticker_date_index ON tickers (date, ticker);
#     """)

def create_staging_table3(cursor) -> None:
    cursor.execute("""
        ALTER TABLE tickers
        ADD COLUMN comment_mentions INTEGER,
        ADD COLUMN post_title_mentions INTEGER,
        ADD COLUMN post_text_mentions INTEGER;
    """)

with connection.cursor() as cursor:
    create_staging_table3(cursor)
