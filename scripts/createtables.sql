create artista(
IdArtista serial primary key,
Nombre_artista varchar(100)
);

create genero(
IdGenero serial primary key,
Nombre_genero varchar(100)
);

create song(
	IdSong serial primary key,
	name varchar(100),
	duration_ms int,
	explicit bool,
	yearsong date,
	popularity int,
	danceability numeric,
	energy numeric,
	keysong int,
	loudness numeric,
	mode int,
	speechiness numeric,
	acousticness numeric,
	instrumentalness numeric,
	liveness numeric,
	valence numeric,
	tempo numeric,
	idArtista int references artista(IdArtista),
	idGenero int references genero(IdGenero)
);


create alldata(
	artist varchar(100)
	sont varchar(100),
	duration_ms int,
	explicit bool,
	yearsong date,
	popularity int,
	danceability numeric,
	energy numeric,
	keysong int,
	loudness numeric,
	mode int,
	speechiness numeric,
	acousticness numeric,
	instrumentalness numeric,
	liveness numeric,
	valence numeric,
	tempo numeric,
	genre varchar(100)
);


