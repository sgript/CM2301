<?php		
	$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
	$dbquery = "SELECT Firstname FROM Users WHERE UserID='$UserID'";
	$IDresult = $mysqli->query($dbquery) or die($mysqli->error.__LINE__);
	$count = mysqli_num_rows($IDresult);
	$Names = mysqli_fetch_assoc($IDresult);
	if(isset($_GET['fb'])){
		$fb = $_GET['fb'];
		if($fb == 'fail'){
			echo "Login unsuccessful, please try again.";
		}
	}
	if (($count != 0) and (isset($_COOKIE["shopnet_login"]))) {//deal with logins, unsuccessful, successful and yet-to-be-completed
		$Name = implode($Names);
		echo "Welcome back, " . $Name . ". Not " . $Name . "? <a href='logout.php'>Sign in as a different user or log out.</a>";
	} else {
		echo "<form method='post' action='login.php'>";	
		echo 	"Email address: <br/><input type='text' size=15 name='email' placeholder='Email address' /><br/>";
		echo 	"Password: <br/><input size=15 type='password' name='password' placeholder='Password'/><br/>";
		echo 	"<input type='submit' name='submit' value='Login'/>";
		echo 	"</form>";
		echo "<p>Not a member?<br/> <a href='register.php'>Register now!</a></p>";
	}
	$basket = "SELECT SUM(Quantity) As Totalquant FROM Basket WHERE UserID='$UserID'";
	$num = mysqli_query($connect,$basket);
	$bresult = mysqli_fetch_assoc($num) or die($mysqli->error.__LINE__);
	echo "<a href='basket.php' id='basket'><img src='images/basket.png' height=70 id='basket'/></a>";
	echo $bresult['Totalquant'];
?>