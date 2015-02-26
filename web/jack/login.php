<?php
			$email = $_POST['email'];//retrieve login details from form
			$DBNAME = 'c1327650';
			$DBHOST = 'ephesus.cs.cf.ac.uk';//sql connect details
			$DBUSER = 'c1327650';
			$DBPASS = 'berlin';
			$mysqli = new mysqli($DBHOST, $DBUSER, $DBPASS, $DBNAME);
			if (mysqli_connect_errno()) {
				printf("Failed: %s\n", mysqli_connect_error());
				exit();
			}
			$passw = "SELECT Password FROM Users WHERE Email='$email'"; //select credentials where email provided is in the database
			$passq = $mysqli->query($passw) or die($mysqli->error.__LINE__);
			$passz = mysqli_fetch_assoc($passq);
			$pass = password_verify($_POST['password'],$passz['Password']);//verify password against hashed, salted password
			if ($pass == TRUE){
				$login = "SELECT UserID FROM Users WHERE Email='$email'";
				$old = $_COOKIE['shopnet'];//record old user id to merge items into basket
				$result = $mysqli->query($login) or die($mysqli->error.__LINE__);
				$count = mysqli_num_rows($result);
				$UserID = mysqli_fetch_assoc($result);
				$UserID = implode($UserID); //Add feature to increase basket by one when item is in both baskets
				$lmq = "SELECT * FROM Basket WHERE UserID = '$old'";
				$lmqr = $mysqli->query($lmq);
				while ($lmqrr = mysqli_fetch_assoc($lmqr)){
					$ispresentq = "SELECT * IN Basket WHERE (ProductID = '$ProductID') AND (UserID = '$UserID')";
					if (!$mysqli->query($ispresentq)){
						$add = "INSERT INTO Basket(UserID, ProductID, Quantity) VALUES ('" . $UserID . "','" . $lmqrr['ProductID'] . "','" . $lmqrr['Quantity'] . "')";
						$mysqli->query($add);
					} else {
						$mergebaskets = "UPDATE Basket SET UserID = '$UserID' WHERE UserID = '$old'";
						$mysqli->query($mergebaskets);
					}
				}
				setcookie("shopnet_login",$UserID,time()+1800,'/');
				setcookie("shopnet","",time()-1,'/');
				header("Location: Home.php");
			} else {
				header("Location: Home.php?fb=fail");//redirect failed login to home

			}

		mysqli_close($mysqli);//close mysql connection
?>
  