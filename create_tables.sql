CREATE TABLE foods(
  id int not null primary key auto_increment,
  food_name varchar(100) not null,
  quantity_indentifier Enum('kg', 'mg', 'number'),
  calories int not null
);
