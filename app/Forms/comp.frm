<div cmptype="Form"  name="MAINFORM" width="60%" height="60%"  caption="Примеры использования контролов" >


Описание полей

SELECT column_name,
       udt_name ,        -- имя типа устройства
       ordinal_position  -- порядковый номер колонки
FROM information_schema.columns
WHERE table_name = 'd_testtab'
ORDER BY ordinal_position;


        -- Удаление таблиц
   DROP TABLE IF EXISTS goods, categories;

   -- Создание таблицы categories
   CREATE TABLE categories (
      category_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
      category_name VARCHAR(100) NOT NULL
   );

   -- Создание таблицы goods
   CREATE TABLE goods (
      product_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
      product_name VARCHAR(100) NOT NULL,
      category INT NOT NULL DEFAULT 1,
      price NUMERIC(18,2) NULL,
    CONSTRAINT fk_category_goods FOREIGN KEY (category) REFERENCES categories (category_id)
);




</div>

