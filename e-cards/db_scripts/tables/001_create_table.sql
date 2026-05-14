CREATE TABLE tbl_collections (
    id SERIAL PRIMARY KEY,
    collectionSetName VARCHAR(100) NOT NULL,
    releaseDate DATE NOT NULL,
    totalCardsInCollection SMALLINT NOT NULL
);

CREATE TABLE tbl_types (
    id SERIAL PRIMARY KEY,
    typeName VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE tbl_stages (
    id SERIAL PRIMARY KEY,
    stageName VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE tbl_cards (
    id SERIAL PRIMARY KEY,
    hp SMALLINT,
    name VARCHAR(80) NOT NULL,
    info TEXT,
    attack VARCHAR(100),
    damage VARCHAR(20),
    weak VARCHAR(30),
    resis VARCHAR(30),
    retreat VARCHAR(20),
    cardNumberInCollection SMALLINT NOT NULL,
    collection_id INT NOT NULL,
    type_id INT NOT NULL,
    stage_id INT NOT NULL,
    CONSTRAINT fk_collection FOREIGN KEY (collection_id)
        REFERENCES tbl_collections (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_type FOREIGN KEY (type_id)
        REFERENCES tbl_types (id)
        ON DELETE RESTRICT,
    CONSTRAINT fk_stage FOREIGN KEY (stage_id)
        REFERENCES tbl_stages (id)
        ON DELETE RESTRICT
);

CREATE UNIQUE INDEX idx_cards_unique_number ON tbl_cards (collection_id, cardNumberInCollection);
CREATE INDEX idx_cards_collection ON tbl_cards (collection_id);
CREATE INDEX idx_cards_type ON tbl_cards (type_id);
CREATE INDEX idx_cards_stage ON tbl_cards (stage_id);
