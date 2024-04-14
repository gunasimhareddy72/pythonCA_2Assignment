CREATE TABLE IF NOT EXISTS public.customer(
   
    Customer_ID  varchar(20)  NOTNULL
    CONSTRAINT UNIQUE_Customer_ID
    PRIMARY KEY,
    First_name  varchar(50) NOTNULL,
    Last_name    varchar(50)  NOTNULL,
    mail_id      varchar(100) NOTNULL,
    Address      varchar(100) NOTNULL,
    created_date timestamp default CURRENT_TIMESTAMP,
    updated_date timestamp default CURRENT_TIMESTAMP

);

CREATE TABLE public.user_table (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255)
);


