-- Create a new database for Dungeons & Dragons
CREATE DATABASE dnd_db;

-- Use the newly created database so we can create tables in it
USE dnd_db;

-- Create a table for storing party information
CREATE TABLE parties (
    party_id INT PRIMARY KEY AUTO_INCREMENT,
    party_name VARCHAR(200) NOT NULL,
    campaign_name VARCHAR(200)
);


-- Create a table for storing guild information
CREATE TABLE guilds (
    guild_id INT PRIMARY KEY AUTO_INCREMENT,
    guild_name VARCHAR(200) NOT NULL,
    guild_master VARCHAR(200),
    guild_location VARCHAR(200)
);

-- Create a table for characters in the game
CREATE TABLE characters (
    character_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    race VARCHAR(200),
    class VARCHAR(200),
    level INT CHECK (level >= 1),
    alignment VARCHAR(200),
    hit_points INT,
    guild_id INT,
    party_id INT,
    FOREIGN KEY (guild_id) REFERENCES guilds(guild_id),
    FOREIGN KEY (party_id) REFERENCES parties(party_id)
);

-- Create a table for storing monster information
CREATE TABLE monsters (
    monster_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    type VARCHAR(200),
    hit_points INT
);

-- Create a table for storing fight information
CREATE TABLE fights (
    fight_id INT PRIMARY KEY AUTO_INCREMENT,
    party_id INT,
    fight_date DATE,
    result VARCHAR(200),
    FOREIGN KEY (party_id) REFERENCES parties(party_id)
);

-- Create a junction table for associating fights with monsters
CREATE TABLE fight_monsters (
    fight_id INT,
    monster_id INT,
    PRIMARY KEY (fight_id, monster_id),
    FOREIGN KEY (fight_id) REFERENCES fights(fight_id) ON DELETE CASCADE,
    FOREIGN KEY (monster_id) REFERENCES monsters(monster_id) ON DELETE CASCADE
);

-- Insert into guilds
INSERT INTO guilds (guild_name, guild_master, guild_location)
VALUES
	('The Silver Foxes', 'Vik Von Clause', 'Kezrk'),
    ('The Order of the Wolf', 'Tyrian Evenshroud', 'Neverwinter'),
    ('The Iron Fists', 'Dorian Blackthorn', 'Frosthaven'),
    ('The Emerald Enclave', 'Sylas Greenbriar', 'Woodland Vale'),
    ('The Crimson Blades', 'Aria Bloodstone', 'Shadowfell'),
    ('The Arcane Circle', 'Meredith Starfire', 'Mysthaven'),
    ('The Silver Serpents', 'Vesper Nightshade', 'Gloomhaven'),
    ('The Knights of Valor', 'Sir Cedric Lightbringer', 'Eldoria');

-- Insert into parties
INSERT INTO parties (party_name, campaign_name)
VALUES
	('The Donnies', 'The Curse of Strahd'),
    ('The Holy Order for the Prevention of Evil', 'Vecna: Eve of Ruin'),
    ('The Sword of Scales', 'Tyranny of Dragons'),
    ('The Shadow Guardians', 'Secrets of the Forgotten Realms'),
    ('The Arcane Companions', 'The Lost City of Omu'),
    ('The Dragon Hunters', 'The Rise of Tiamat'),
    ('The Silver Sentinels', 'The War of the Ancients'),
    ('The Wild Adventurers', 'The Quest for the Holy Grail');

-- Insert into characters
INSERT INTO characters (name, race, class, level, alignment, hit_points, guild_id, party_id)
VALUES
	('Celaena', 'Dark-Elf', 'Rogue', 3, 'Chaotic Neutral', 24, 1, 1),
	('Vugs', 'Goliath', 'Barbarian', 3, 'Neutral', 32, 1, 1),
	('Cassius Felst', 'High-Elf', 'Cleric', 3, 'Neutral', 24, 1, 1),
	('Elandor Venkalyn', 'Eladrin', 'Druid', 3, 'Chaotic Good', 24, 1, 1),
	('Zaphiel', 'Aasimar', 'Sorcerer', 3, 'Chaotic Evil', 14, 1, 1),
	('Elyndra', 'Half-Elf', 'Cleric', 5, 'Lawful Good', 32, NULL, 3),
	('Fern', 'Human', 'Bard', 4, 'Lawful Neutral', 24, 2, 3),
	('Sylvie', 'Human', 'Paladin', 5, 'Lawful Good', 55, 2, 2);

