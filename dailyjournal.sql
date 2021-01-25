CREATE TABLE "Journal_Entries" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	Date,
	`topic`	TEXT NOT NULL,
    `entry` text NOT NULL,
    `mood_id` INTEGER NOT NULL,
    `hashtag_id` INTEGER NOT NULL
	FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
	FOREIGN KEY(`hashtag_id`) REFERENCES `HashTags`(`id`)
);

CREATE Table "Moods" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood` TEXT
);

CREATE Table "HashTags" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tag` TEXT
);

INSERT INTO "Moods" VALUES (null, "Happy");
INSERT INTO "Moods" VALUES (null, "Stressed");
INSERT INTO "Moods" VALUES (null, "Lost");
INSERT INTO "Moods" VALUES (null, "Proud")

INSERT INTO "Journal_Entries" VALUES (null, "01/02/2021","sql","it sucks","1","1");
INSERT INTO "Journal_Entries" VALUES (null, "01/03/2021","what","blah","2","3");

INSERT INTO "HashTags" VALUES (null, "#python");
INSERT INTO "HashTags" VALUES (null, "#sql");

ALTER Table Journal_Entries add `hashtag_id` INTEGER

SELECT
            j.id,
            j.date,
            j.topic,
            j.entry,
            j.mood_id
        FROM Journal_Entries j
        WHERE j.entry LIKE '%debugging%';
        
SELECT * FROM HashTags;
