import accessBDD

# Mostrar la cantidad de copias que existen en el inventario para la película 'Sugar Wonka'
def c1():
    sqlQuery = "select t.nombre, p.Titulo, a.cantidad \
from Asignacion_tienda_pelicula a \
	join Pelicula p on p.idPelicula = a.idPelicula \
	join Tienda t on t.idTienda = a.idTienda \
where lower(p.Titulo) = lower('Sugar Wonka') \
group by 1, 2, 3;"

    conexionCarga = accessBDD
    data = conexionCarga.sqlSelectCustom(sqlQuery)

    return data

# Mostrar el nombre, apellido y pago total de todos los clientes que han rentado películas por lo menos 40 veces
def c2():
    sqlQuery = "SELECT r.idcliente, c.nombre, c.apellido, count(r.idcliente), cast(SUM(p.costo_renta)as VARCHAR) from renta r \
join cliente c on c.idcliente = r.idcliente \
join pelicula p on p.idpelicula = r.idpelicula \
GROUP by 1, 2, 3 \
HAVING count(r.idcliente) >= 40 ORDER by 4 \
;"
    conexionCarga = accessBDD
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data

# Mostrar el nombre y apellido de los actores que contienen la palabra “SON” en su apellido, ordenados por su primer nombre.
def c3():
    sqlQuery = "select nombre, apellido \
from Actor \
where lower(apellido) like lower('%son%') \
order by nombre"

    conexionCarga = accessBDD
    data = conexionCarga.sqlSelectCustom(sqlQuery)

    return data

# Mostrar el nombre y apellido de los actores que participaron en una película cuya descripción incluye la palabra “crocodile” 
# y “shark” junto con el año de lanzamiento de la película, ordenados por el apellido del actor en forma ascendente.
def c4():
    sqlQuery = "select nombre, apellido, p.Titulo, p.Ano_lanzamiento \
from Actor a \
join Asignacion_actor_pelicula aapp on aapp.idactor = a.idactor \
join Pelicula p on p.idPelicula = aapp.idPelicula \
where lower(p.descripcion) like lower('%Crocodile%') and lower(p.descripcion) like lower('%shark%') \
order by 2 asc"

    conexionCarga = accessBDD
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data

# Mostrar el país y el nombre del cliente que más películas rentó así como también el porcentaje que representa 
# la cantidad de películas que rentó conrespecto al resto de clientes del país.
def c5():
    sqlQuery = "select pais, nombre, apellido, cast(round((count::DECIMAL/total::DECIMAL)::DECIMAL,2)*100 as VARCHAR(10))||'%' porcentaje from ( \
SELECT b.idpais, b.pais, b.nombre, b.apellido, b.idciudad, b.ciudad, b.count,  \
(SELECT max(d.sumarentas) from ( \
	SELECT p.idpais, ci.idciudad, COUNT(idrenta) sumarentas from renta r \
	join cliente cli on cli.idcliente = r.idcliente \
	JOIN ciudad ci on ci.idciudad = cli.idciudad \
	JOIN pais p on p.idpais = ci.idpais \
	GROUP by 1, 2 ORDER by 1) d where b.idpais = d.idpais) maxrent,  \
( SELECT COUNT(idrenta) from renta r  \
	join cliente cli on cli.idcliente = r.idcliente \
	JOIN ciudad ci on ci.idciudad = cli.idciudad \
	JOIN pais p on p.idpais = ci.idpais where p.idpais = b.idpais ORDER by 1) total  \
from ( SELECT p.idpais, p.nombre pais, cli.nombre, cli.apellido, ci.idciudad, ci.nombre ciudad, COUNT(idrenta) from renta r  \
	join cliente cli on cli.idcliente = r.idcliente \
	JOIN ciudad ci on ci.idciudad = cli.idciudad \
	JOIN pais p on p.idpais = ci.idpais \
	GROUP by 1, 2, 3, 4, 5, 6 ORDER by 7 desc limit 1 \
) b GROUP by 1, 2, 3, 4,5, 6,7,8 ) final where maxrent = count"
    conexionCarga = accessBDD
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data