-- Insert into monsters
INSERT INTO monsters (name, type, hit_points)
VALUES
	('Goblin', 'Humanoid', 15),
    ('Were-Wolf', 'Humanoid', 32),
    ('Anvilwrought Raptor', 'Construct', 48),
    ('Dragon Wyrmling', 'Dragon', 60),
    ('Lich', 'Undead', 135),
    ('Orc', 'Humanoid', 30),
    ('Fire Elemental', 'Elemental', 102),
    ('Beholder', 'Aberration', 180),
    ('Kobold', 'Humanoid', 5),
    ('Mimic', 'Monstrosity', 58),
    ('Basilisk', 'Monstrosity', 52);

-- Insert into fights
INSERT INTO fights (party_id, fight_date, result)
VALUES
    (1, '2024-09-01', 'Victory'),
    (2, '2023-07-04', 'Defeat'),
    (1, '2024-08-15', 'Victory'),
    (3, '2024-07-20', 'Defeat'),
    (2, '2024-06-30', 'Victory'),
    (1, '2024-05-10', 'Victory'),
    (3, '2024-04-25', 'Defeat'),
    (2, '2024-03-15', 'Victory');

-- Insert into fight_monsters
INSERT INTO fight_monsters (fight_id, monster_id)
VALUES
	(1, 1), -- Goblin in fight 1
    (1, 2), -- Werewolf in fight 1
    (1, 3), -- Anvilwrought Raptor in fight 1
    (2, 4), -- Dragon Wyrmling in fight 2
    (2, 5), -- Lich in fight 2
    (3, 6), -- Orc in fight 3
    (3, 7), -- Fire Elemental in fight 3
    (4, 8), -- Beholder in fight 4
    (5, 9), -- Kobold in fight 5
    (6, 10), -- Mimic in fight 6
    (7, 11), -- Basilisk in fight 7
    (8, 1), -- Goblin in fight 8
    (8, 3); -- Anvilwrought Raptor in fight 8

-- Query to check inserted data in characters table
SELECT *
FROM characters;

-- Query to find the average level of characters in a specific guild (guild_id = 1)
SELECT AVG(level) AS average_level
FROM characters
WHERE guild_id = 1;

-- Retrieve all characters along with their race, class, and associated guild name
SELECT c.name, c.race, c.class, g.guild_name
FROM characters c
JOIN guilds g ON c.guild_id = g.guild_id
ORDER BY c.name; -- Sort by character name

SELECT SUM(m.hit_points) AS total_monster_hp
FROM fights f
JOIN fight_monsters fm ON f.fight_id = fm.fight_id
JOIN monsters m ON fm.monster_id = m.monster_id
WHERE f.fight_id = 1; -- Replace with the specific fight_id you're querying

-- Retrieve fight details and monster information
SELECT f.fight_id, f.fight_date, m.name AS monster_name, m.type AS monster_type
FROM fights f
JOIN fight_monsters fm ON f.fight_id = fm.fight_id
JOIN monsters m ON fm.monster_id = m.monster_id
WHERE f.fight_id = 1;

-- Calculate average hit points of monsters in a specific fight
SELECT f.fight_id, AVG(m.hit_points) AS average_hp
FROM fight_monsters fm
JOIN monsters m ON fm.monster_id = m.monster_id
JOIN fights f ON fm.fight_id = f.fight_id
WHERE f.fight_id = 1
GROUP BY f.fight_id;

-- Stored procedure
DELIMITER //

CREATE PROCEDURE get_total_fights_by_party_id(IN in_party_id INT)
BEGIN
    SELECT COUNT(*) AS total_fights
    FROM fights
    WHERE party_id = in_party_id;
END //

DELIMITER ;

-- Using the stored procedure
CALL get_total_fights_by_party_id(1);  -- Replace '1' with the actual party_id you want to query

-- Delete query
DELETE FROM fights
WHERE fight_id = 8;  -- Insert the fight id you would like to delete (fight 8)

-- Check that the delete worked correctly
SELECT *
FROM fights;

-- Creative Use:
-- Organising and Tracking Campaigns with the DnD Database
-- 1. Party Management:
--    The `parties` table allows DMs to track multiple adventuring groups, their names, and associated campaigns, while the `characters` table links characters to their respective parties.

-- 2. Character Development:
--    By storing character attributes like hit points and guild affiliations, DMs can tailor challenges and storylines based on party strengths and weaknesses.

-- 3. Fight Records:
--    The `fights` and `fight_monsters` tables document combat encounters, helping DMs analyze total fights and average monster stats to balance future combat scenarios.

-- 4. Storyline Development:
--    Campaigns can be tracked by the `campaign_name` field, allowing DMs to ensure continuity and easily adapt to evolving storylines.

-- 5. Post-Game Review:
--    After sessions, DMs can review performance data to inform future gameplay and engage players by discussing character growth and plot development.

-- This database structure streamlines campaign management, allowing DMs to focus on storytelling while keeping all mechanics organized, leading to a richer gaming experience.