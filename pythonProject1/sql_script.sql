create database BookClub;
USE BookClub;

CREATE USER 'almalika'@'localhost' IDENTIFIED BY 'cfg2023';
GRANT ALL PRIVILEGES ON *.* TO 'almalika'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE TABLE Books (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(200),
author VARCHAR(200),
publication_year INT,
isbn VARCHAR(13), -- ISBNs are 13 digits
genre VARCHAR(200)
);

INSERT INTO Books
(title, author, publication_year, isbn, genre)
VALUES
('Queen', 'Queen', 2012, 9781617130137, 'Music'),
('Queen of Our Times: The Life of Elizabeth II', 'Robert Hardman', 2022, 9781529063417, 'Biography'),
('The White Queen', 'Philippa Gregory', 2009, 9781847374554, 'Historical Fiction'),
('The Black Queen', 'Jumata Emill', 2023, 9780702322945, 'Young Adult'),
('Queens: 3,000 Years of the Most Powerful Women in History', 'Victoria Crossman', 2020, 9780702301902, 'History'),
('Cleopatra: Last Queen of Egypt', 'Joyce Tyldesley', 2009, 9781861979018, 'History'),
('Diary of a Drag Queen', 'Crystal Rasmissen with Tom Rasmussen', 2019, 9780374538576, 'Memoir'),
('Girl, Goddess, Queen', 'Bea Fitzgerald', 2023, 9780241624272, 'Fiction'),
('Queen of the Damned', 'Anne Rice', 1988, 9780345366762, 'Fantasy'),
('The African Queen', 'C.S. Forester', 1935, 9780316289104, 'Adventure'),
('Queen of Shadows', 'Sarah J. Maas', 2015, 9781619636040, 'Fantasy'),
('The Queen of Attolia', 'Megan Whalen Turner', 2000, 9780688178594, 'Young Adult'),
('Queen of Air and Darkness', 'Cassandra Clare', 2018, 9781442468436, 'Fantasy'),
('The Red Queen', 'Philippa Gregory', 2010, 9781416563703, 'Historical Fiction'),
('The Iron Queen', 'Julie Kagawa', 2011, 9780373210329, 'Young Adult'),
('The Queen of Tearling', 'Erika Johansen', 2014, 9780062290380, 'Fantasy'),
('Queen of Snow', 'Laura Byron and Jessie Cal', 2019, 9781797761986, 'Fantasy'),
('The Queen''s Fool', 'Philippa Gregory', 2003, 9780743246071, 'Historical Fiction'),
('Queenie', 'Candice Carty-Williams', 2019, 9781501196010, 'Fiction'),
('The Queen of the Night', 'Alexander Chee', 2016, 9780544106604, 'Historical Fiction'),
('The Queen of Zombie Hearts', 'Gena Showalter', 2014, 9780373211449, 'Young Adult'),
('Queen Bee', 'Dorothea Benton Frank', 2019, 9780062861212, 'Fiction'),
('The Queen''s Poisoner', 'Jeff Wheeler', 2016, 9781503953306, 'Fantasy'),
('The Queen''s Resistance', 'Rebecca Ross', 2020, 9780062471397, 'Fantasy'),
('The Queen''s Rising', 'Rebecca Ross', 2018, 9780062471342, 'Fantasy'),
('The Queen of Sorrow', 'Sarah Beth Durst', 2018, 9780062413389, 'Fantasy'),
('The Queen''s Gambit', 'Walter Tevis', 1983, 9780586071116, 'Fiction'),
('Queen Takes Knights', 'Joely Sue Burkhart', 2020, 9781941637641, 'Fantasy'),
('Queen Takes King', 'Joely Sue Burkhart', 2021, 9781941637795, 'Fantasy'),
('Queen Takes Checkmate', 'Joely Sue Burkhart', 2021, 9781941637900, 'Fantasy'),
('Queen Takes Rook', 'Joely Sue Burkhart', 2020, 9781941637634, 'Fantasy'),
('The Queen''s Fortune', 'Allison Pataki', 2020, 9780593128187, 'Historical Fiction'),
('Queenie Malone''s Paradise Hotel', 'Ruth Hogan', 2019, 9780062955348, 'Fiction'),
('The Queen of All That Dies', 'Laura Thalassa', 2015, 9781310623183, 'Science Fiction'),
('The Queen of All That Lives', 'Laura Thalassa', 2015, 9781311438245, 'Science Fiction'),
('The Queen of All That Falls', 'Laura Thalassa', 2016, 9781370457837, 'Science Fiction'),
('The Queen''s Weapons', 'Anne Bishop', 2021, 9780451491667, 'Fantasy'),
('The Queen of Nothing', 'Holly Black', 2019, 9780316310426, 'Fantasy'),
('The Queen''s Assassin', 'Melissa de la Cruz', 2020, 9780525515913, 'Fantasy'),
('The Queen''s Knickers', 'Nicholas Allen', 2000, 9780099413141, 'Children Books');

SELECT * FROM Books;