# Mostrar el total de clientes y porcentaje de clientes por ciudad y país. El ciento por ciento es el total de clientes por país. 
# (Tip: Todos los porcentajes por ciudad de un país deben sumar el 100%).
def c6():
    sqlQuery="SELECT p.nombre AS pais, ci.nombre AS ciudad, \
	(SELECT count(idcliente) FROM cliente cli2 \
			JOIN ciudad ci2 ON ci2.idciudad = cli2.idciudad \
		WHERE ci2.idciudad = ci.idciudad) AS clientesxciudad,"

    sqlQuery += " cast(round((round((SELECT count(idcliente) FROM cliente cli2 JOIN ciudad ci2 ON ci2.idciudad = cli2.idciudad \
				WHERE ci2.idciudad = ci.idciudad) * 100::DECIMAL, 2) / round(( \
				SELECT COUNT(cct.idcliente) FROM cliente cct \
					JOIN ciudad ccd ON cct.idciudad = ccd.idciudad \
					JOIN pais pp ON ccd.idpais = pp.idpais \
				WHERE pp.idpais = p.idpais) * 100::DECIMAL, 2))::DECIMAL, 2)*100 as varchar (10))||'%' AS porcentaje, \
    (SELECT COUNT(cct.idcliente) \
    FROM cliente cct \
        JOIN ciudad ccd ON cct.idciudad = ccd.idciudad \
        JOIN pais pp ON ccd.idpais = pp.idpais \
    WHERE pp.idpais = p.idpais) AS totalxpais \
FROM cliente cl \
    JOIN ciudad ci ON ci.idciudad = cl.idciudad \
    JOIN pais p ON p.idpais = ci.idpais \
ORDER BY 1, 2;"
    conexionCarga = accessBDD
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data

# Mostrar el nombre del país, la ciudad y el promedio de rentas por ciudad. Por ejemplo: si el país tiene 3 ciudades, se deben sumar todas las rentas de
# la ciudad y dividirlo dentro de tres (número de ciudades del país).
def c7():
    sqlQuery="SELECT pais, ciudad, rentas, cast(round((rentas::DECIMAL/numpaises::decimal), 2) as varchar(10)) promedio from ( \
	SELECT b.*,  \
	( \
		select count(cc.idciudad) numpaises from ciudad cc \
		where cc.idpais = b.idpais \
	) numpaises \
	from ( \
		SELECT p.idpais, p.nombre pais, ci.idciudad, ci.nombre ciudad, count(idrenta) rentas from renta r \
		join cliente cli on cli.idcliente = r.idcliente \
		join ciudad ci on ci.idciudad = cli.idciudad \
		join pais p on p.idpais = ci.idpais \
		GROUP by 1, 2, 3, 4 \
		order by 1 \
	) b \
) d;"
    conexionCarga = accessBDD   
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data

# Mostrar el nombre del país y el porcentaje de rentas de películas de la
# categoría “Sports”. El porcentaje es sobre el número total de rentas decada país.
def c8():
    sqlQuery = "SELECT pais, cast(round((numsports::DECIMAL/sum::DECIMAL), 3)*100 as varchar(10))||'%' porcentajesport from( \
	SELECT pais, sum(rentas), numsports from ( \
		SELECT b.*, \
			( \
				SELECT count(idrenta) numsports from renta r \
				join cliente cli on cli.idcliente = r.idcliente \
				join ciudad ci on ci.idciudad = cli.idciudad \
				join pais p on p.idpais = ci.idpais \
				join pelicula pe on pe.idpelicula = r.idpelicula \
				join asignacion_categoria_pelicula acp on acp.idpelicula = pe.idpelicula \
				join categoria c on c.idcategoria = acp.idcategoria \
				where lower(c.nombre) = 'sports' and p.idpais = b.idpais \
			) numsports  \
		from ( \
			SELECT p.idpais, p.nombre pais, ci.idciudad, ci.nombre ciudad, count(idrenta) rentas from renta r \
			join cliente cli on cli.idcliente = r.idcliente \
			join ciudad ci on ci.idciudad = cli.idciudad \
			join pais p on p.idpais = ci.idpais \
			GROUP by 1, 2, 3, 4 \
			order by 1 \
		) b ORDER by 1, 2, 3, 4, 6 \
	) f GROUP by 1, 3 \
) g;"
    conexionCarga = accessBDD   
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data

