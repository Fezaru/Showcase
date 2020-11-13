-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 13, 2020 at 03:22 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trpo`
--

-- --------------------------------------------------------

--
-- Table structure for table `test_answers`
--

CREATE TABLE `test_answers` (
  `test` int(5) NOT NULL,
  `question_id` int(100) NOT NULL,
  `answer1` double NOT NULL,
  `answer2` double NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_answers`
--

INSERT INTO `test_answers` (`test`, `question_id`, `answer1`, `answer2`, `id`) VALUES
(1, 1, 5, -2, 1),
(1, 2, 3, 1, 2),
(1, 3, 15, -3, 3),
(1, 4, 18, 22, 4),
(1, 5, -2, -10, 5),
(1, 6, 6, -3, 6),
(1, 7, 0, -3, 7),
(1, 8, 2, 4, 8),
(1, 9, 0, 1, 9),
(1, 10, 4, -7, 10),
(1, 11, -5, 4, 11),
(1, 12, 3, 2, 12),
(1, 13, 20, 60, 13),
(1, 14, 10, 0, 14),
(1, 15, 4, -1.5, 15),
(2, 16, 1, 2, 16),
(2, 16, -1, -2, 17),
(2, 17, 1, 1, 18),
(2, 17, -1.8, -0.6, 19),
(2, 18, 2, 3, 20),
(2, 18, -2, -3, 21),
(2, 19, -1, 9, 22),
(2, 19, 9, -1, 23),
(2, 20, -2, 2, 24),
(2, 20, 2, -2, 25),
(2, 21, -2, 3, 26),
(2, 21, 2, -3, 27);

-- --------------------------------------------------------

--
-- Table structure for table `test_questions`
--

CREATE TABLE `test_questions` (
  `test` int(5) NOT NULL,
  `question_id` int(100) NOT NULL,
  `question1` varchar(300) NOT NULL,
  `question2` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_questions`
--

INSERT INTO `test_questions` (`test`, `question_id`, `question1`, `question2`) VALUES
(1, 1, 'x/5 = 1', 'x + y = 3'),
(1, 2, 'x + y = y + 3', 'y / x = 1/3'),
(1, 3, '2x + y = 27', 'x + y = 12'),
(1, 4, '1/4x + 1/4y = 10', '2x - y = 14'),
(1, 5, 'x - y = -12', '7x - y = 0'),
(1, 6, '3x + 2y = 12', 'x + y = 3'),
(1, 7, 'x - 2y = 6', '3x + 2y = -6'),
(1, 8, 'x = y/2', 'x + 7y = 30'),
(1, 9, '13x + y = 7x -5y + 6', '12y + x = 12'),
(1, 10, 'x + y = -7x - 3y + 4', 'x = 2(x + y/2) + 3'),
(1, 11, '2x + 5y = 10', '2x = 10 - 5y'),
(1, 12, 'y = 4 -2x/3', 'y = 3x - 7'),
(1, 13, '12x - 3y = 60', 'x/5 + y/10 = 10'),
(1, 14, '7x = 70', 'x + 3y = 10'),
(1, 15, 'x + y = -x -y + 5', 'x +2y = 1'),
(2, 16, '3x^2*y^2 + x^2 -3xy = 7', '10x^2*y^2 + 3x^2 -20xy = 3'),
(2, 17, '(x + 2y)(2x - y + 1) = 6', '(2x - y + 1) = 2/3(x + 2y)'),
(2, 18, '3x^2 + xy - 2y^2 = 0', '2x^2 - 3xy + y^2 = -1'),
(2, 19, 'x + y - 8 = 0', 'x^2 + y^2 - 82 = 0'),
(2, 20, '3x^2 + 2xy - y^2 = 0', 'x^2 - 3xy = 16'),
(2, 21, 'xy + 2y^2 = 12', 'x^2 + 4xy = -20');

-- --------------------------------------------------------

--
-- Table structure for table `test_rating`
--

CREATE TABLE `test_rating` (
  `user` varchar(32) DEFAULT NULL,
  `test` int(11) DEFAULT NULL,
  `best_result` double DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_rating`
--

INSERT INTO `test_rating` (`user`, `test`, `best_result`, `id`) VALUES
('1', 1, 1, 1),
('artem', 1, 0, 2),
('abcabc', 1, 1, 3),
('1', 2, 4, 4),
('artem', 2, 2, 5),
('lyubamil', 1, 1, 6),
('lyubamil', 2, 2, 7),
('alexandr', 1, 1, 8),
('alexandr', 2, 0, 9);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `login` varchar(30) DEFAULT NULL,
  `pass` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `login`, `pass`) VALUES
