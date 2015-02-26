<?php
	$id = $_GET['id'];//retrieve id of product to add to basket from the URL
	if(isset($_COOKIE["shopnet_login"])){//retrieve the userids from the cookies
		$UserID = $_COOKIE['shopnet_login'];
	}
	elseif(isset($_COOKIE["shopnet"])){
		$UserID = $_COOKIE['shopnet'];
	}
	$DB_NAME = 'c1327650';//mysql server details for connection
	$DB_HOST = 'ephesus.cs.cf.ac.uk';
	$DB_USER = 'c1327650';
	$DB_PASS = 'berlin';
	$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
	$inbasket = "SELECT Quantity FROM Basket WHERE ProductID = '$id' AND UserID = '$UserID'";//query to retrieve quantity of $id in basket
	$bresult = $mysqli->query($inbasket) or die($mysqli->error.__LINE__);
	$b = mysqli_fetch_assoc($bresult);
	if ($b == 0){//if not in basket then add to basket with quantity 1
		$dbquery = "INSERT INTO Basket(UserID, ProductID) VALUES ('" . $UserID . "','" . $id . "')";
		if(!$mysqli->query($dbquery)){
			echo 'Please quote this:' . $mysqli->errno . $mysqli->error . '';
		} else {
			header("Location: product.php?id=" . $id  . "");
		}
	} else {//if in basket then increment by 1 the quantity value
		$addone = "UPDATE Basket SET Quantity = Quantity + 1 WHERE ProductID = '$id' AND UserID = '$UserID'";
		if(!$mysqli->query($addone)){
			echo 'Please quote this:' . $mysqli->errno . $mysqli->error . '';
		} else {
			header("Location: product.php?id=" . $id  . "");
		}
	}
?>
