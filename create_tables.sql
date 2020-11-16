CREATE TABLE foods(
  id int not null primary key auto_increment,
  category varchar(100) not null,
  food_name varchar(100) not null,
  quantity_indentifier Enum('kg', 'mg', 'number'),
  calories int not null
);
