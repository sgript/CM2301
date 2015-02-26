<?php
	//connect to the mysqli servers at uni, assign userid if not set and if it is reset the cookie so it will expire after 30 minutes inactivity.
	$connect = mysqli_connect("ephesus.cs.cf.ac.uk","c1327650","berlin","c1327650");
	if(isset($_COOKIE["shopnet_login"])){
		$UserID = $_COOKIE['shopnet_login'];
		setcookie("shopnet_login",$UserID,time()+1800,'/');
		$DB_NAME = 'c1327650';
		$DB_HOST = 'ephesus.cs.cf.ac.uk';
		$DB_USER = 'c1327650';
		$DB_PASS = 'berlin';
		$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
		$rquery = "SELECT * FROM Administrators WHERE UserID = '$UserID'";
		$rresult = $mysqli->query($rquery) or die($mysqli->error.__LINE__); 
		if (mysqli_num_rows($rresult) = 0){
			header("Location: Home.php");
		}

	}
	else{
		header("Location: Home.php");
	}
?>
<!DOCTYPE html >
<html lang="en">
	<head>
		<title>Shopnet - Product view</title>
		<meta charset="utf-8" />
		<link rel="stylesheet" type="text/css" href="Home.css">
	
	</head>
	<body>
		<h1>
			<header>
				<a href="Home.php"><img src="Banner.png" id="Top" alt="Shopnet Home" width=300 Title="Shopnet Home" /></a>
				<form method="post" action="query.php" id='mainQuery'>
					<input type="text" name="searchTerm" placeholder="Search for a product..."/>
					<select name="category">
					<?php
					$DB_NAME = 'c1327650';
					$DB_HOST = 'ephesus.cs.cf.ac.uk';
					$DB_USER = 'c1327650';
					$DB_PASS = 'berlin';
					$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
					$dquery = "SELECT DISTINCT Category FROM Products";
					$dresult = $mysqli->query($dquery) or die($mysqli->error.__LINE__); 
					echo "<option value='.' selected>All categories</option>";
					while ($dropdown = mysqli_fetch_assoc($dresult)){
						$drop = implode($dropdown);//fetch dropdown list from database and display it
						echo "<option value=" . urlencode($drop) .">" . $drop . "</option>";
						$subq = "SELECT DISTINCT Subcategory FROM Products WHERE Category='$drop'";
						$subr = $mysqli->query($subq) or die($mysqli->error.__LINE__);
						while ($Subc = mysqli_fetch_assoc($subr)){
							$Subd = implode($Subc);
							echo "<option value=" . urlencode($Subd) . ">|--" . $Subd . "</option>";
						}
					}
					?>
					<input type="submit" name="submit" value="Go!"/>
				</form>
			</header>
		</h1>	
		<div id="wrapper">
		<nav id="navigation">
			<ul>
				<li><a href=Home.php>Home</a></li>
				<li id='cat'>Categories</li>
				<hr>
				<?php
					$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
					$query = "SELECT DISTINCT Category FROM Products";
					$result = $mysqli->query($query) or die($mysqli->error.__LINE__); 
					while ($Category = mysqli_fetch_assoc($result)){
						$Cat = implode($Category);
						echo "<li><a href=query.php?cat=" . $Cat .">" . $Cat . "</a></li>";
						$subquery = "SELECT DISTINCT Subcategory FROM Products WHERE Category='$Cat'";
						$subresult = $mysqli->query($subquery) or die($mysqli->error.__LINE__);
						$i = 0;
						echo "<ul>";
						while ($Subcategory = mysqli_fetch_assoc($subresult)){
							$j = mysqli_num_fields($subresult);
							$Sub = implode($Subcategory);
							$i ++;
							echo "<li><a href=query.php?cat=" . $Sub . ">-" . $Sub . "</a></li>";//fetch category list from databse and display it
						} echo "</ul>";
					}
				?>
				<hr>
			</ul>
		</nav>
		<div id="rightcol">
			<?php		
				$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
				$dbquery = "SELECT Firstname FROM Users WHERE UserID='$UserID'";
				$IDresult = $mysqli->query($dbquery) or die($mysqli->error.__LINE__);
				$count = mysqli_num_rows($IDresult);
				$Names = mysqli_fetch_assoc($IDresult);
				if ($count != 0){
					$Name = implode($Names);
					echo "Welcome back, " . $Name . ". Not " . $Name . "? <a href='logout.php'>Sign in as a different user or log out.</a>";//if you're logged in it will greet you
				} else {
					echo "<form method='post' action='login.php'>";	
					echo 	"Email address: <br/><input type='text' name='email' placeholder='Email address' /><br/>";
					echo 	"Password: <br/><input type='password' name='password' placeholder='Password'/><br/>";
					echo 	"<input type='submit' name='submit' value='Login'/>";
					echo 	"</form>";
					echo "<p>Not a member? <a href='register.php'>Register now!</a></p>";
				}
				$basket = "SELECT SUM(Quantity) As Totalquant FROM Basket WHERE UserID='$UserID'";//count items in basket and display them
				$num = mysqli_query($connect,$basket);
				$bresult = mysqli_fetch_assoc($num) or die($mysqli->error.__LINE__);
				echo "<a href='basket.php' id='basket'><img src='images/basket.png' height=70 id='basket'/></a>";
				echo $bresult['Totalquant'];

			?>
		</div>
		<div id="Centre">
			<h2>
				<?php
					$id = $_GET['id'];
					$getidinfo = "SELECT Name,Price,Price * Offers As newprice,Manufacturer,ProductID,Image,Description FROM Products WHERE ProductID='$id'";//fetch details of product and display in a table with a buy now button
					$getresult = $mysqli->query($getidinfo) or die($mysqli->error.__LINE__);					
					$idresult = mysqli_fetch_assoc($getresult);
					echo "<tbody><tr><td><form method='post' action='submit.php'>Manufacturer:<input type='text' name='manu' value='" . $idresult['Manufacturer'] . "'/></td><td>Name:<input type='text' name='Name' value='" . $idresult['Name'] . "'/></td><td><input type='text' name='Price' value='" . $idresult['Price'] . "'/></td></tr>";
				?>
			</h2>
		</div>
		</div>
	</body>
</html>

