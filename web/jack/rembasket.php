<?php
	$id = $_GET['id'];//id of product to remove
	if(isset($_COOKIE["shopnet_login"])){//retrieval of user id from cookie
		$UserID = $_COOKIE['shopnet_login'];
	}
	elseif(isset($_COOKIE["shopnet"])){
		$UserID = $_COOKIE['shopnet'];
	}
	$user = $_COOKIE['shopnet'];//sql server details
	$DB_NAME = 'c1327650';
	$DB_HOST = 'ephesus.cs.cf.ac.uk';
	$DB_USER = 'c1327650';
	$DB_PASS = 'berlin';
	$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
	$inbasket = "DELETE FROM Basket WHERE ProductID = '$id' AND UserID = '$UserID'";//deletion of item from basket with id $id and Userid from cookie
	$bresult = $mysqli->query($inbasket) or die($mysqli->error.__LINE__);
	header("Location: basket.php?fb=del");//redirect to basket
?>
