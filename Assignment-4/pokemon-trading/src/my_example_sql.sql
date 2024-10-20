CREATE DATABASE pokemon_trading;
USE pokemon_trading;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(200),
    email VARCHAR(200)
);

CREATE TABLE cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200),
    rarity VARCHAR(200),
    PSA VARCHAR(200),
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

CREATE TABLE trades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    proposer_id INT,
    recipient_id INT,
    proposed_card_id INT,
    requested_card_id INT,
    status ENUM('pending', 'accepted', 'rejected'),
    FOREIGN KEY (proposer_id) REFERENCES users(id),
    FOREIGN KEY (recipient_id) REFERENCES users(id),
    FOREIGN KEY (proposed_card_id) REFERENCES cards(id),
    FOREIGN KEY (requested_card_id) REFERENCES cards(id)
);

INSERT INTO users (username, email)
VALUES
('AshKetchum', 'ash@pokemon.com'),
('MistyWater', 'misty@cerulean.com'),
('BrockRock', 'brock@pewtergym.com'),
('GaryOak', 'gary@pallet.com'),
('JessieRocket', 'jessie@teamrocket.com');

INSERT INTO cards (name, rarity, PSA, owner_id)
VALUES
('Pikachu', 'Common', 'Mint 9', 1),
('Charizard', 'Rare', 'Gem Mint 10', 2),
('Bulbasaur', 'Uncommon', 'Near Mint 8', 3),
('Squirtle', 'Common', 'Excellent 6', 4),
('Eevee', 'Rare', 'Mint 9', 1),
('Gyarados', 'Rare', 'Gem Mint 10', 2),
('Onix', 'Uncommon', 'Mint 9', 3),
('Snorlax', 'Uncommon', 'Near Mint 7', 4),
('Meowth', 'Common', 'Excellent 5', 5),
('Jigglypuff', 'Uncommon', 'Mint 9', 1);

INSERT INTO trades (proposer_id, recipient_id, proposed_card_id, requested_card_id, status)
VALUES
(1, 2, 1, 2, 'pending'),  -- Ash proposes to trade Pikachu for Misty's Charizard
(2, 3, 2, 3, 'pending'),  -- Misty proposes to trade Charizard for Brock's Bulbasaur
(4, 1, 4, 1, 'pending'),  -- Gary proposes to trade Squirtle for Ash's Pikachu
(3, 5, 3, 5, 'pending'),  -- Brock proposes to trade Bulbasaur for Jessie's Meowth
(5, 4, 5, 4, 'pending');  -- Jessie proposes to trade Meowth for Gary's Squirtle