#Name: Abdullah ALmutlaq
#Institution: Misk-Udacity
#Course: Full Stack Nanodegree
#Instructor: Lujain Algholaiqa
#Project: First project
#Date: 17/11/2018


#About:
This program will retrive data from postgres database in order to answer the following questions:
1-What are the most popular three articles of all time?
2-Who are the most popular article authors of all time?
3-On which days did more than 1% of requests lead to errors?

The qestions and answers will be written in Results.txt file once the program ran. 

#Database 
Postgres database structured and filled by Udacity. It has three tables as the following with its details: 

<run \dt>
          List of relations
 Schema |   Name   | Type  |  Owner
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant


<run \d articles>
                                  Table "public.articles"
 Column |           Type           |                       Modifiers
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     |
 body   | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


<run \d authors>
                         Table "public.authors"
 Column |  Type   |                      Modifiers
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    |
 id     | integer | not null default nextval('authors_id_seq'::regclass)
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


<run \d log>
                                  Table "public.log"
 Column |           Type           |                    Modifiers
--------+--------------------------+--------------------------------------------------
 path   | text                     |
 ip     | inet                     |
 method | text                     |
 status | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)

# Difficulties: 
    1-One of the most difficuties I encountered was setting up the vagrant due to             confliction of port 8080 which was opened by another Oracle DB in my Machine. 
    2-Understanding the database relation due to lack of efficient and indexed relation       between Log table and Article table

# Prerequisite
Python3
VB
Vagrant



