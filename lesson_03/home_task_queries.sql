/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
SELECT c.name AS film_name,
       COUNT(f.film_id) AS film_count
FROM film f
LEFT JOIN film_category fc ON f.film_id = fc.film_id
LEFT JOIN category c ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY film_count DESC;



/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
SELECT a.first_name || ' ' || a.last_name AS actor_full_name,
       COUNT(r.rental_id) AS rental_count
FROM actor a
LEFT JOIN film_actor fa on a.actor_id = fa.actor_id
LEFT JOIN inventory i on fa.film_id = i.film_id
LEFT JOIN rental r on i.inventory_id = r.inventory_id
GROUP BY actor_full_name
ORDER BY rental_count DESC
LIMIT 10;



/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
SELECT c.name category_name
FROM payment p
LEFT JOIN rental r on p.rental_id = r.rental_id
LEFT JOIN inventory i on r.inventory_id = i.inventory_id
LEFT JOIN film_category fc on i.film_id = fc.film_id
LEFT JOIN category c on fc.category_id = c.category_id
GROUP BY category_name
ORDER BY SUM(p.amount) DESC
LIMIT 1;



/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
SELECT f.title
FROM inventory
RIGHT JOIN film f on inventory.film_id = f.film_id
WHERE inventory.film_id IS NULL;



/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
SELECT a.first_name || ' ' || a.last_name AS actor_full_name
FROM film_category
LEFT JOIN category c on c.category_id = film_category.category_id
LEFT JOIN film_actor fa on film_category.film_id = fa.film_id
LEFT JOIN actor a on fa.actor_id = a.actor_id
WHERE c.name = 'Children'
GROUP BY actor_full_name
ORDER BY COUNT(*) DESC
LIMIT 3;
