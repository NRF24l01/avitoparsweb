create table public.advises(
   id INT NOT NULL,
   req VARCHAR (50),
   name VARCHAR (35),
   description VARCHAR (750),
   url VARCHAR (50),
   price VARCHAR (20),
   views VARCHAR (10),
   date_public VARCHAR (10),
   seller_name VARCHAR (10),
   PRIMARY KEY (id)
);

create table public.reqs(
   id INT NOT NULL,
   req VARCHAR (50) NOT NULL,
   upd_time VARCHAR (35) NOT NULL,
   mails VARCHAR (50),
   tgs VARCHAR (20),
   key_creator VARCHAR (50),
   PRIMARY KEY (id)
);

create table public.keys(
   id INT NOT NULL,
   key VARCHAR (50) NOT NULL,
   usages VARCHAR (10) NOT NULL,
   PRIMARY KEY (id)
);