SELECT Fruits.food_name, Meat.food_name, Fruits.calories, Meat.calories
FROM Fruits
LEFT JOIN Meat ON Fruits.id=Meat.id;
