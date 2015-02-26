<?php
	$id = $_GET['id'];//id of product to change quantity
	$q = $_POST['qno'];//new quantity number from POST
	if(isset($_COOKIE["shopnet_login"])){
		$UserID = $_COOKIE['shopnet_login'];
	}
	elseif(isset($_COOKIE["shopnet"])){
		$UserID = $_COOKIE['shopnet'];
	}
	$user = $_COOKIE['shopnet'];
	$DB_NAME = 'c1327650';
	$DB_HOST = 'ephesus.cs.cf.ac.uk';
	$DB_USER = 'c1327650';
	$DB_PASS = 'berlin';
	$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
	if ($q == 0){//if quantity to set is 0, remove from basket, else just ammend quantity
		$change = "DELETE FROM Basket WHERE ProductID = '$id' AND UserID = '$UserID'";
	} else{
	$change = "UPDATE Basket SET Quantity = '$q' WHERE ProductID = '$id' AND UserID = '$UserID'";
	}
	if(!$mysqli->query($change)){
		echo 'Please quote this:' . $mysqli->errno . $mysqli->error . '';//if something goes wrong
	} else {
		header("Location: basket.php?fb=upd"); //redirect to basket.php
	}
?>
