CREATE TABLE Meat(
  id int not null primary key auto_increment,
  food_name varchar(100) not null,
  quantity_indentifier Enum('kg', 'mg', 'number'),
  calories int not null
);

CREATE TABLE Fruits(
  id int not null primary key auto_increment,
  food_name varchar(100) not null,
  quantity_indentifier Enum('kg', 'mg', 'number'),
  calories int not null
);

CREATE TABLE Vegetables(
  id int not null primary key auto_increment,
  food_name varchar(100) not null,
  quantity_indentifier Enum('kg', 'mg', 'number'),
  calories int not null
);

--table s vsi4ki imena i foreign keyove kum tablitzi meat, fruits, vegetables ... etc
