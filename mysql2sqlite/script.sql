CREATE TABLE notificacao (
	idAula	INTEGER UNIQUE,
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	idAvaliacao	INTEGER,
	tipo	INTEGER NOT NULL,
	FOREIGN KEY(idAula) REFERENCES AULA(id) ON DELETE CASCADE,
	FOREIGN KEY(idAvaliacao) REFERENCES AVALIACAO(id) ON DELETE CASCADE
);
CREATE TABLE preferencia_usuario (
	nmPreferencia	TEXT,
	isActive	INTEGER,
	notifyTimeDiscip	INTEGER,
	strValue	TEXT,
	PRIMARY KEY(nmPreferencia)
);
CREATE TABLE plano_estudos (
	id	INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(id) REFERENCES TURMA(id) ON UPDATE CASCADE ON DELETE CASCADE
);
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