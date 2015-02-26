<?php
	if(isset($_COOKIE["shopnet_login"])){//if cookie is present, set the cookie's expiration to the past, else direct to home.
		setcookie("shopnet_login","",time()-1,"/");
		$UserID = uniqid("",true);
		setcookie("shopnet",$UserID,time()+1800,'/');
		header("Location: Home.php");
	}
	else {
		header("Location: Home.php");
	}
?>