# Mostrar la lista de ciudades de Estados Unidos y el número de rentas de películas para 
# las ciudades que obtuvieron más rentas que la ciudad “Dayton”.
def c9():
    sqlQuery="SELECT ciudad, rentas from ( \
	SELECT p.idpais, p.nombre pais, ci.idciudad, ci.nombre ciudad, count(idrenta) rentas from renta r \
	join cliente cli on cli.idcliente = r.idcliente \
	join ciudad ci on ci.idciudad = cli.idciudad \
	join pais p on p.idpais = ci.idpais \
	where LOWER(p.nombre) = LOWER('United States') \
	GROUP by 1, 2, 3, 4 \
	order by 1 \
) b where rentas > ( \
		SELECT count(idrenta) rentas from renta r \
		join cliente cli on cli.idcliente = r.idcliente \
		join ciudad ci on ci.idciudad = cli.idciudad \
		join pais p on p.idpais = ci.idpais \
		where LOWER(p.nombre) = LOWER('United States') and lower(ci.nombre) = LOWER('Dayton') \
		order by 1 \
	)	"
    conexionCarga = accessBDD   
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data

# Mostrar todas las ciudades por país en las que predomina la renta de películas de la categoría “Horror”. 
# Es decir, hay más rentas que las otras categorías.
def c10():
    sqlQuery="select pais, ciudad from ( \
	SELECT * from ( \
		SELECT p.idpais, p.nombre pais, c.idciudad, c.nombre ciudad, cat.idcategoria, cat.nombre categoria, count(r.idrenta) maxrenta from renta r \
		join cliente cli on r.idcliente = cli.idcliente  \
		join ciudad c on cli.idciudad = c.idciudad \
		join pais p on c.idpais = p.idpais \
		join pelicula pe on pe.idpelicula = r.idpelicula \
		join asignacion_categoria_pelicula acp on pe.idpelicula = acp.idpelicula \
		join categoria cat on cat.idcategoria = acp.idcategoria \
		GROUP by 1, 2, 3, 4, 5, 6 \
		order by 1, 3, 7) m  \
join ( \
SELECT b.idpais, b.idciudad, max(b.maxrenta ) \
from ( \
	SELECT p.idpais, p.nombre pais, c.idciudad, c.nombre ciudad, cat.idcategoria, cat.nombre categoria, count(r.idrenta) maxrenta from renta r \
	join cliente cli on r.idcliente = cli.idcliente \
	join ciudad c on cli.idciudad = c.idciudad \
	join pais p on c.idpais = p.idpais \
	join pelicula pe on pe.idpelicula = r.idpelicula \
	join asignacion_categoria_pelicula acp on pe.idpelicula = acp.idpelicula \
	join categoria cat on cat.idcategoria = acp.idcategoria \
	GROUP by 1, 2, 3, 4, 5, 6) b  \
join categoria cat on b.idcategoria = cat.idcategoria \
join ciudad c on b.idciudad = c.idciudad and c.idpais = b.idpais \
group by 1, 2) pp on pp.idpais = m.idpais and pp.idciudad = m.idciudad and pp.max = m.maxrenta) u \
where u.idcategoria = (select idcategoria from categoria where lower(nombre) = lower('Horror'));"
    
    conexionCarga = accessBDD
    data = conexionCarga.sqlSelectCustom(sqlQuery)
    return data