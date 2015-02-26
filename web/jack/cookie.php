<?php
	$connect = mysqli_connect("ephesus.cs.cf.ac.uk","c1327650","berlin","c1327650");//connection details, cookie and user id assignment
	if(isset($_COOKIE["shopnet_login"])){
		$UserID = $_COOKIE['shopnet_login'];
		$basketresult = "SELECT * FROM Basket WHERE UserID='".$_COOKIE['shopnet_login']."'";
		setcookie("shopnet_login",$UserID,time()+1800,'/');
		$adminq = "SELECT * IN Admin WHERE UserID = '$UserID'";
		$admina = $mysqli->query($adminq);
		if (mysqli_num_rows($admina) == 0){
			$admin = 0;
		}else{
			$admin = 1;
		}
	}
	elseif(isset($_COOKIE["shopnet"])){
		$UserID = $_COOKIE['shopnet'];
		$basketresult = "SELECT * FROM Basket WHERE UserID='".$_COOKIE['shopnet']."'";
		setcookie("shopnet",$UserID,time()+1800,'/');	
	}
	else{
		$UserID = uniqid("",true);
		setcookie("shopnet",$UserID,time()+1800,'/');
		$basketresult = "SELECT * FROM Basket WHERE UserID='".$_COOKIE['shopnet']."'";
	}
?>