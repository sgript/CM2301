<?php //This file checks which cookies are set and redirects the user if they are not registered. If they are registered then they may continue, 
	if(isset($_COOKIE["shopnet_login"])){					//where all of their items are deletec from the basket.
		$UserID = $_COOKIE['shopnet_login'];
	}
	elseif(isset($_COOKIE["shopnet"])){
		header("Location: basket.php?fb=nolog");
	}
	$DB_NAME = 'c1327650';
	$DB_HOST = 'ephesus.cs.cf.ac.uk';
	$DB_USER = 'c1327650';
	$DB_PASS = 'berlin';
	$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
	$inbasket = "DELETE FROM Basket WHERE UserID = '$UserID'";
	$bresult = $mysqli->query($inbasket) or die($mysqli->error.__LINE__);
	header("Location: basket.php?fb=del");
?>
