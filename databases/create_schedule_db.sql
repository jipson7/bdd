BEGIN TRANSACTION;
CREATE TABLE teaching_assistants
(
  teaching_assistant_id INTEGER NOT NULL,
  ta_name TEXT NOT NULL,
  CONSTRAINT Key5 PRIMARY KEY (teaching_assistant_id)
);
INSERT INTO `teaching_assistants` VALUES (1,'bob');
INSERT INTO `teaching_assistants` VALUES (2,'sally');
INSERT INTO `teaching_assistants` VALUES (3,'alice');
INSERT INTO `teaching_assistants` VALUES (4,'alex');
INSERT INTO `teaching_assistants` VALUES (5,'caleb');
INSERT INTO `teaching_assistants` VALUES (6,'miguel');
INSERT INTO `teaching_assistants` VALUES (7,'elias');
INSERT INTO `teaching_assistants` VALUES (8,'luisa');
INSERT INTO `teaching_assistants` VALUES (9,'rebecca');
INSERT INTO `teaching_assistants` VALUES (10,'courtney');
INSERT INTO `teaching_assistants` VALUES (11,'josh');
INSERT INTO `teaching_assistants` VALUES (12,'jeremy');



CREATE TABLE "ta_prior_engagements" (
	`id`	INTEGER NOT NULL,
	`day_of_week`	INTEGER NOT NULL,
	`start_time`	time NOT NULL,
	`end_time`	time NOT NULL,
	`teaching_assistant_id`	INTEGER NOT NULL,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`teaching_assistant_id`) REFERENCES `teaching_assistants`(`teaching_assistant_id`)
);
INSERT INTO `ta_prior_engagements` VALUES (1,1,'12:40:00','14:00:00',1);
INSERT INTO `ta_prior_engagements` VALUES (2,3,'08:10:00','09:30:00',2);
INSERT INTO `ta_prior_engagements` VALUES (3,3,'08:10:00','09:30:00',12);
INSERT INTO `ta_prior_engagements` VALUES (4,1,'12:40:00','14:00:00',12);



CREATE TABLE "ta_assignments" (
	`assignment_id`	INTEGER NOT NULL,
	`solution`	INTEGER,
	`teaching_assistant_id`	INTEGER NOT NULL,
	`section_id`	INTEGER NOT NULL,
	PRIMARY KEY(`assignment_id`,`teaching_assistant_id`,`section_id`),
	FOREIGN KEY(`teaching_assistant_id`) REFERENCES `teaching_assistants`(`teaching_assistant_id`),
	FOREIGN KEY(`section_id`) REFERENCES `sections`(`section_id`)
);



CREATE TABLE sections
(
  section_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL,
  classroom_id INTEGER NOT NULL,
  day_of_week INTEGER NOT NULL,
  start_time time NOT NULL,
  end_time time NOT NULL,
  CONSTRAINT Key6 PRIMARY KEY (section_id),
  CONSTRAINT course_sections FOREIGN KEY (course_id) REFERENCES courses (course_id),
  CONSTRAINT section_classroom FOREIGN KEY (classroom_id) REFERENCES classrooms (classroom_id)
);
INSERT INTO `sections` VALUES (1,1,1,1,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (2,1,1,3,'08:10:00','09:30:00');
INSERT INTO `sections` VALUES (3,2,2,2,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (4,2,2,4,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (5,3,3,2,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (6,3,3,4,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (7,4,4,3,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (8,4,4,5,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (9,5,4,5,'08:10:00','09:30:00');
INSERT INTO `sections` VALUES (10,5,5,1,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (11,6,5,2,'12:40:00','14:00:00');
INSERT INTO `sections` VALUES (12,6,5,3,'12:40:00','14:00:00');


CREATE TABLE courses
(
  course_id INTEGER NOT NULL,
  course_name TEXT NOT NULL,
  prof_name TEXT,
  CONSTRAINT Key3 PRIMARY KEY (course_id)
);
INSERT INTO `courses` VALUES (1,'course1','');
INSERT INTO `courses` VALUES (2,'course2','');
INSERT INTO `courses` VALUES (3,'course3','');
INSERT INTO `courses` VALUES (4,'course4','');
INSERT INTO `courses` VALUES (5,'course5','');
INSERT INTO `courses` VALUES (6,'course6','');



CREATE TABLE classrooms
(
  classroom_id INTEGER NOT NULL,
  room_number TEXT NOT NULL,
  capacity INTEGER NOT NULL,
  CONSTRAINT Key2 PRIMARY KEY (classroom_id)
);
INSERT INTO `classrooms` VALUES (1,'room1',30);
INSERT INTO `classrooms` VALUES (2,'room2',30);
INSERT INTO `classrooms` VALUES (3,'room3',30);
INSERT INTO `classrooms` VALUES (4,'room4',30);
INSERT INTO `classrooms` VALUES (5,'room5',30);
CREATE INDEX IX_Relationship12 ON sections (classroom_id);
CREATE INDEX IX_Relationship11 ON sections (course_id);
COMMIT;
