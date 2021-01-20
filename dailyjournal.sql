CREATE TABLE "Journal_Entries" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	Date,
	`topic`	TEXT NOT NULL,
    `entry` text NOT NULL,
    `mood_id` INTEGER NOT NULL,
	FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE Table "Moods" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood` TEXT
);

INSERT INTO "Moods" VALUES (null, "Happy");
INSERT INTO "Moods" VALUES (null, "Stressed");
INSERT INTO "Moods" VALUES (null, "Lost");

INSERT INTO "Journal_Entries" VALUES (null, "01/02/2021","sql","it sucks","1");
INSERT INTO "Journal_Entries" VALUES (null, "01/03/2021","what","blah","2");
INSERT INTO "Journal_Entries" VALUES (null, "01/04/2021","delete this","blah","2");

SELECT 
m.id,
m.mood
FROM Moods m;