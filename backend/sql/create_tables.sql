CREATE TABLE IF NOT EXISTS recipe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    instructions TEXT NOT NULL,
    link TEXT NOT NULL,
    comments TEXT NOT NULL,
    servings TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS recipe_ingredient (
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    preparation TEXT,
    quantity TEXT,
    PRIMARY KEY (recipe_id, ingredient_id)
    FOREIGN KEY (recipe_id) REFERENCES recipe (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredient (id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS tag (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS recipe_tag (
    recipe_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (recipe_id, tag_id),
    FOREIGN KEY (recipe_id) REFERENCES recipe (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tag (id) ON DELETE CASCADE ON UPDATE CASCADE
);

