CREATE TABLE avaliacao (
	id	INTEGER NOT NULL,
	tipo	TEXT NOT NULL,
	nmDiscip	TEXT NOT NULL,
	descricao	TEXT,
	nmProfessor	TEXT,
	nrSala	TEXT,
	data INTEGER,
	PRIMARY KEY(id)
);

CREATE TABLE plano_estudos (
	id	INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(id) REFERENCES TURMA(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE preferencia_usuario (
	nmPreferencia	TEXT,
	isActive	INTEGER,
	notifyTimeDiscip	INTEGER,
	strValue	TEXT,
	PRIMARY KEY(nmPreferencia)
);