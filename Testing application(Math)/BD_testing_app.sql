-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 13, 2020 at 03:13 PM
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
-- Database: `rspo`
--

-- --------------------------------------------------------

--
-- Table structure for table `test_answers`
--

CREATE TABLE `test_answers` (
  `question_id` int(5) NOT NULL,
  `answer` varchar(255) NOT NULL,
  `correctness` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_answers`
--

INSERT INTO `test_answers` (`question_id`, `answer`, `correctness`) VALUES
(1, 'x = 1', 1),
(1, 'x = -1', 0),
(1, 'x = 0', 0),
(1, 'x = 5', 0),
(1, 'x = -5', 0),
(2, 'x = 1', 1),
(2, 'x = 7', 0),
(2, 'x = 3', 0),
(2, 'x = -7', 0),
(2, 'x = 6', 0),
(2, 'x = -1', 0),
(3, 'x = 9', 1),
(3, 'x = -9', 0),
(3, 'x = 2', 0),
(3, 'x = -2', 0),
(3, 'x = 0', 0),
(3, 'x = 14', 0),
(3, 'x = 15', 0),
(4, 'a', 1),
(4, 'b', 0),
(15, '1', 1),
(15, '0', 0),
(15, '0', 0),
(15, '0', 0),
(15, '0', 0),
(15, '0', 0),
(15, '0', 0);

-- --------------------------------------------------------

--
-- Table structure for table `test_question`
--

CREATE TABLE `test_question` (
  `question_id` int(5) NOT NULL,
  `question` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_question`
--

INSERT INTO `test_question` (`question_id`, `question`) VALUES
(1, '5x + 5 = 10'),
(2, '7x + 7 = 14'),
(3, 'x + 3 = 12'),
(15, 'вопрос тест');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `FIO` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`login`, `password`, `FIO`, `role`) VALUES
('1', '1', 'test', 'Преподаватель'),
('a', 'abc', 'adasd', 'Пользователь'),
('admin', 'admin', 'admin adminovich adminov', 'Администратор'),
('b', 'b', 'b b b', 'Пользователь');

-- --------------------------------------------------------

--
-- Table structure for table `users_dates`
--

CREATE TABLE `users_dates` (
  `user_login` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users_dates`
--

INSERT INTO `users_dates` (`user_login`, `date`) VALUES
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('a', '10/21/2020'),
('b', '10/21/2020'),
('a', '10/21/2020');

-- --------------------------------------------------------

--
-- Table structure for table `users_info`
--

CREATE TABLE `users_info` (
  `user_login` varchar(255) NOT NULL,
  `cor_answers` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users_info`
--

INSERT INTO `users_info` (`user_login`, `cor_answers`, `time`) VALUES
('a', '33.33%', '5.62'),
('a', '100.00%', '32.12'),
('a', '100.00%', '14.11'),
('a', '25.00%', '7.23'),
('a', '75.00%', '13.71'),
('a', '25.00%', '17.21'),
('a', '75.00%', '11.77'),
('b', '0.00%', '6.13'),
('a', '25.00%', '15.11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `test_question`
--
ALTER TABLE `test_question`
  ADD PRIMARY KEY (`question_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`login`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `test_question`
--
ALTER TABLE `test_question`
  MODIFY `question_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