(8, '1', '1'),
(9, '123', '123'),
(10, '1234', '1234'),
(11, '12345', '12345'),
(12, '111', '698d51a19d8a121ce581499d7b701668'),
(13, '1351', 'dcfa8d5624e1241463b640880ebf914f'),
(14, '3f1gg1', '384028b0a178129dfb32e1ba29824b7c'),
(15, 'artem', '3ba664d81bbb51266c00f328f029fdf1'),
(16, 'artem', '3ba664d81bbb51266c00f328f029fdf1'),
(17, 'artem', '3ba664d81bbb51266c00f328f029fdf1'),
(18, 'artem', '3ba664d81bbb51266c00f328f029fdf1'),
(19, '1234', '81dc9bdb52d04dc20036dbd8313ed055'),
(20, '1234', '81dc9bdb52d04dc20036dbd8313ed055'),
(21, '1', 'c4ca4238a0b923820dcc509a6f75849b'),
(22, '1', 'c4ca4238a0b923820dcc509a6f75849b'),
(23, 'artem', '3ba664d81bbb51266c00f328f029fdf1'),
(24, '1', 'c4ca4238a0b923820dcc509a6f75849b'),
(25, '1', 'c4ca4238a0b923820dcc509a6f75849b'),
(26, '004k22dk', '3ba664d81bbb51266c00f328f029fdf1'),
(27, '1234', '81dc9bdb52d04dc20036dbd8313ed055'),
(28, 'artem', '9605959095f1e07ba7628a197088bd70'),
(29, 'aretm', '9605959095f1e07ba7628a197088bd70'),
(30, 'artem', '9d7790ded179278910129447b7e866ae'),
(31, '1234', '81dc9bdb52d04dc20036dbd8313ed055'),
(32, '1234', '81dc9bdb52d04dc20036dbd8313ed055'),
(33, '123', '202cb962ac59075b964b07152d234b70'),
(34, '123', '202cb962ac59075b964b07152d234b70'),
(35, '213', '9b04d152845ec0a378394003c96da594'),
(36, '1234', '827ccb0eea8a706c4c34a16891f84e7b'),
(37, '1', '698d51a19d8a121ce581499d7b701668'),
(38, '1', '900150983cd24fb0d6963f7d28e17f72'),
(39, 'lyuba', '202cb962ac59075b964b07152d234b70'),
(40, 'artemartem', '202cb962ac59075b964b07152d234b70'),
(41, 'artme', '202cb962ac59075b964b07152d234b70'),
(42, '123456789', '202cb962ac59075b964b07152d234b70'),
(43, 'abcabc', 'c4ca4238a0b923820dcc509a6f75849b'),
(44, 'lyubamil', '74db120f0a8e5646ef5a30154e9f6deb'),
(45, 'alexandr', '698d51a19d8a121ce581499d7b701668');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `test_answers`
--
ALTER TABLE `test_answers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_questions`
--
ALTER TABLE `test_questions`
  ADD UNIQUE KEY `question_id` (`question_id`);

--
-- Indexes for table `test_rating`
--
ALTER TABLE `test_rating`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `test_answers`
--
ALTER TABLE `test_answers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `test_rating`
--
ALTER TABLE `test_rating`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
